"""Duux email-code authentication using PKCE."""

import base64
import hashlib
import secrets
from typing import Any

import requests
from homeassistant.exceptions import HomeAssistantError

from .const import API_BASE_URL

API_PASSWORDLESS_CODE = "/auth/passwordlessLogin/code"
API_TOKEN = "/auth/token"
CLIENT_ID = "83f34a5fa5faca9023c78980a57a87b41f6972fc4ee45e9c"
REDIRECT_URI = "https://duux-deeplink.vercel.app/login/verify"
TENANT_ID = 44
REQUEST_TIMEOUT = 30


class DuuxAuthenticationError(HomeAssistantError):
    """Credentials, code, or token were rejected."""


class DuuxConnectionError(HomeAssistantError):
    """Duux could not be reached."""


class DuuxResponseError(HomeAssistantError):
    """Duux returned an unexpected response."""


class DuuxRateLimitError(HomeAssistantError):
    """Duux rejected a request because of rate limiting."""


class DuuxPasswordlessAuth:
    """Keep the PKCE verifier private to one email-code flow."""

    def __init__(self, email: str) -> None:
        self.email = email.strip()
        self.code_verifier: str | None = None
        self.session = requests.Session()

    def _post(self, path: str, payload: dict[str, Any]) -> Any:
        try:
            response = self.session.post(
                f"{API_BASE_URL}{path}", json=payload, timeout=REQUEST_TIMEOUT
            )
            if response.status_code == 429:
                raise DuuxRateLimitError("Too many authentication requests")
            if response.status_code in (400, 401, 403, 422):
                raise DuuxAuthenticationError("Authentication was rejected")
            response.raise_for_status()
        except requests.RequestException:
            raise DuuxConnectionError("Unable to contact Duux") from None
        try:
            body = response.json()
        except ValueError:
            raise DuuxResponseError("Invalid authentication response") from None
        if not isinstance(body, dict) or "data" not in body:
            raise DuuxResponseError("Invalid authentication response")
        if body.get("errorMessage"):
            raise DuuxAuthenticationError("Authentication was rejected")
        return body["data"]

    def request_login_code(self) -> None:
        """Send a new code; retain the old verifier if a resend fails."""
        verifier = secrets.token_urlsafe(96)
        challenge = (
            base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest())
            .decode()
            .rstrip("=")
        )
        data = self._post(
            API_PASSWORDLESS_CODE,
            {
                "email": self.email,
                "clientId": CLIENT_ID,
                "codeChallenge": challenge,
                # Duux calls the base64url SHA256 method "sha256", not "S256".
                "codeChallengeMethod": "sha256",
                "redirectUri": REDIRECT_URI,
                "tenantId": TENANT_ID,
            },
        )
        if data != "ok":
            raise DuuxResponseError("Invalid code request response")
        self.code_verifier = verifier

    def verify_code(self, code: str | None) -> str:
        """Exchange an email code for an account-bound long-lived token."""
        if not self.code_verifier or not isinstance(code, str) or not code.strip():
            raise DuuxAuthenticationError("Request a code and enter it to sign in")
        data = self._post(
            API_TOKEN,
            {
                "code": code.strip(),
                "codeVerifier": self.code_verifier,
                "grantType": "authorization_code",
                "clientId": CLIENT_ID,
                "redirectUri": REDIRECT_URI,
                "makeAccessTokenLongLasting": True,
            },
        )
        if not isinstance(data, dict):
            raise DuuxResponseError("Invalid token response")
        token = data.get("token")
        username = data.get("username")
        if (
            not isinstance(token, str)
            or not token.strip()
            or not isinstance(username, str)
            or not username.strip()
        ):
            raise DuuxResponseError("Missing token or account in response")
        if username.casefold() != self.email.casefold():
            raise DuuxAuthenticationError("The code belongs to another account")
        self.code_verifier = None
        return token

    def close(self) -> None:
        """Release the connection and discard pending login material."""
        self.code_verifier = None
        self.session.close()
