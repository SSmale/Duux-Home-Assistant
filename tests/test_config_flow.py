"""Unit tests for custom_components.duux.config_flow.DuuxConfigFlow."""

import asyncio
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from homeassistant.const import CONF_EMAIL, CONF_PASSWORD
from homeassistant.data_entry_flow import FlowResultType

from custom_components.duux.config_flow import DuuxConfigFlow


async def test_async_step_user_no_input_shows_login_menu(fake_hass):
    flow = DuuxConfigFlow()
    flow.hass = fake_hass

    result = await flow.async_step_user(user_input=None)

    assert result["type"] is FlowResultType.MENU
    assert result["step_id"] == "user"
    assert result["menu_options"] == ["passwordless", "password"]


async def test_async_step_user_valid_credentials_creates_entry(fake_hass):
    flow = DuuxConfigFlow()
    flow.hass = fake_hass
    flow._async_current_entries = MagicMock(return_value=[])
    flow.async_set_unique_id = AsyncMock()
    flow._abort_if_unique_id_configured = MagicMock()

    with patch("custom_components.duux.config_flow.DuuxAPI.login", return_value=True):
        result = await flow.async_step_password(
            user_input={CONF_EMAIL: "user@example.com", CONF_PASSWORD: "hunter2"}
        )

    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["title"] == "user@example.com"
    assert result["data"] == {
        CONF_EMAIL: "user@example.com",
        CONF_PASSWORD: "hunter2",
    }


async def test_async_step_user_invalid_credentials_shows_error(fake_hass):
    flow = DuuxConfigFlow()
    flow.hass = fake_hass

    with patch("custom_components.duux.config_flow.DuuxAPI.login", return_value=False):
        result = await flow.async_step_password(
            user_input={CONF_EMAIL: "user@example.com", CONF_PASSWORD: "wrong"}
        )

    assert result["type"] is FlowResultType.FORM
    assert result["errors"] == {"base": "invalid_auth"}


def make_flow(fake_hass):
    flow = DuuxConfigFlow()
    flow.hass = fake_hass
    flow._async_current_entries = MagicMock(return_value=[])
    flow.async_set_unique_id = AsyncMock()
    flow._abort_if_unique_id_configured = MagicMock()
    return flow


async def request_code(flow):
    with patch(
        "custom_components.duux.config_flow.DuuxPasswordlessAuth.request_login_code"
    ):
        return await flow.async_step_passwordless({"email": "user@example.com"})


async def test_passwordless_requests_email_then_code(fake_hass):
    flow = make_flow(fake_hass)
    result = await flow.async_step_passwordless()
    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "passwordless"

    result = await request_code(flow)
    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "verify_code"
    assert result["description_placeholders"] == {"email": "user@example.com"}


async def test_passwordless_persists_only_email_method_and_token(fake_hass):
    flow = make_flow(fake_hass)
    await request_code(flow)
    with patch(
        "custom_components.duux.config_flow.DuuxPasswordlessAuth.verify_code",
        return_value="synthetic-token",
    ):
        result = await flow.async_step_verify_code({"code": "Ab12Cd34"})

    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["data"] == {
        "email": "user@example.com",
        "auth_method": "passwordless",
        "token": "synthetic-token",
    }
    flow.async_set_unique_id.assert_awaited_once_with("user@example.com")
    assert flow._auth is None


@pytest.mark.parametrize(
    ("error_name", "expected_error"),
    [
        ("DuuxAuthenticationError", "invalid_code"),
        ("DuuxConnectionError", "cannot_connect"),
        ("DuuxRateLimitError", "rate_limited"),
        ("DuuxResponseError", "invalid_response"),
    ],
)
async def test_passwordless_verification_errors_leave_flow_retryable(
    fake_hass, error_name, expected_error
):
    from custom_components.duux import auth

    flow = make_flow(fake_hass)
    await request_code(flow)
    with patch(
        "custom_components.duux.config_flow.DuuxPasswordlessAuth.verify_code",
        side_effect=getattr(auth, error_name)("safe-error"),
    ):
        result = await flow.async_step_verify_code({"code": "incorrect"})
    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "verify_code"
    assert result["errors"] == {"base": expected_error}
    assert flow._auth is not None


async def test_passwordless_resend_stays_on_code_step(fake_hass):
    flow = make_flow(fake_hass)
    await request_code(flow)
    with (
        patch(
            "custom_components.duux.config_flow.DuuxPasswordlessAuth.request_login_code"
        ) as request,
        patch(
            "custom_components.duux.config_flow.DuuxPasswordlessAuth.verify_code"
        ) as verify,
    ):
        result = await flow.async_step_verify_code({"resend": True})
    request.assert_called_once()
    verify.assert_not_called()
    assert result["step_id"] == "verify_code"
    assert result["errors"] == {}


