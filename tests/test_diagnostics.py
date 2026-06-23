"""Unit tests for custom_components.duux.diagnostics."""

from unittest.mock import MagicMock

import pytest

from custom_components.duux import const, diagnostics
from custom_components.duux.const import CONF_MODE_MAPPING, DEFAULT_MODE_MAPPING
from homeassistant.helpers.update_coordinator import UpdateFailed


def _make_entry(entry_id="entry_1", options=None):
    entry = MagicMock()
    entry.entry_id = entry_id
    entry.options = options or {}
    return entry


async def test_diagnostics_redacts_sensitive_fields(fake_hass, devices_fixture):
    entry = _make_entry()
    api = MagicMock()
    api.get_devices.return_value = devices_fixture
    fake_hass.data[const.DOMAIN] = {
        "entry_1": {"api": api, "devices": devices_fixture}
    }

    result = await diagnostics.async_get_config_entry_diagnostics(fake_hass, entry)

    assert "devices" in result
    assert "mode_mappings" in result
    for device in result["devices"]:
        assert device["deviceId"] == "**REDACTED**"


async def test_diagnostics_includes_default_mapping_for_unconfigured_devices(
    fake_hass, devices_fixture
):
    entry = _make_entry(options={})  # no custom mappings
    api = MagicMock()
    api.get_devices.return_value = devices_fixture
    fake_hass.data[const.DOMAIN] = {
        "entry_1": {"api": api, "devices": devices_fixture}
    }

    result = await diagnostics.async_get_config_entry_diagnostics(fake_hass, entry)

    for device_id, info in result["mode_mappings"].items():
        assert info["is_custom"] is False
        assert info["mapping"] == DEFAULT_MODE_MAPPING


async def test_diagnostics_shows_custom_mapping_flag(fake_hass, devices_fixture):
    device_id = devices_fixture[0]["deviceId"]
    custom = {"1": "eco", "2": "boost", "3": "comfort"}
    entry = _make_entry(options={CONF_MODE_MAPPING: {device_id: custom}})
    api = MagicMock()
    api.get_devices.return_value = devices_fixture
    fake_hass.data[const.DOMAIN] = {
        "entry_1": {"api": api, "devices": devices_fixture}
    }

    result = await diagnostics.async_get_config_entry_diagnostics(fake_hass, entry)

    assert result["mode_mappings"][device_id]["is_custom"] is True
    assert result["mode_mappings"][device_id]["mapping"] == custom


async def test_diagnostics_wraps_api_errors(fake_hass):
    entry = _make_entry()
    api = MagicMock()
    api.get_devices.side_effect = RuntimeError("boom")
    fake_hass.data[const.DOMAIN] = {"entry_1": {"api": api, "devices": []}}

    with pytest.raises(UpdateFailed):
        await diagnostics.async_get_config_entry_diagnostics(fake_hass, entry)
