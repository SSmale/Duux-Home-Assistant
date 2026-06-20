"""Unit tests for custom_components.duux.select."""

from custom_components.duux import const
from custom_components.duux.select import (
    DuuxBright2TimerSelector,
    DuuxFanSpeedSelector,
    DuuxHorizontalOscillationSelect,
    DuuxHorizontalSwingSelect,
    DuuxNeoSpeedSelector,
    DuuxTimerSelector,
    DuuxVerticalOscillationSelect,
    DuuxVerticalTiltSelect,
    async_setup_entry,
)


def attach_hass(entity, hass):
    entity.hass = hass
    return entity


# ---------------------------------------------------------------------------
# Oscillation selects (horosc/verosc -- the original swing buttons)
# ---------------------------------------------------------------------------


def test_horizontal_oscillation_current_option(make_coordinator, mock_api):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Fan"}
    coordinator = make_coordinator({"horosc": 2})
    entity = DuuxHorizontalOscillationSelect(coordinator, mock_api, device)

    assert entity.current_option == "60°"
    assert entity.options == ["Off", "30°", "60°", "90°"]


async def test_horizontal_oscillation_select_option_calls_set_horosc(
    make_coordinator, mock_api, make_hass
):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Fan"}
    coordinator = make_coordinator({"horosc": 0})
    entity = attach_hass(
        DuuxHorizontalOscillationSelect(coordinator, mock_api, device), make_hass()
    )

    await entity.async_select_option("90°")

    mock_api.set_horosc.assert_called_once_with("AA:BB", 3)
    assert entity.current_option == "90°"


async def test_swing_family_unknown_option_is_ignored(
    make_coordinator, mock_api, make_hass
):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Fan"}
    coordinator = make_coordinator({"horosc": 0})
    entity = attach_hass(
        DuuxHorizontalOscillationSelect(coordinator, mock_api, device), make_hass()
    )

    await entity.async_select_option("not-a-real-option")

    mock_api.set_horosc.assert_not_called()


def test_swing_family_current_option_with_unrecognised_raw_value_returns_none(
    make_coordinator, mock_api
):
    """Regression guard: logging an unmatched raw value must not crash --
    these entities never set _attr_name (they use translation_key naming)."""
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Fan"}
    coordinator = make_coordinator({"horosc": 999})  # not in HORIZONTAL_SWING_OPTIONS
    entity = DuuxHorizontalOscillationSelect(coordinator, mock_api, device)

    assert entity.current_option is None


def test_vertical_oscillation_current_option(make_coordinator, mock_api):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Fan"}
    coordinator = make_coordinator({"verosc": 1})
    entity = DuuxVerticalOscillationSelect(coordinator, mock_api, device)

    assert entity.current_option == "45°"


async def test_vertical_oscillation_select_option_calls_set_verosc(
    make_coordinator, mock_api, make_hass
):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Fan"}
    coordinator = make_coordinator({"verosc": 0})
    entity = attach_hass(
        DuuxVerticalOscillationSelect(coordinator, mock_api, device), make_hass()
    )

    await entity.async_select_option("100°")

    mock_api.set_verosc.assert_called_once_with("AA:BB", 2)
    assert entity.current_option == "100°"


# ---------------------------------------------------------------------------
# Swing/tilt selects (the Whisper Flex Ultimate's separate "swing"/"tilt" axes)
# ---------------------------------------------------------------------------


