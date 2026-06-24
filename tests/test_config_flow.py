"""Unit tests for custom_components.duux.config_flow.DuuxConfigFlow."""

from unittest.mock import patch

from homeassistant.const import CONF_EMAIL, CONF_PASSWORD
from homeassistant.data_entry_flow import FlowResultType

from custom_components.duux.config_flow import DuuxConfigFlow, DuuxOptionsFlow
from custom_components.duux.const import CONF_MODE_MAPPING, DOMAIN
from homeassistant.components.climate.const import PRESET_BOOST, PRESET_COMFORT, PRESET_ECO


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


# ---------------------------------------------------------------------------
# DuuxOptionsFlow
# ---------------------------------------------------------------------------


def _make_options_flow(fake_hass, devices, existing_options=None):
    """Wire up a DuuxOptionsFlow with fake hass data."""
    entry = type(
        "Entry",
        (),
        {"entry_id": "entry_1", "options": existing_options or {}},
    )()
    fake_hass.config_entries.register(entry)
    fake_hass.data[DOMAIN] = {"entry_1": {"devices": devices}}

    flow = DuuxOptionsFlow()
    # Replicate what HA does when handing out an options flow
    flow.hass = fake_hass
    flow.handler = "entry_1"
    return flow, entry


async def test_options_flow_init_shows_device_selection(fake_hass):
    devices = [
        {"deviceId": "AA:01", "displayName": "Heater One", "sensorType": {"type": 51}},
        {"deviceId": "AA:02", "displayName": "Heater Two", "sensorType": {"type": 51}},
    ]
    flow, _ = _make_options_flow(fake_hass, devices)

    result = await flow.async_step_init(user_input=None)

    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "init"


async def test_options_flow_device_selection_navigates_to_mapping_form(fake_hass):
    devices = [{"deviceId": "AA:01", "displayName": "Heater One", "sensorType": {"type": 51}}]
    flow, entry = _make_options_flow(fake_hass, devices)
    # Prime the device list
    await flow.async_step_init(user_input=None)

    result = await flow.async_step_init(user_input={"device_id": "AA:01"})

    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "device_mode_mapping"
    assert flow._selected_device == "AA:01"


async def test_options_flow_no_device_selected_saves_existing_options(fake_hass):
    devices = [{"deviceId": "AA:01", "displayName": "Heater One", "sensorType": {"type": 51}}]
    existing = {CONF_MODE_MAPPING: {"AA:01": {"1": PRESET_ECO}}}
    flow, _ = _make_options_flow(fake_hass, devices, existing_options=existing)
    await flow.async_step_init(user_input=None)

    result = await flow.async_step_init(user_input={})

    assert result["type"] is FlowResultType.CREATE_ENTRY
    # Existing options are preserved unchanged
    assert result["data"] == existing


async def test_options_flow_device_mode_mapping_saves_options(fake_hass):
    devices = [{"deviceId": "AA:01", "displayName": "Heater One", "sensorType": {"type": 51}}]
    flow, _ = _make_options_flow(fake_hass, devices)
    await flow.async_step_init(user_input=None)
    await flow.async_step_init(user_input={"device_id": "AA:01"})

    result = await flow.async_step_device_mode_mapping(
        user_input={
            "mode_0": None,
            "mode_1": PRESET_ECO,
            "mode_2": PRESET_COMFORT,
            "mode_3": PRESET_BOOST,
        }
    )

    assert result["type"] is FlowResultType.CREATE_ENTRY
    saved_mapping = result["data"][CONF_MODE_MAPPING]["AA:01"]
    assert saved_mapping == {
        "0": None,
        "1": PRESET_ECO,
        "2": PRESET_COMFORT,
        "3": PRESET_BOOST,
    }


async def test_options_flow_preserves_other_device_mappings_when_saving(fake_hass):
    devices = [
        {"deviceId": "AA:01", "displayName": "Heater One", "sensorType": {"type": 51}},
        {"deviceId": "AA:02", "displayName": "Heater Two", "sensorType": {"type": 51}},
    ]
    existing_mapping = {"AA:02": {"1": PRESET_BOOST, "2": PRESET_ECO}}
    flow, _ = _make_options_flow(
        fake_hass, devices, existing_options={CONF_MODE_MAPPING: existing_mapping}
    )
    await flow.async_step_init(user_input=None)
    await flow.async_step_init(user_input={"device_id": "AA:01"})

    result = await flow.async_step_device_mode_mapping(
        user_input={
            "mode_0": None,
            "mode_1": PRESET_ECO,
            "mode_2": PRESET_COMFORT,
            "mode_3": PRESET_BOOST,
        }
    )

    assert result["type"] is FlowResultType.CREATE_ENTRY
    # AA:02's existing mapping must be untouched
    assert result["data"][CONF_MODE_MAPPING]["AA:02"] == existing_mapping["AA:02"]
