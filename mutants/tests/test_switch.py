"""Unit tests for custom_components.duux.switch."""

import pytest

from custom_components.duux import const
from custom_components.duux.switch import (
    DuuxChildLockSwitch,
    DuuxCleaningModeSwitch,
    DuuxIonizerSwitch,
    DuuxLaundryModeSwitch,
    DuuxNightModeSwitch,
    DuuxSleepModeSwitch,
    async_setup_entry,
)


def attach_hass(entity, hass):
    entity.hass = hass
    return entity


# Each (switch class, coordinator data key, api method name) triple covers
# every simple on/off switch in one parametrized sweep.
SWITCH_CASES = [
    (DuuxChildLockSwitch, "lock", "set_lock"),
    (DuuxNightModeSwitch, "night", "set_night_mode"),
    (DuuxSleepModeSwitch, "sleep", "set_sleep_mode"),
    (DuuxCleaningModeSwitch, "dry", "set_cleaning_mode"),
    (DuuxLaundryModeSwitch, "laundr", "set_laundry_mode"),
]


@pytest.mark.parametrize("switch_cls,data_key,api_method", SWITCH_CASES)
def test_is_on_reflects_coordinator_data(
    switch_cls, data_key, api_method, make_coordinator, mock_api
):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Test"}

    on_entity = switch_cls(make_coordinator({data_key: 1}), mock_api, device)
    off_entity = switch_cls(make_coordinator({data_key: 0}), mock_api, device)
    missing_entity = switch_cls(make_coordinator({}), mock_api, device)

    assert on_entity.is_on is True
    assert off_entity.is_on is False
    assert missing_entity.is_on is False


@pytest.mark.parametrize("switch_cls,data_key,api_method", SWITCH_CASES)
async def test_turn_on_calls_correct_api_method(
    switch_cls, data_key, api_method, make_coordinator, mock_api, make_hass
):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Test"}
    coordinator = make_coordinator({data_key: 0})
    entity = attach_hass(switch_cls(coordinator, mock_api, device), make_hass())

    await entity.async_turn_on()

    getattr(mock_api, api_method).assert_called_once_with("AA:BB", True)
    assert entity.is_on is True


@pytest.mark.parametrize("switch_cls,data_key,api_method", SWITCH_CASES)
async def test_turn_off_calls_correct_api_method(
    switch_cls, data_key, api_method, make_coordinator, mock_api, make_hass
):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Test"}
    coordinator = make_coordinator({data_key: 1})
    entity = attach_hass(switch_cls(coordinator, mock_api, device), make_hass())

    await entity.async_turn_off()

    getattr(mock_api, api_method).assert_called_once_with("AA:BB", False)


# ---------------------------------------------------------------------------
# DuuxIonizerSwitch -- has extra Bright 2 speed-1 constraint logic
# ---------------------------------------------------------------------------


def test_ionizer_unavailable_when_bright2_speed_is_one(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(61)  # Bright 2
    data = dict(device["latestData"]["fullData"])
    data["speed"] = 1
    coordinator = make_coordinator(data)
    entity = DuuxIonizerSwitch(coordinator, mock_api, device)

    assert entity.available is False


def test_ionizer_available_in_auto_mode_speed_zero(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(61)
    data = dict(device["latestData"]["fullData"])
    data["speed"] = 0
    coordinator = make_coordinator(data)
    entity = DuuxIonizerSwitch(coordinator, mock_api, device)

    assert entity.available is True


async def test_ionizer_turn_on_blocked_when_speed_is_one(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(61)
    data = dict(device["latestData"]["fullData"])
    data["speed"] = 1
    coordinator = make_coordinator(data)
    entity = attach_hass(DuuxIonizerSwitch(coordinator, mock_api, device), make_hass())

    await entity.async_turn_on()

    mock_api.set_ionizer.assert_not_called()


async def test_ionizer_turn_on_allowed_when_speed_not_one(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(61)
    data = dict(device["latestData"]["fullData"])
    data["speed"] = 2
    coordinator = make_coordinator(data)
    entity = attach_hass(DuuxIonizerSwitch(coordinator, mock_api, device), make_hass())

    await entity.async_turn_on()

    mock_api.set_ionizer.assert_called_once_with(device["deviceId"], True)
    assert entity.is_on is True


# ---------------------------------------------------------------------------
# Platform dispatch
# ---------------------------------------------------------------------------


async def test_async_setup_entry_dispatches_expected_switches_per_device(
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

    by_device = {}
    for entity in entities:
        by_device.setdefault(entity._device_mac, []).append(type(entity).__name__)

    # Edge Heater V2 (STID 50): child lock + night mode
    assert sorted(by_device["AA:00:00:00:00:01"]) == [
        "DuuxChildLockSwitch",
        "DuuxNightModeSwitch",
    ]
    # Bora 2024 (STID 62): lock, sleep, cleaning, laundry
    assert sorted(by_device["AA:00:00:00:00:05"]) == [
        "DuuxChildLockSwitch",
        "DuuxCleaningModeSwitch",
        "DuuxLaundryModeSwitch",
        "DuuxSleepModeSwitch",
    ]
    # Neo (STID 47): night mode only
    assert by_device["AA:00:00:00:00:07"] == ["DuuxNightModeSwitch"]
    # Bright 2 (STID 61): night mode + ionizer
    assert sorted(by_device["AA:00:00:00:00:10"]) == [
        "DuuxIonizerSwitch",
        "DuuxNightModeSwitch",
    ]
    # Beam Mini and Whisper Flex (plain) get no switches at all.
    assert "AA:00:00:00:00:06" not in by_device
    assert "AA:00:00:00:00:08" not in by_device
