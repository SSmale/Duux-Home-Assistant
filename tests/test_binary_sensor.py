"""Unit tests for custom_components.duux.binary_sensor."""

from custom_components.duux import const
from custom_components.duux.binary_sensor import (
    DuuxConnectivitySensor,
    DuuxErrorSensor,
    async_setup_entry,
)


# ---------------------------------------------------------------------------
# DuuxErrorSensor (binary "problem" sensor)
# ---------------------------------------------------------------------------


def test_error_binary_sensor_off_when_ok(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(61)
    coordinator = make_coordinator(device["latestData"]["fullData"])  # err == 0 (OK)
    entity = DuuxErrorSensor(coordinator, mock_api, device)

    assert entity.is_on is False
    assert entity.extra_state_attributes == {"error_code": 0}


def test_error_binary_sensor_on_when_error_present(make_coordinator, mock_api):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Heater"}
    coordinator = make_coordinator({"err": 4})  # Ice_Detected
    entity = DuuxErrorSensor(coordinator, mock_api, device)

    assert entity.is_on is True


def test_error_binary_sensor_off_when_err_missing(make_coordinator, mock_api):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Heater"}
    coordinator = make_coordinator({})
    entity = DuuxErrorSensor(coordinator, mock_api, device)

    assert entity.is_on is False


# ---------------------------------------------------------------------------
# DuuxConnectivitySensor -- reads from the device envelope, not coordinator.data
# ---------------------------------------------------------------------------


def test_connectivity_sensor_reflects_device_online_flag(make_coordinator, mock_api):
    device = {
        "id": 1,
        "deviceId": "AA:BB",
        "displayName": "Heater",
        "online": True,
        "connectionType": "mqtt",
        "connectionUpdateDate": "2026-01-01T00:00:00Z",
    }
    coordinator = make_coordinator({})
    entity = DuuxConnectivitySensor(coordinator, mock_api, device)

    assert entity.is_on is True
    assert entity.extra_state_attributes == {
        "last_seen": "2026-01-01T00:00:00Z",
        "connection_type": "mqtt",
    }


def test_connectivity_sensor_off_when_device_offline(make_coordinator, mock_api):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Heater", "online": False}
    coordinator = make_coordinator({})
    entity = DuuxConnectivitySensor(coordinator, mock_api, device)

    assert entity.is_on is False


def test_connectivity_sensor_off_when_online_key_missing(make_coordinator, mock_api):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Heater"}
    coordinator = make_coordinator({})
    entity = DuuxConnectivitySensor(coordinator, mock_api, device)

    assert entity.is_on is False


# ---------------------------------------------------------------------------
# Platform dispatch -- every device gets exactly these two binary sensors
# ---------------------------------------------------------------------------


async def test_async_setup_entry_adds_error_and_connectivity_for_every_device(
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

    assert len(entities) == len(devices_fixture) * 2

    by_device = {}
    for entity in entities:
        by_device.setdefault(entity._device_mac, []).append(type(entity).__name__)

    for device in devices_fixture:
        assert sorted(by_device[device["deviceId"]]) == sorted(
            ["DuuxErrorSensor", "DuuxConnectivitySensor"]
        )
