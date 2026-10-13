"""Configuration and reauthentication for Duux."""

import asyncio
from typing import Any

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_EMAIL, CONF_PASSWORD
from homeassistant.core import callback

from .auth import (
    DuuxAuthenticationError,
    DuuxConnectionError,
    DuuxPasswordlessAuth,
    DuuxRateLimitError,
    DuuxResponseError,
)
from .const import AUTH_PASSWORDLESS, CONF_AUTH_METHOD, CONF_TOKEN, DOMAIN
from .duux_api import DuuxAPI


class DuuxConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle both password and email-code sign-in."""

    VERSION = 1

    def __init__(self) -> None:
        self._email = ""
        self._auth: DuuxPasswordlessAuth | None = None
        self._existing_entry: config_entries.ConfigEntry | None = None
        self._auth_lock = asyncio.Lock()
        self._removed = False

    async def _async_close_auth(self) -> None:
        async with self._auth_lock:
            if self._auth is not None:
                await self.hass.async_add_executor_job(self._auth.close)
                self._auth = None

    @callback
    def async_remove(self) -> None:
        """Discard the pending verifier and session when setup is cancelled."""
        self._removed = True
        if self._auth is not None:
            self.hass.async_create_task(self._async_close_auth())
        super().async_remove()

    def _account_error(self, email: str) -> str | None:
        if self._existing_entry is not None:
            if email.casefold() != self._existing_entry.data[CONF_EMAIL].casefold():
                return "wrong_account"
            return None
        # Entries created by older releases have no unique_id.
        if any(
            entry.data.get(CONF_EMAIL, "").casefold() == email.casefold()
            for entry in self._async_current_entries()
        ):
            return "already_configured"
        return None

    async def _async_finish(self, data: dict[str, Any]):
        await self._async_close_auth()
        if self._removed:
            return self.async_abort(reason="login_cancelled")
        if self._existing_entry is not None:
            updated = {
                key: value
                for key, value in self._existing_entry.data.items()
                if key not in (CONF_PASSWORD, CONF_TOKEN, CONF_AUTH_METHOD)
            }
            updated.update(data)
            return self.async_update_reload_and_abort(
                self._existing_entry, data=updated
            )
        if self._account_error(data[CONF_EMAIL]):
            return self.async_abort(reason="already_configured")
        await self.async_set_unique_id(data[CONF_EMAIL].casefold())
        self._abort_if_unique_id_configured()
        return self.async_create_entry(title=data[CONF_EMAIL], data=data)

    async def async_step_user(self, user_input=None):
        """Let the user choose a sign-in method."""
        await self._async_close_auth()
        return self.async_show_menu(
            step_id="user", menu_options=["passwordless", "password"]
        )

    async def async_step_password(self, user_input=None):
        """Keep the existing password sign-in available."""
        await self._async_close_auth()
        errors = {}
        if user_input is not None:
            email = user_input[CONF_EMAIL].strip()
            account_error = self._account_error(email)
            if account_error == "already_configured":
                return self.async_abort(reason=account_error)
            if account_error:
                errors["base"] = account_error
            else:
                api = DuuxAPI(email=email, password=user_input[CONF_PASSWORD])
                try:
                    logged_in = await self.hass.async_add_executor_job(api.login)
                finally:
                    await self.hass.async_add_executor_job(api.close)
                if logged_in:
                    return await self._async_finish(
                        {CONF_EMAIL: email, CONF_PASSWORD: user_input[CONF_PASSWORD]}
                    )
                errors["base"] = "invalid_auth"
        return self.async_show_form(
            step_id="password",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_EMAIL, default=self._email): str,
                    vol.Required(CONF_PASSWORD): str,
                }
            ),
            errors=errors,
        )

    async def async_step_passwordless(self, user_input=None):
        """Request an email code with a flow-local PKCE verifier."""
        errors = {}
        if user_input is not None:
            email = user_input[CONF_EMAIL].strip()
            account_error = self._account_error(email)
            if account_error == "already_configured":
                return self.async_abort(reason=account_error)
            if account_error:
                errors["base"] = account_error
            else:
                self._email = email
                await self._async_close_auth()
                if self._removed:
                    return self.async_abort(reason="login_cancelled")
                self._auth = DuuxPasswordlessAuth(email)
                try:
                    async with self._auth_lock:
                        if self._removed:
                            return self.async_abort(reason="login_cancelled")
                        await self.hass.async_add_executor_job(
                            self._auth.request_login_code
                        )
                except DuuxAuthenticationError:
                    errors["base"] = "invalid_auth"
                except DuuxConnectionError:
                    errors["base"] = "cannot_connect"
                except DuuxRateLimitError:
                    errors["base"] = "rate_limited"
                except DuuxResponseError:
                    errors["base"] = "invalid_response"
                else:
                    if self._removed:
                        return self.async_abort(reason="login_cancelled")
                    return await self.async_step_verify_code()
        return self.async_show_form(
            step_id="passwordless",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_EMAIL, default=self._email): str,
                }
            ),
            errors=errors,
        )

    async def async_step_verify_code(self, user_input=None):
        """Verify the emailed code, or request a replacement."""
        if self._removed:
            return self.async_abort(reason="login_cancelled")
        if self._auth is None:
            return await self.async_step_passwordless()
        errors = {}
        if user_input is not None:
            try:
                async with self._auth_lock:
                    if self._removed:
                        return self.async_abort(reason="login_cancelled")
                    if user_input.get("resend"):
                        await self.hass.async_add_executor_job(
                            self._auth.request_login_code
                        )
                    else:
                        token = await self.hass.async_add_executor_job(
                            self._auth.verify_code, user_input.get("code")
                        )
                if self._removed:
                    return self.async_abort(reason="login_cancelled")
                if not user_input.get("resend"):
                    return await self._async_finish(
                        {
                            CONF_EMAIL: self._email,
                            CONF_AUTH_METHOD: AUTH_PASSWORDLESS,
                            CONF_TOKEN: token,
                        }
                    )
            except DuuxAuthenticationError:
                errors["base"] = "invalid_code"
            except DuuxConnectionError:
                errors["base"] = "cannot_connect"
            except DuuxRateLimitError:
                errors["base"] = "rate_limited"
            except DuuxResponseError:
                errors["base"] = "invalid_response"
        if self._removed:
            return self.async_abort(reason="login_cancelled")
        return self.async_show_form(
            step_id="verify_code",
            data_schema=vol.Schema(
                {
                    vol.Optional("code"): str,
                    vol.Optional("resend", default=False): bool,
                }
            ),
            errors=errors,
            description_placeholders={"email": self._email},
        )

    async def async_step_reauth(self, entry_data):
        """Renew credentials without replacing the account's entities."""
        self._existing_entry = self._get_reauth_entry()
        self._email = self._existing_entry.data[CONF_EMAIL]
        return await self.async_step_reauth_confirm()

    async def async_step_reconfigure(self, user_input=None):
        """Allow an existing account to switch sign-in methods."""
        self._existing_entry = self._get_reconfigure_entry()
        self._email = self._existing_entry.data[CONF_EMAIL]
        return await self.async_step_reauth_confirm()

    async def async_step_reauth_confirm(self, user_input=None):
        """Offer either sign-in method for the existing account."""
        return self.async_show_menu(
            step_id="reauth_confirm",
            menu_options=["passwordless", "password"],
            description_placeholders={"email": self._email},
        )
