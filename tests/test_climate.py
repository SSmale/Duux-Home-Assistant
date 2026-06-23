"""Unit tests for custom_components.duux.climate."""

from custom_components.duux import const
from custom_components.duux.climate import (
    DuuxClimateAutoDiscovery,
    DuuxEdgeClimate,
    DuuxEdgeTwoClimate,
    DuuxThreesixtyClimate,
    DuuxThreesixtyTwoClimate,
    async_setup_entry,
)
from custom_components.duux.const import (
    CONF_MODE_MAPPING,
    DEFAULT_MODE_MAPPING,
)
from homeassistant.components.climate.const import (
    HVACMode,
    PRESET_BOOST,
    PRESET_COMFORT,
    PRESET_ECO,
)


def attach_hass(entity, hass):
    entity.hass = hass
    return entity


def make_entry(options=None):
    """Create a minimal fake config entry with options."""
    return type("Entry", (), {"entry_id": "entry_1", "options": options or {}})()


# ---------------------------------------------------------------------------
# DuuxEdgeTwoClimate (low/high/boost) — uses DEFAULT_MODE_MAPPING {0,1,2}
# ---------------------------------------------------------------------------


def test_edge_two_climate_properties(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(50)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxEdgeTwoClimate(coordinator, mock_api, device, DEFAULT_MODE_MAPPING)

    assert entity.target_temperature == 21
    assert entity.current_temperature == 19
    assert entity.hvac_mode == HVACMode.HEAT
    assert entity.preset_mode == PRESET_BOOST  # heatin==2 → BOOST in default mapping
    assert entity.preset_modes == [
        entity.PRESET_LOW,
        entity.PRESET_HIGH,
        entity.PRESET_BOOST,
    ]
    assert entity.unique_id == f"duux_{device['id']}"


async def test_edge_two_climate_set_temperature(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(50)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxEdgeTwoClimate(coordinator, mock_api, device, DEFAULT_MODE_MAPPING),
        make_hass(),
    )

    await entity.async_set_temperature(temperature=25)

    mock_api.set_temperature.assert_called_once_with(device["deviceId"], 25)
    assert entity.target_temperature == 25


async def test_edge_two_climate_set_hvac_mode_off_calls_set_power_false(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(50)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxEdgeTwoClimate(coordinator, mock_api, device, DEFAULT_MODE_MAPPING),
        make_hass(),
    )

    await entity.async_set_hvac_mode(HVACMode.OFF)

    mock_api.set_power.assert_called_once_with(device["deviceId"], False)
    assert entity.hvac_mode == HVACMode.OFF


async def test_edge_two_climate_set_preset_mode_boost(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(50)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxEdgeTwoClimate(coordinator, mock_api, device, DEFAULT_MODE_MAPPING),
        make_hass(),
    )

    await entity.async_set_preset_mode(PRESET_BOOST)

    # reverse of {0: ECO, 1: COMFORT, 2: BOOST} → BOOST maps to index 2
    mock_api.set_mode.assert_called_once_with(device["deviceId"], 2)
    assert entity.preset_mode == PRESET_BOOST


async def test_edge_two_climate_custom_mapping_remaps_preset(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    """When a custom mapping swaps modes, preset_mode and set_preset_mode follow it."""
    device = device_by_stid(50)
    # heatin==2 is in the fixture; remap 2 → BOOST so preset_mode returns BOOST
    custom_mapping = {"1": PRESET_BOOST, "2": PRESET_ECO, "3": PRESET_COMFORT}
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxEdgeTwoClimate(coordinator, mock_api, device, custom_mapping),
        make_hass(),
    )

    assert entity.preset_mode == PRESET_ECO  # heatin==2 → ECO in custom mapping

    await entity.async_set_preset_mode(PRESET_BOOST)
    # reverse of custom: BOOST→1
    mock_api.set_mode.assert_called_once_with(device["deviceId"], 1)
    assert entity.preset_mode == PRESET_BOOST


# ---------------------------------------------------------------------------
# DuuxEdgeClimate (low/high only -- no boost preset)
# ---------------------------------------------------------------------------


def test_edge_climate_has_no_boost_preset(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(51)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxEdgeClimate(coordinator, mock_api, device, DEFAULT_MODE_MAPPING)

    assert entity.preset_modes == [entity.PRESET_LOW, entity.PRESET_HIGH]
    assert entity.preset_mode == entity.PRESET_HIGH  # heatin==1 → COMFORT in default mapping
    assert entity.hvac_mode == HVACMode.OFF  # power==0 in fixture


async def test_edge_climate_set_preset_mode_uses_configured_mapping(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(51)
    custom_mapping = {"1": PRESET_COMFORT, "2": PRESET_ECO}  # swapped
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxEdgeClimate(coordinator, mock_api, device, custom_mapping), make_hass()
    )

    assert entity.preset_mode == PRESET_COMFORT  # heatin==1 → COMFORT in custom mapping

    await entity.async_set_preset_mode(PRESET_ECO)
    mock_api.set_mode.assert_called_once_with(device["deviceId"], 2)
    assert entity.preset_mode == PRESET_ECO


# ---------------------------------------------------------------------------
# Threesixty climates -- presets discovered from "availableModes" trait data
# ---------------------------------------------------------------------------


def test_threesixty_climate_discovers_presets_from_fixture(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(49)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxThreesixtyClimate(coordinator, mock_api, device, DEFAULT_MODE_MAPPING)

    # _normalize_mode_name maps value "2"->ECO, "1"->COMFORT, "0"->BOOST
    assert set(entity.preset_modes) == {"eco", "comfort", "boost"}
    assert entity.preset_mode == "eco"  # mode == "2" in fixture


async def test_threesixty_climate_set_preset_mode_sends_discovered_command(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(49)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxThreesixtyClimate(coordinator, mock_api, device, DEFAULT_MODE_MAPPING),
        make_hass(),
    )

    await entity.async_set_preset_mode("boost")

    mock_api.send_command.assert_called_once_with(
        device["deviceId"], "tune set heating 0"
    )
    assert entity.preset_mode == "boost"


def test_threesixty_two_climate_also_discovers_presets(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(31)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxThreesixtyTwoClimate(coordinator, mock_api, device, DEFAULT_MODE_MAPPING)

    assert entity.preset_mode == "comfort"  # mode == "1" in fixture


# ---------------------------------------------------------------------------
# DuuxClimateAutoDiscovery -- degenerate case (no availableModes anywhere)
# ---------------------------------------------------------------------------


def test_autodiscovery_with_no_modes_data_is_empty(make_coordinator, mock_api):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Mystery Heater"}
    coordinator = make_coordinator({"power": 1, "sp": 20, "temp": 18})
    entity = DuuxClimateAutoDiscovery(coordinator, mock_api, device, DEFAULT_MODE_MAPPING)

    assert entity.preset_modes == []
    assert entity.preset_mode is None


# ---------------------------------------------------------------------------
# extra_state_attributes — mode mapping exposure and custom/default flag
# ---------------------------------------------------------------------------


def test_extra_state_attributes_default_mapping_flag(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(50)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxEdgeTwoClimate(coordinator, mock_api, device, DEFAULT_MODE_MAPPING)

    attrs = entity.extra_state_attributes
    assert CONF_MODE_MAPPING in attrs
    assert attrs[CONF_MODE_MAPPING]["is_custom"] is False
    assert "mapping" in attrs[CONF_MODE_MAPPING]
    assert attrs["raw_heatin_index"] == 2  # heatin==2 in fixture


def test_extra_state_attributes_custom_mapping_flag(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(50)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    custom_mapping = {"1": PRESET_BOOST, "2": PRESET_ECO, "3": PRESET_COMFORT}
    entity = DuuxEdgeTwoClimate(coordinator, mock_api, device, custom_mapping)

    attrs = entity.extra_state_attributes
    assert attrs[CONF_MODE_MAPPING]["is_custom"] is True


# ---------------------------------------------------------------------------
# available / availability
# ---------------------------------------------------------------------------


def test_available_false_when_coordinator_update_failed(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(50)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    coordinator.last_update_success = False
    entity = DuuxEdgeTwoClimate(coordinator, mock_api, device, DEFAULT_MODE_MAPPING)

    assert entity.available is False


def test_available_false_when_device_reports_offline(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(50)
    data = dict(device["latestData"]["fullData"])
    data["online"] = False
    coordinator = make_coordinator(data)
    entity = DuuxEdgeTwoClimate(coordinator, mock_api, device, DEFAULT_MODE_MAPPING)

    assert entity.available is False


# ---------------------------------------------------------------------------
# Platform dispatch (async_setup_entry)
# ---------------------------------------------------------------------------


async def test_async_setup_entry_dispatches_correct_entity_classes(
    fake_hass, devices_fixture, make_coordinator
):
    coordinators = {
        d["deviceId"]: make_coordinator(d["latestData"]["fullData"])
        for d in devices_fixture
    }
    entry = make_entry()
    fake_hass.data[const.DOMAIN] = {
        "entry_1": {
            "api": object(),
            "coordinators": coordinators,
            "devices": devices_fixture,
        }
    }

    added = []
    await async_setup_entry(fake_hass, entry, added.append)
    entities = added[0]

    classes_by_unique_id = {e.unique_id: type(e).__name__ for e in entities}

    assert classes_by_unique_id["duux_100001"] == "DuuxEdgeTwoClimate"
    assert classes_by_unique_id["duux_100002"] == "DuuxEdgeClimate"
    assert classes_by_unique_id["duux_100003"] == "DuuxThreesixtyClimate"
    assert classes_by_unique_id["duux_100004"] == "DuuxThreesixtyTwoClimate"
    # Non-heater/thermostat devices (humidifiers, fans) must not get a
    # climate entity at all.
    climate_device_ids = {"duux_100001", "duux_100002", "duux_100003", "duux_100004"}
    assert set(classes_by_unique_id) == climate_device_ids


async def test_async_setup_entry_uses_default_mapping_when_no_options(
    fake_hass, devices_fixture, make_coordinator
):
    """Entry with empty options falls back to DEFAULT_MODE_MAPPING per device."""
    coordinators = {
        d["deviceId"]: make_coordinator(d["latestData"]["fullData"])
        for d in devices_fixture
    }
    entry = make_entry()
    fake_hass.data[const.DOMAIN] = {
        "entry_1": {
            "api": object(),
            "coordinators": coordinators,
            "devices": devices_fixture,
        }
    }

    added = []
    await async_setup_entry(fake_hass, entry, added.append)
    entities = added[0]

    edge_v2 = next(e for e in entities if isinstance(e, DuuxEdgeTwoClimate))
    assert edge_v2._device_mode_mapping is DEFAULT_MODE_MAPPING
    assert edge_v2.extra_state_attributes[CONF_MODE_MAPPING]["is_custom"] is False


async def test_async_setup_entry_applies_custom_mapping(
    fake_hass, devices_fixture, make_coordinator
):
    """Custom options mapping is passed through to the entity."""
    device = next(d for d in devices_fixture if d["sensorTypeId"] == 50)
    coordinators = {
        d["deviceId"]: make_coordinator(d["latestData"]["fullData"])
        for d in devices_fixture
    }
    custom = {"1": PRESET_BOOST, "2": PRESET_ECO, "3": PRESET_COMFORT}
    entry = make_entry(options={CONF_MODE_MAPPING: {device["deviceId"]: custom}})
    fake_hass.data[const.DOMAIN] = {
        "entry_1": {
            "api": object(),
            "coordinators": coordinators,
            "devices": devices_fixture,
        }
    }

    added = []
    await async_setup_entry(fake_hass, entry, added.append)
    entities = added[0]

    edge_v2 = next(e for e in entities if isinstance(e, DuuxEdgeTwoClimate))
    assert edge_v2._device_mode_mapping == custom
    assert edge_v2.extra_state_attributes[CONF_MODE_MAPPING]["is_custom"] is True


async def test_async_setup_entry_falls_back_to_autodiscovery_for_unknown_stid(
    fake_hass, make_coordinator
):
    device = {
        "id": 555,
        "deviceId": "AA:UNKNOWN",
        "displayName": "New Heater",
        "sensorTypeId": 9999,
        "sensorType": {
            "type": const.DUUX_DTID_HEATER[0],
            "name": "Mystery Heater",
            "googleDeviceType": "action.devices.types.HEATER",
        },
    }
    coordinators = {device["deviceId"]: make_coordinator({})}

    entry = make_entry()
    fake_hass.data[const.DOMAIN] = {
        "entry_1": {
            "api": object(),
            "coordinators": coordinators,
            "devices": [device],
        }
    }

    added = []
    await async_setup_entry(fake_hass, entry, added.append)

    assert len(added[0]) == 1
    assert isinstance(added[0][0], DuuxClimateAutoDiscovery)