async def test_code_step_without_pending_flow_restarts_email_step(fake_hass):
    flow = make_flow(fake_hass)
    result = await flow.async_step_verify_code({"code": "Ab12Cd34"})
    assert result["step_id"] == "passwordless"


async def test_request_network_error_shows_email_form(fake_hass):
    from custom_components.duux.auth import DuuxConnectionError

    flow = make_flow(fake_hass)
    with patch(
        "custom_components.duux.config_flow.DuuxPasswordlessAuth.request_login_code",
        side_effect=DuuxConnectionError("safe-error"),
    ):
        result = await flow.async_step_passwordless({"email": "user@example.com"})
    assert result["step_id"] == "passwordless"
    assert result["errors"] == {"base": "cannot_connect"}


async def test_duplicate_legacy_account_aborts_before_sending_email(fake_hass):
    flow = make_flow(fake_hass)
    flow._async_current_entries.return_value = [
        SimpleNamespace(data={"email": "USER@example.com"})
    ]
    with patch(
        "custom_components.duux.config_flow.DuuxPasswordlessAuth.request_login_code"
    ) as request:
        result = await flow.async_step_passwordless({"email": "user@example.com"})
    assert result["type"] is FlowResultType.ABORT
    assert result["reason"] == "already_configured"
    request.assert_not_called()


async def test_reauth_updates_existing_entry_and_removes_password(fake_hass):
    flow = make_flow(fake_hass)
    flow.context = {"source": "reauth", "entry_id": "existing"}
    entry = SimpleNamespace(
        data={"email": "user@example.com", "password": "old-password", "extra": 1},
        entry_id="existing",
        title="user@example.com",
    )
    fake_hass.config_entries.async_get_known_entry = MagicMock(return_value=entry)
    fake_hass.config_entries.async_update_entry = MagicMock(return_value=True)
    fake_hass.config_entries.async_schedule_reload = MagicMock()
    result = await flow.async_step_reauth(entry.data)
    assert result["step_id"] == "reauth_confirm"
    assert result["type"] is FlowResultType.MENU

    await request_code(flow)
    with (
        patch(
            "custom_components.duux.config_flow.DuuxPasswordlessAuth.verify_code",
            return_value="replacement-token",
        ),
        patch("homeassistant.config_entries.persistent_notification.async_dismiss"),
    ):
        result = await flow.async_step_verify_code({"code": "Ab12Cd34"})
    assert result["type"] is FlowResultType.ABORT
    assert result["reason"] == "reauth_successful"
    update = fake_hass.config_entries.async_update_entry.call_args.kwargs
    assert update["entry"] is entry
    assert update["data"] == {
        "email": "user@example.com",
        "auth_method": "passwordless",
        "token": "replacement-token",
        "extra": 1,
    }
    fake_hass.config_entries.async_schedule_reload.assert_called_once_with("existing")


async def test_reauth_rejects_another_email_before_request(fake_hass):
    flow = make_flow(fake_hass)
    flow.context = {"source": "reauth", "entry_id": "existing"}
    entry = SimpleNamespace(
        data={"email": "original@example.com"}, title="original@example.com"
    )
    fake_hass.config_entries.async_get_known_entry = MagicMock(return_value=entry)
    await flow.async_step_reauth(entry.data)
    with patch(
        "custom_components.duux.config_flow.DuuxPasswordlessAuth.request_login_code"
    ) as request:
        result = await flow.async_step_passwordless({"email": "different@example.com"})
    assert result["errors"] == {"base": "wrong_account"}
    request.assert_not_called()


async def test_cancelled_flow_closes_auth_and_discards_pending_verifier(fake_hass):
    flow = make_flow(fake_hass)
    await request_code(flow)
    auth = flow._auth
    auth.code_verifier = "pending-verifier"
    auth.session = MagicMock()
    fake_hass.async_create_task = MagicMock()

    flow.async_remove()

    fake_hass.async_create_task.assert_called_once()
    await fake_hass.async_create_task.call_args.args[0]
    auth.session.close.assert_called_once()
    assert auth.code_verifier is None
    assert flow._auth is None


async def test_real_passwordless_client_runs_through_flow_without_saving_pkce(
    fake_hass,
):
    flow = make_flow(fake_hass)
    with patch("custom_components.duux.auth.requests.Session") as session:
        response = session.return_value.post.return_value
        response.status_code = 200
        response.json.return_value = {"data": "ok", "errorMessage": None}
        result = await flow.async_step_passwordless({"email": "user@example.com"})
        assert result["step_id"] == "verify_code"
        verifier = flow._auth.code_verifier
        response.json.return_value = {
            "data": {
                "token": "synthetic-token",
                "refresh_token": None,
                "username": "user@example.com",
            },
            "errorMessage": None,
        }
        result = await flow.async_step_verify_code({"code": "Ab12Cd34"})

    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["data"] == {
        "email": "user@example.com",
        "auth_method": "passwordless",
        "token": "synthetic-token",
    }
    assert session.return_value.post.call_count == 2
    assert (
        session.return_value.post.call_args.kwargs["json"]["codeVerifier"] == verifier
    )
    session.return_value.close.assert_called_once()


