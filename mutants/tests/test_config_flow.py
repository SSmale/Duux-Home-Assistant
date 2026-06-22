"""Unit tests for custom_components.duux.config_flow.DuuxConfigFlow."""

from unittest.mock import patch

from homeassistant.const import CONF_EMAIL, CONF_PASSWORD
from homeassistant.data_entry_flow import FlowResultType

from custom_components.duux.config_flow import DuuxConfigFlow


async def test_async_step_user_no_input_shows_form(fake_hass):
    flow = DuuxConfigFlow()
    flow.hass = fake_hass

    result = await flow.async_step_user(user_input=None)

    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "user"
    assert result["errors"] == {}


async def test_async_step_user_valid_credentials_creates_entry(fake_hass):
    flow = DuuxConfigFlow()
    flow.hass = fake_hass

    with patch(
        "custom_components.duux.config_flow.DuuxAPI.login", return_value=True
    ):
        result = await flow.async_step_user(
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

    with patch(
        "custom_components.duux.config_flow.DuuxAPI.login", return_value=False
    ):
        result = await flow.async_step_user(
            user_input={CONF_EMAIL: "user@example.com", CONF_PASSWORD: "wrong"}
        )

    assert result["type"] is FlowResultType.FORM
    assert result["errors"] == {"base": "invalid_auth"}
