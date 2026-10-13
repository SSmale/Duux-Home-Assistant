"""Capture-backed passwordless protocol tests using synthetic credentials."""

import base64
import hashlib
from unittest.mock import MagicMock

import pytest
import requests


def make_auth():
    from custom_components.duux.auth import DuuxPasswordlessAuth

    auth = DuuxPasswordlessAuth("user@example.com")
    auth.session = MagicMock()
    auth.session.post.return_value.status_code = 200
    auth.session.post.return_value.json.return_value = {
        "data": "ok",
        "errorMessage": None,
    }
    return auth


def test_request_code_uses_observed_pkce_payload():
    auth = make_auth()
    auth.request_login_code()

    call = auth.session.post.call_args
    assert call.args == ("https://v5.api.cloudgarden.nl/auth/passwordlessLogin/code",)
    assert call.kwargs["timeout"] == 30
    payload = call.kwargs["json"]
    assert payload == {
        "email": "user@example.com",
        "clientId": "83f34a5fa5faca9023c78980a57a87b41f6972fc4ee45e9c",
        "redirectUri": "https://duux-deeplink.vercel.app/login/verify",
        "tenantId": 44,
        "codeChallengeMethod": "sha256",
        "codeChallenge": base64.urlsafe_b64encode(
            hashlib.sha256(auth.code_verifier.encode()).digest()
        )
        .decode()
        .rstrip("="),
    }
    assert 43 <= len(auth.code_verifier) <= 128


def test_verify_code_returns_nested_token_and_discards_verifier():
    auth = make_auth()
    auth.request_login_code()
    verifier = auth.code_verifier
    auth.session.post.return_value.json.return_value = {
        "data": {
            "token": "synthetic-token",
            "refresh_token": None,
            "username": "USER@example.com",
        },
        "errorMessage": None,
    }

    assert auth.verify_code("  Ab12Cd34  ") == "synthetic-token"
    call = auth.session.post.call_args
    assert call.args == ("https://v5.api.cloudgarden.nl/auth/token",)
    assert call.kwargs == {
        "timeout": 30,
        "json": {
            "code": "Ab12Cd34",
            "codeVerifier": verifier,
            "grantType": "authorization_code",
            "clientId": "83f34a5fa5faca9023c78980a57a87b41f6972fc4ee45e9c",
            "redirectUri": "https://duux-deeplink.vercel.app/login/verify",
            "makeAccessTokenLongLasting": True,
        },
    }
    assert auth.code_verifier is None


@pytest.mark.parametrize(
    "payload",
    [
        None,
        [],
        {"data": None},
        {"data": {}},
        {"data": {"token": 123}},
        {"data": {"token": ""}},
        {"data": {"token": "synthetic-token"}},
    ],
)
def test_verify_code_rejects_malformed_response(payload):
    from custom_components.duux.auth import DuuxResponseError

    auth = make_auth()
    auth.request_login_code()
    auth.session.post.return_value.json.return_value = payload
    with pytest.raises(DuuxResponseError):
        auth.verify_code("Ab12Cd34")


def test_verify_code_rejects_wrong_account():
    from custom_components.duux.auth import DuuxAuthenticationError

    auth = make_auth()
    auth.request_login_code()
    auth.session.post.return_value.json.return_value = {
        "data": {"token": "synthetic-token", "username": "different@example.com"},
        "errorMessage": None,
    }
    with pytest.raises(DuuxAuthenticationError):
        auth.verify_code("Ab12Cd34")


def test_rejected_code_can_be_retried_with_same_verifier():
    from custom_components.duux.auth import DuuxAuthenticationError

    auth = make_auth()
    auth.request_login_code()
    verifier = auth.code_verifier
    auth.session.post.return_value.status_code = 400
    with pytest.raises(DuuxAuthenticationError):
        auth.verify_code("incorrect")
    assert auth.code_verifier == verifier
    auth.session.post.return_value.status_code = 200
    auth.session.post.return_value.json.return_value = {
        "data": {"token": "synthetic-token", "username": auth.email},
    }
    assert auth.verify_code("Ab12Cd34") == "synthetic-token"


def test_resend_uses_new_verifier():
    auth = make_auth()
    auth.request_login_code()
    verifier = auth.code_verifier
    auth.request_login_code()
    assert auth.code_verifier != verifier


@pytest.mark.parametrize("code", ["", "   ", None])
def test_empty_code_is_rejected_without_network(code):
    from custom_components.duux.auth import DuuxAuthenticationError

    auth = make_auth()
    auth.request_login_code()
    auth.session.reset_mock()
    with pytest.raises(DuuxAuthenticationError):
        auth.verify_code(code)
    auth.session.post.assert_not_called()


def test_verify_without_requested_code_is_rejected():
    from custom_components.duux.auth import DuuxAuthenticationError

    auth = make_auth()
    with pytest.raises(DuuxAuthenticationError):
        auth.verify_code("Ab12Cd34")
    auth.session.post.assert_not_called()


def test_rate_limit_is_reported_and_failed_resend_keeps_verifier():
    from custom_components.duux.auth import DuuxRateLimitError

    auth = make_auth()
    auth.request_login_code()
    verifier = auth.code_verifier
    auth.session.post.return_value.status_code = 429
    with pytest.raises(DuuxRateLimitError):
        auth.request_login_code()
    assert auth.code_verifier == verifier


def test_network_error_does_not_expose_request_secrets():
    from custom_components.duux.auth import DuuxConnectionError

    auth = make_auth()
    auth.session.post.side_effect = requests.Timeout("secret-request-url")
    with pytest.raises(DuuxConnectionError) as exc:
        auth.request_login_code()
    assert "secret-request-url" not in str(exc.value)
    assert exc.value.__suppress_context__


def test_json_error_is_reported():
    from custom_components.duux.auth import DuuxResponseError

    auth = make_auth()
    auth.session.post.return_value.json.side_effect = ValueError("private-response")
    with pytest.raises(DuuxResponseError) as exc:
        auth.request_login_code()
    assert "private-response" not in str(exc.value)


def test_error_envelope_is_not_treated_as_success():
    from custom_components.duux.auth import DuuxAuthenticationError

    auth = make_auth()
    auth.session.post.return_value.json.return_value = {
        "data": None,
        "errorMessage": "private server error",
    }
    with pytest.raises(DuuxAuthenticationError) as exc:
        auth.request_login_code()
    assert "private server error" not in str(exc.value)


def test_close_discards_verifier_and_closes_session():
    auth = make_auth()
    auth.request_login_code()
    auth.close()
    assert auth.code_verifier is None
    auth.session.close.assert_called_once()


@pytest.mark.parametrize(
    "error_name",
    [
        "DuuxAuthenticationError",
        "DuuxConnectionError",
        "DuuxResponseError",
        "DuuxRateLimitError",
    ],
)
def test_api_errors_are_user_visible_home_assistant_errors(error_name):
    from homeassistant.exceptions import HomeAssistantError
    from custom_components.duux import auth

    assert isinstance(getattr(auth, error_name)("safe-error"), HomeAssistantError)
