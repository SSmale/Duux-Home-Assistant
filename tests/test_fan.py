"""Unit tests for custom_components.duux.fan."""

import pytest

from custom_components.duux import const
from custom_components.duux.fan import (
    DuuxAirPurifierFan,
    DuuxFanAutoDiscovery,
    DuuxWhisperFlexElevateFan,
    DuuxWhisperFlexFan,
    DuuxWhisperFlexTwoFan,
    DuuxWhisperFlexUltimateFan,
    async_setup_entry,
)


def attach_hass(entity, hass):
    entity.hass = hass
    return entity


# ---------------------------------------------------------------------------
# DuuxWhisperFlexFan (plain DuuxFan subclass, speed 1-25, 3 presets)
# ---------------------------------------------------------------------------


def test_whisper_flex_properties(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(36)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxWhisperFlexFan(coordinator, mock_api, device)

    assert entity.is_on is True
    assert entity.preset_mode == "normal"  # mode == 0
    assert entity.percentage is not None


async def test_whisper_flex_turn_on_sets_power_optimistically(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(36)
    data = dict(device["latestData"]["fullData"])
    data["power"] = 0
    coordinator = make_coordinator(data)
    entity = attach_hass(DuuxWhisperFlexFan(coordinator, mock_api, device), make_hass())

    await entity.async_turn_on()

    mock_api.set_power.assert_called_once_with(device["deviceId"], True)
    assert entity.is_on is True


async def test_whisper_flex_turn_off(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(36)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(DuuxWhisperFlexFan(coordinator, mock_api, device), make_hass())

    await entity.async_turn_off()

    mock_api.set_power.assert_called_once_with(device["deviceId"], 0)
    assert entity.is_on is False
    assert coordinator.data["power"] is False


async def test_whisper_flex_turn_on_with_percentage_passes_value(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(36)
    data = dict(device["latestData"]["fullData"])
    data["power"] = 0
    coordinator = make_coordinator(data)
    entity = attach_hass(DuuxWhisperFlexFan(coordinator, mock_api, device), make_hass())

    await entity.async_turn_on(percentage=50)

    mock_api.set_speed.assert_called_once()
    speed_sent = mock_api.set_speed.call_args.args[1]
    assert speed_sent is not None


async def test_whisper_flex_set_percentage_calls_set_speed_with_range(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(36)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(DuuxWhisperFlexFan(coordinator, mock_api, device), make_hass())

    await entity.async_set_percentage(50)

    mock_api.set_speed.assert_called_once()
    call_args = mock_api.set_speed.call_args.args
    assert call_args[0] == device["deviceId"]
    assert call_args[2] == entity._speed_range[0]
    assert call_args[3] == entity._speed_range[-1]
    assert coordinator.data["speed"] is not None
    assert coordinator.data["speed"] == call_args[1]


async def test_whisper_flex_set_percentage_zero_turns_off(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(36)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(DuuxWhisperFlexFan(coordinator, mock_api, device), make_hass())

    await entity.async_set_percentage(0)

    mock_api.set_power.assert_called_once_with(device["deviceId"], 0)
    mock_api.set_speed.assert_not_called()


async def test_whisper_flex_set_preset_mode_natural(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(36)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(DuuxWhisperFlexFan(coordinator, mock_api, device), make_hass())

    await entity.async_set_preset_mode("natural")

    mock_api.set_mode.assert_called_once_with(device["deviceId"], 1)
    assert entity.preset_mode == "natural"
    assert coordinator.data["mode"] == 1


@pytest.mark.parametrize(
    ("preset", "expected_mode_value"),
    [("normal", 0), ("natural", 1), ("night", 2)],
)
async def test_whisper_flex_set_preset_mode_updates_coordinator(
    preset, expected_mode_value, device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(36)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(DuuxWhisperFlexFan(coordinator, mock_api, device), make_hass())

    await entity.async_set_preset_mode(preset)

    assert coordinator.data["mode"] == expected_mode_value
    assert entity.preset_mode == preset


# ---------------------------------------------------------------------------
# DuuxWhisperFlexElevateFan (sensorTypeId 70, speed 1-26, oscillation)
# ---------------------------------------------------------------------------

_ELEVATE_DEVICE = {
    "id": 100012,
    "deviceId": "AA:00:00:00:00:12",
    "displayName": "Whisper Flex Elevate",
    "sensorType": {"type": 26, "name": "DUUX Whisper Flex Elevate"},
}


def test_whisper_flex_elevate_speed_range_is_1_to_26(make_coordinator, mock_api):
    coordinator = make_coordinator({"power": 1, "speed": 13, "mode": 0, "horosc": 0})
    entity = DuuxWhisperFlexElevateFan(coordinator, mock_api, _ELEVATE_DEVICE)

    assert entity._speed_range == list(range(1, 27))
    assert entity._attr_speed_count == 26


def test_whisper_flex_elevate_has_normal_and_natural_presets_only(
    make_coordinator, mock_api
):
    coordinator = make_coordinator({"power": 1, "speed": 1, "mode": 0})
    entity = DuuxWhisperFlexElevateFan(coordinator, mock_api, _ELEVATE_DEVICE)

    assert entity._attr_preset_modes == ["normal", "natural"]
    assert "night" not in entity._attr_preset_modes


async def test_whisper_flex_elevate_100_percent_sends_speed_26(
    make_coordinator, mock_api, make_hass
):
    """Regression: speed range ends at 26; 100% must NOT send 27."""
    coordinator = make_coordinator({"power": 1, "speed": 1, "mode": 0})
    entity = attach_hass(
        DuuxWhisperFlexElevateFan(coordinator, mock_api, _ELEVATE_DEVICE), make_hass()
    )

    await entity.async_set_percentage(100)

    mock_api.set_speed.assert_called_once()
    speed_sent = mock_api.set_speed.call_args.args[1]
    assert speed_sent == 26, f"Expected 26 but got {speed_sent}"


def test_whisper_flex_elevate_oscillating_reads_horosc(make_coordinator, mock_api):
    coordinator = make_coordinator({"power": 1, "horosc": 1})
    entity = DuuxWhisperFlexElevateFan(coordinator, mock_api, _ELEVATE_DEVICE)

    assert entity.oscillating is True

    coordinator.async_set_updated_data({"power": 1, "horosc": 0})
    assert entity.oscillating is False


async def test_whisper_flex_elevate_async_oscillate_on(
    make_coordinator, mock_api, make_hass
):
    coordinator = make_coordinator({"power": 1, "horosc": 0})
    entity = attach_hass(
        DuuxWhisperFlexElevateFan(coordinator, mock_api, _ELEVATE_DEVICE), make_hass()
    )

    await entity.async_oscillate(True)

    mock_api.set_horosc_bool.assert_called_once_with(_ELEVATE_DEVICE["deviceId"], 1)
    assert coordinator.data["horosc"] == 1


async def test_whisper_flex_elevate_async_oscillate_off(
    make_coordinator, mock_api, make_hass
):
    coordinator = make_coordinator({"power": 1, "horosc": 1})
    entity = attach_hass(
        DuuxWhisperFlexElevateFan(coordinator, mock_api, _ELEVATE_DEVICE), make_hass()
    )

    await entity.async_oscillate(False)

    mock_api.set_horosc_bool.assert_called_once_with(_ELEVATE_DEVICE["deviceId"], 0)
    assert coordinator.data["horosc"] == 0


# ---------------------------------------------------------------------------
# DuuxWhisperFlexTwoFan
# ---------------------------------------------------------------------------


def test_whisper_flex_two_has_only_normal_and_natural_presets(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(67)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxWhisperFlexTwoFan(coordinator, mock_api, device)

    assert entity._attr_preset_modes == ["normal", "natural"]


# ---------------------------------------------------------------------------
# DuuxWhisperFlexUltimateFan -- adds swing/tilt support (set via select.py)
# ---------------------------------------------------------------------------


def test_whisper_flex_ultimate_properties(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(40)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxWhisperFlexUltimateFan(coordinator, mock_api, device)

    assert entity._attr_preset_modes == ["normal", "natural", "night"]
    assert entity.is_on is True
    assert entity.preset_mode == "natural"  # mode == 1


async def test_whisper_flex_ultimate_set_preset_mode_night(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(40)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxWhisperFlexUltimateFan(coordinator, mock_api, device), make_hass()
    )

    await entity.async_set_preset_mode("night")

    mock_api.set_mode.assert_called_once_with(device["deviceId"], 2)
    assert entity.preset_mode == "night"


# ---------------------------------------------------------------------------
# DuuxAirPurifierFan (Bright 2) -- manual speed, auto mode, ionizer interplay
# ---------------------------------------------------------------------------


def test_air_purifier_percentage_in_manual_speed(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(61)
    coordinator = make_coordinator(device["latestData"]["fullData"])  # speed=2
    entity = DuuxAirPurifierFan(coordinator, mock_api, device)

    assert entity.preset_mode is None  # speed != 0, not in Auto
    assert entity.percentage == round(2 / 4 * 100)


def test_air_purifier_auto_mode_reported_when_speed_zero(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(61)
    data = dict(device["latestData"]["fullData"])
    data["speed"] = 0
    data["aq"] = 2
    coordinator = make_coordinator(data)
    entity = DuuxAirPurifierFan(coordinator, mock_api, device)

    assert entity.preset_mode == "Auto"
    # aq=2 -> estimated speed = min(2+1, 4) = 3
    assert entity.percentage == round(3 / 4 * 100)


def test_air_purifier_auto_mode_high_tvoc_forces_max_speed(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(61)
    data = dict(device["latestData"]["fullData"])
    data["speed"] = 0
    data["tvoc"] = 2  # > 1 -> Polluted/Harmful
    coordinator = make_coordinator(data)
    entity = DuuxAirPurifierFan(coordinator, mock_api, device)

    assert entity.percentage == 100


async def test_air_purifier_set_percentage_to_lowest_turns_off_ionizer(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(61)
    data = dict(device["latestData"]["fullData"])
    data["ion"] = 1
    coordinator = make_coordinator(data)
    entity = attach_hass(DuuxAirPurifierFan(coordinator, mock_api, device), make_hass())

    await entity.async_set_percentage(25)  # maps to speed 1 (lowest)

    mock_api.set_purifier_speed.assert_called_once_with(device["deviceId"], 1)
    mock_api.set_ionizer.assert_called_once_with(device["deviceId"], False)


async def test_air_purifier_set_percentage_does_not_touch_ionizer_when_already_off(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(61)
    data = dict(device["latestData"]["fullData"])
    data["ion"] = 0
    coordinator = make_coordinator(data)
    entity = attach_hass(DuuxAirPurifierFan(coordinator, mock_api, device), make_hass())

    await entity.async_set_percentage(25)  # maps to speed 1 (lowest)

    mock_api.set_ionizer.assert_not_called()


async def test_air_purifier_set_preset_mode_auto_sets_speed_zero(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(61)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(DuuxAirPurifierFan(coordinator, mock_api, device), make_hass())

    await entity.async_set_preset_mode("Auto")

    mock_api.set_purifier_speed.assert_called_once_with(device["deviceId"], 0)


async def test_air_purifier_set_percentage_zero_turns_off(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    """Regression: percentage=0 must call turn_off, not set_purifier_speed(1)."""
    device = device_by_stid(61)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(DuuxAirPurifierFan(coordinator, mock_api, device), make_hass())

    await entity.async_set_percentage(0)

    mock_api.set_power.assert_called_once_with(device["deviceId"], False)
    mock_api.set_purifier_speed.assert_not_called()


async def test_air_purifier_set_percentage_updates_coordinator_speed(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(61)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(DuuxAirPurifierFan(coordinator, mock_api, device), make_hass())

    await entity.async_set_percentage(75)

    speed_sent = mock_api.set_purifier_speed.call_args.args[1]
    assert coordinator.data["speed"] == speed_sent
    assert coordinator.data["speed"] is not None


async def test_air_purifier_set_preset_mode_auto_does_not_call_set_power_when_already_on(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    """if not self.is_on guard: set_power must NOT be called when already on."""
    device = device_by_stid(61)
    data = dict(device["latestData"]["fullData"])
    data["power"] = 1
    coordinator = make_coordinator(data)
    entity = attach_hass(DuuxAirPurifierFan(coordinator, mock_api, device), make_hass())

    await entity.async_set_preset_mode("Auto")

    mock_api.set_power.assert_not_called()
    mock_api.set_purifier_speed.assert_called_once_with(device["deviceId"], 0)


async def test_air_purifier_set_preset_mode_auto_updates_coordinator_speed_to_zero(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(61)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(DuuxAirPurifierFan(coordinator, mock_api, device), make_hass())

    await entity.async_set_preset_mode("Auto")

    assert coordinator.data["speed"] == 0


async def test_air_purifier_set_preset_mode_auto_calls_set_power_when_off(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(61)
    data = dict(device["latestData"]["fullData"])
    data["power"] = 0
    coordinator = make_coordinator(data)
    entity = attach_hass(DuuxAirPurifierFan(coordinator, mock_api, device), make_hass())

    await entity.async_set_preset_mode("Auto")

    mock_api.set_power.assert_called_once_with(device["deviceId"], True)


async def test_air_purifier_set_percentage_ensures_power_on_first(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(61)
    data = dict(device["latestData"]["fullData"])
    data["power"] = 0
    coordinator = make_coordinator(data)
    entity = attach_hass(DuuxAirPurifierFan(coordinator, mock_api, device), make_hass())

    await entity.async_set_percentage(50)

    mock_api.set_power.assert_called_once_with(device["deviceId"], True)


# ---------------------------------------------------------------------------
# DuuxFanAutoDiscovery -- degenerate (no Traits) case
# ---------------------------------------------------------------------------


def test_fan_autodiscovery_with_no_traits_has_no_speeds_or_presets(
    make_coordinator, mock_api
):
    device = {
        "id": 1,
        "deviceId": "AA:BB",
        "displayName": "Mystery Fan",
        "sensorType": {"name": "Mystery"},
    }
    coordinator = make_coordinator({"power": 1})
    entity = DuuxFanAutoDiscovery(coordinator, mock_api, device)

    assert entity._speed_range == []
    assert entity._attr_preset_modes is None
    assert entity.percentage is None


def test_fan_autodiscovery_parses_traits_for_speeds_and_modes(
    make_coordinator, mock_api
):
    device = {
        "id": 1,
        "deviceId": "AA:BB",
        "displayName": "Discovered Fan",
        "sensorType": {
            "name": "Discovered Fan",
            "Traits": [
                {
                    "name": "FanSpeed",
                    "commands": ["tune set speed {fanSpeed}"],
                    "settings": {
                        "availableFanSpeeds": {
                            "speeds": [
                                {"speed_name": "1"},
                                {"speed_name": "2"},
                                {"speed_name": "3"},
                            ]
                        }
                    },
                },
                {
                    "name": "Modes",
                    "commands": ["tune set mode {mode}"],
                    "settings": {
                        "availableModes": [
                            {
                                "command_key": "mode",
                                "settings": [
                                    {"setting_name": "Night", "setting_value": "2"}
                                ],
                            }
                        ]
                    },
                },
            ],
        },
    }
    coordinator = make_coordinator({"speed": "2", "mode": "2"})
    entity = DuuxFanAutoDiscovery(coordinator, mock_api, device)

    assert entity._speed_range == [1, 2, 3]
    assert entity._attr_preset_modes == ["Night"]
    assert entity.preset_mode == "Night"


async def test_fan_autodiscovery_set_preset_mode_sends_built_command(
    make_coordinator, mock_api, make_hass
):
    device = {
        "id": 1,
        "deviceId": "AA:BB",
        "displayName": "Discovered Fan",
        "sensorType": {
            "name": "Discovered Fan",
            "Traits": [
                {
                    "name": "Modes",
                    "commands": ["tune set mode {mode}"],
                    "settings": {
                        "availableModes": [
                            {
                                "command_key": "mode",
                                "settings": [
                                    {"setting_name": "Night", "setting_value": "2"}
                                ],
                            }
                        ]
                    },
                },
            ],
        },
    }
    coordinator = make_coordinator({"mode": "0"})
    entity = attach_hass(DuuxFanAutoDiscovery(coordinator, mock_api, device), make_hass())

    await entity.async_set_preset_mode("Night")

    mock_api.send_command.assert_called_once_with(device["deviceId"], "tune set mode 2")


# ---------------------------------------------------------------------------
# available
# ---------------------------------------------------------------------------


def test_available_false_when_device_offline(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(36)
    data = dict(device["latestData"]["fullData"])
    data["online"] = False
    coordinator = make_coordinator(data)
    entity = DuuxWhisperFlexFan(coordinator, mock_api, device)

    assert entity.available is False


# ---------------------------------------------------------------------------
# Platform dispatch
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

    assert classes_by_unique_id["duux_100008"] == "DuuxWhisperFlexFan"
    assert classes_by_unique_id["duux_100009"] == "DuuxWhisperFlexTwoFan"
    assert classes_by_unique_id["duux_100010"] == "DuuxAirPurifierFan"
    assert classes_by_unique_id["duux_100011"] == "DuuxWhisperFlexUltimateFan"
    assert classes_by_unique_id["duux_100012"] == "DuuxWhisperFlexElevateFan"
    fan_device_ids = {
        "duux_100008",
        "duux_100009",
        "duux_100010",
        "duux_100011",
        "duux_100012",
    }
    assert set(classes_by_unique_id) == fan_device_ids
