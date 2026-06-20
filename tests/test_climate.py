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
from homeassistant.components.climate.const import HVACMode, PRESET_BOOST


def attach_hass(entity, hass):
    entity.hass = hass
    return entity


# ---------------------------------------------------------------------------
# DuuxEdgeTwoClimate (low/high/boost)
# ---------------------------------------------------------------------------


def test_edge_two_climate_properties(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(50)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxEdgeTwoClimate(coordinator, mock_api, device)

    assert entity.target_temperature == 21
    assert entity.current_temperature == 19
    assert entity.hvac_mode == HVACMode.HEAT
    assert entity.preset_mode == entity.PRESET_HIGH  # heatin == 2
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
    entity = attach_hass(DuuxEdgeTwoClimate(coordinator, mock_api, device), make_hass())

    await entity.async_set_temperature(temperature=25)

    mock_api.set_temperature.assert_called_once_with(device["deviceId"], 25)
    assert entity.target_temperature == 25


async def test_edge_two_climate_set_hvac_mode_off_calls_set_power_false(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(50)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(DuuxEdgeTwoClimate(coordinator, mock_api, device), make_hass())

    await entity.async_set_hvac_mode(HVACMode.OFF)

    mock_api.set_power.assert_called_once_with(device["deviceId"], False)
    assert entity.hvac_mode == HVACMode.OFF


async def test_edge_two_climate_set_preset_mode_boost(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(50)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(DuuxEdgeTwoClimate(coordinator, mock_api, device), make_hass())

    await entity.async_set_preset_mode(PRESET_BOOST)

    mock_api.set_mode.assert_called_once_with(device["deviceId"], "3")
    assert entity.preset_mode == PRESET_BOOST


# ---------------------------------------------------------------------------
# DuuxEdgeClimate (low/high only -- no boost preset)
# ---------------------------------------------------------------------------


def test_edge_climate_has_no_boost_preset(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(51)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxEdgeClimate(coordinator, mock_api, device)

    assert entity.preset_modes == [entity.PRESET_LOW, entity.PRESET_HIGH]
    assert entity.preset_mode == entity.PRESET_LOW  # heatin == 1
    assert entity.hvac_mode == HVACMode.OFF  # power == 0 in fixture


# ---------------------------------------------------------------------------
# Threesixty climates -- presets discovered from "availableModes" trait data
# ---------------------------------------------------------------------------


def test_threesixty_climate_discovers_presets_from_fixture(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(49)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxThreesixtyClimate(coordinator, mock_api, device)

    # _normalize_mode_name maps value "2"->ECO, "1"->COMFORT, "0"->BOOST
    assert set(entity.preset_modes) == {"eco", "comfort", "boost"}
    assert entity.preset_mode == "eco"  # mode == "2" in fixture


async def test_threesixty_climate_set_preset_mode_sends_discovered_command(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(49)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxThreesixtyClimate(coordinator, mock_api, device), make_hass()
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
    entity = DuuxThreesixtyTwoClimate(coordinator, mock_api, device)

    assert entity.preset_mode == "comfort"  # mode == "1" in fixture


# ---------------------------------------------------------------------------
# DuuxClimateAutoDiscovery -- degenerate case (no availableModes anywhere)
# ---------------------------------------------------------------------------


def test_autodiscovery_with_no_modes_data_is_empty(make_coordinator, mock_api):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Mystery Heater"}
    coordinator = make_coordinator({"power": 1, "sp": 20, "temp": 18})
    entity = DuuxClimateAutoDiscovery(coordinator, mock_api, device)

    assert entity.preset_modes == []
    assert entity.preset_mode is None


# ---------------------------------------------------------------------------
# available / availability
# ---------------------------------------------------------------------------


def test_available_false_when_coordinator_update_failed(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(50)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    coordinator.last_update_success = False
    entity = DuuxEdgeTwoClimate(coordinator, mock_api, device)

    assert entity.available is False


def test_available_false_when_device_reports_offline(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(50)
    data = dict(device["latestData"]["fullData"])
    data["online"] = False
    coordinator = make_coordinator(data)
    entity = DuuxEdgeTwoClimate(coordinator, mock_api, device)

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
    entry = type("Entry", (), {"entry_id": "entry_1"})()
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

    entry = type("Entry", (), {"entry_id": "entry_1"})()
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
