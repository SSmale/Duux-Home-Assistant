"""Unit tests for custom_components.duux.diagnostics."""

from unittest.mock import MagicMock

import pytest

from custom_components.duux import const, diagnostics
from homeassistant.helpers.update_coordinator import UpdateFailed


async def test_diagnostics_redacts_sensitive_fields(fake_hass, devices_fixture):
    entry = MagicMock()
    entry.entry_id = "entry_1"
    api = MagicMock()
    api.get_devices.return_value = devices_fixture
    fake_hass.data[const.DOMAIN] = {"entry_1": {"api": api}}

    result = await diagnostics.async_get_config_entry_diagnostics(fake_hass, entry)

    assert len(result) == len(devices_fixture)
    for device in result:
        assert device["deviceId"] == "**REDACTED**"


async def test_diagnostics_wraps_api_errors(fake_hass):
    entry = MagicMock()
    entry.entry_id = "entry_1"
    api = MagicMock()
    api.get_devices.side_effect = RuntimeError("boom")
    fake_hass.data[const.DOMAIN] = {"entry_1": {"api": api}}

    with pytest.raises(UpdateFailed):
        await diagnostics.async_get_config_entry_diagnostics(fake_hass, entry)