async def test_cancelled_inflight_reauth_does_not_update_credentials(fake_hass):
    flow = make_flow(fake_hass)
    flow.context = {"source": "reauth", "entry_id": "existing"}
    entry = SimpleNamespace(
        data={
            "email": "user@example.com",
            "auth_method": "passwordless",
            "token": "original-token",
        },
        title="user@example.com",
        entry_id="existing",
    )
    fake_hass.config_entries.async_get_known_entry = MagicMock(return_value=entry)
    fake_hass.config_entries.async_update_entry = MagicMock()
    fake_hass.config_entries.async_schedule_reload = MagicMock()
    await flow.async_step_reauth(entry.data)
    await request_code(flow)
    auth = flow._auth
    started = asyncio.Event()
    release = asyncio.Event()
    cleanup_tasks = []

    async def executor(func, *args):
        if func == auth.verify_code:
            started.set()
            await release.wait()
            return "replacement-token"
        return func(*args)

    def create_task(coro):
        task = asyncio.create_task(coro)
        cleanup_tasks.append(task)
        return task

    fake_hass.async_add_executor_job = executor
    fake_hass.async_create_task = create_task
    with (
        patch.object(auth.session, "close") as close,
        patch("homeassistant.config_entries.persistent_notification.async_dismiss"),
    ):
        pending = asyncio.create_task(flow.async_step_verify_code({"code": "Ab12Cd34"}))
        await started.wait()
        flow.async_remove()
        await asyncio.sleep(0)
        closed_while_verifying = close.called
        release.set()
        result = await pending
        await asyncio.gather(*cleanup_tasks)

    assert result["type"] is FlowResultType.ABORT
    assert result["reason"] == "login_cancelled"
    assert not closed_while_verifying
    fake_hass.config_entries.async_update_entry.assert_not_called()
    fake_hass.config_entries.async_schedule_reload.assert_not_called()
    assert entry.data["token"] == "original-token"
    assert flow._auth is None


async def test_reconfigure_switches_existing_password_account_to_email_code(fake_hass):
    flow = make_flow(fake_hass)
    flow.context = {"source": "reconfigure", "entry_id": "existing"}
    entry = SimpleNamespace(
        data={"email": "user@example.com", "password": "old-password"},
        title="user@example.com",
        entry_id="existing",
    )
    fake_hass.config_entries.async_get_known_entry = MagicMock(return_value=entry)
    fake_hass.config_entries.async_update_entry = MagicMock()
    fake_hass.config_entries.async_schedule_reload = MagicMock()

    result = await flow.async_step_reconfigure()
    assert result["type"] is FlowResultType.MENU
    await request_code(flow)
    with patch(
        "custom_components.duux.config_flow.DuuxPasswordlessAuth.verify_code",
        return_value="replacement-token",
    ):
        result = await flow.async_step_verify_code({"code": "Ab12Cd34"})

    assert result["type"] is FlowResultType.ABORT
    assert result["reason"] == "reconfigure_successful"
    update = fake_hass.config_entries.async_update_entry.call_args.kwargs
    assert update["entry"] is entry
    assert update["data"] == {
        "email": "user@example.com",
        "auth_method": "passwordless",
        "token": "replacement-token",
    }
    fake_hass.config_entries.async_schedule_reload.assert_called_once_with("existing")


async def test_reconfigure_password_login_discards_old_token(fake_hass):
    flow = make_flow(fake_hass)
    flow.context = {"source": "reconfigure", "entry_id": "existing"}
    entry = SimpleNamespace(
        data={
            "email": "user@example.com",
            "auth_method": "passwordless",
            "token": "old-token",
        },
        title="user@example.com",
        entry_id="existing",
    )
    fake_hass.config_entries.async_get_known_entry = MagicMock(return_value=entry)
    fake_hass.config_entries.async_update_entry = MagicMock()
    fake_hass.config_entries.async_schedule_reload = MagicMock()
    await flow.async_step_reconfigure()
    with patch("custom_components.duux.config_flow.DuuxAPI.login", return_value=True):
        result = await flow.async_step_password(
            {
                "email": "user@example.com",
                "password": "new-password",
            }
        )
    assert result["reason"] == "reconfigure_successful"
    assert fake_hass.config_entries.async_update_entry.call_args.kwargs["data"] == {
        "email": "user@example.com",
        "password": "new-password",
    }