def test_horizontal_swing_current_option(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(40)  # Whisper Flex Ultimate fixture
    coordinator = make_coordinator(device["latestData"]["fullData"])  # swing == 2
    entity = DuuxHorizontalSwingSelect(coordinator, mock_api, device)

    assert entity.current_option == "60°"


async def test_horizontal_swing_select_option_calls_set_swing(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(40)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxHorizontalSwingSelect(coordinator, mock_api, device), make_hass()
    )

    await entity.async_select_option("90°")

    mock_api.set_swing.assert_called_once_with(device["deviceId"], 3)
    assert entity.current_option == "90°"


def test_vertical_tilt_current_option(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(40)
    coordinator = make_coordinator(device["latestData"]["fullData"])  # tilt == 1
    entity = DuuxVerticalTiltSelect(coordinator, mock_api, device)

    assert entity.current_option == "45°"


async def test_vertical_tilt_select_option_calls_set_tilt(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(40)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxVerticalTiltSelect(coordinator, mock_api, device), make_hass()
    )

    await entity.async_select_option("100°")

    mock_api.set_tilt.assert_called_once_with(device["deviceId"], 2)
    assert entity.current_option == "100°"


# ---------------------------------------------------------------------------
# DuuxFanSpeedSelector (Bora) -- note the inverted high/low API mapping
# ---------------------------------------------------------------------------


def test_fan_speed_selector_current_option(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(62)
    coordinator = make_coordinator(device["latestData"]["fullData"])  # fan == 1
    entity = DuuxFanSpeedSelector(coordinator, mock_api, device)

    assert entity.current_option == entity.FAN_LOW


def test_fan_speed_selector_current_option_defaults_when_missing(
    make_coordinator, mock_api
):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Fan"}
    coordinator = make_coordinator({})
    entity = DuuxFanSpeedSelector(coordinator, mock_api, device)

    assert entity.current_option == entity.FAN_LOW


async def test_fan_speed_selector_select_high(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(62)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxFanSpeedSelector(coordinator, mock_api, device), make_hass()
    )

    await entity.async_select_option(entity.FAN_HIGH)

    mock_api.set_fan.assert_called_once_with(device["deviceId"], "0")
    assert entity.current_option == entity.FAN_HIGH


# ---------------------------------------------------------------------------
# DuuxTimerSelector / DuuxBright2TimerSelector
# ---------------------------------------------------------------------------


def test_timer_selector_current_option(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(62)
    coordinator = make_coordinator(device["latestData"]["fullData"])  # timer == 4
    entity = DuuxTimerSelector(coordinator, mock_api, device)

    assert entity.current_option == "4"
    assert entity.options == [str(n) for n in range(0, 25)]


def test_timer_selector_current_option_none_when_missing(make_coordinator, mock_api):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Fan"}
    coordinator = make_coordinator({})
    entity = DuuxTimerSelector(coordinator, mock_api, device)

    assert entity.current_option is None


async def test_timer_selector_select_option_clamps_to_max(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(62)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(DuuxTimerSelector(coordinator, mock_api, device), make_hass())

    await entity.async_select_option("99")

    mock_api.set_timer.assert_called_once_with(device["deviceId"], "24")
    assert entity.current_option == "24"


async def test_timer_selector_select_invalid_option_defaults_to_zero(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(62)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(DuuxTimerSelector(coordinator, mock_api, device), make_hass())

    await entity.async_select_option("not-a-number")

    mock_api.set_timer.assert_called_once_with(device["deviceId"], "0")


def test_bright2_timer_selector_has_restricted_presets(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(61)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxBright2TimerSelector(coordinator, mock_api, device)

    assert entity.options == ["0", "1", "2", "4", "8"]


# ---------------------------------------------------------------------------
# DuuxNeoSpeedSelector
# ---------------------------------------------------------------------------


def test_neo_speed_selector_current_option(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(47)
    coordinator = make_coordinator(device["latestData"]["fullData"])  # speed == 1
    entity = DuuxNeoSpeedSelector(coordinator, mock_api, device)

    assert entity.current_option == entity.SPEED_MID


async def test_neo_speed_selector_select_high(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(47)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxNeoSpeedSelector(coordinator, mock_api, device), make_hass()
    )

    await entity.async_select_option(entity.SPEED_HIGH)

    mock_api.set_speed.assert_called_once_with(device["deviceId"], "2", 0, 2)
    assert entity.current_option == entity.SPEED_HIGH


# ---------------------------------------------------------------------------
# Platform dispatch
# ---------------------------------------------------------------------------


async def test_async_setup_entry_dispatches_expected_selects_per_device(
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

    # Bora 2024 (STID 62): fan speed + timer
    assert sorted(by_device["AA:00:00:00:00:05"]) == [
        "DuuxFanSpeedSelector",
        "DuuxTimerSelector",
    ]
    # Neo (STID 47): neo speed + timer
    assert sorted(by_device["AA:00:00:00:00:07"]) == [
        "DuuxNeoSpeedSelector",
        "DuuxTimerSelector",
    ]
    # Bright 2 (STID 61): its own restricted timer selector
    assert by_device["AA:00:00:00:00:10"] == ["DuuxBright2TimerSelector"]
    # Beam Mini (STID 35) and Edge Heater V2 (STID 50) both just get a plain timer
    assert by_device["AA:00:00:00:00:06"] == ["DuuxTimerSelector"]
    assert by_device["AA:00:00:00:00:01"] == ["DuuxTimerSelector"]
    # Whisper Flex Ultimate (STID 40): has its own "swing"/"tilt" data keys,
    # so it gets the newer swing/tilt selects (not the horosc/verosc ones).
    assert sorted(by_device["AA:00:00:00:00:11"]) == [
        "DuuxHorizontalSwingSelect",
        "DuuxVerticalTiltSelect",
    ]
