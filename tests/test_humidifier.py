"""Unit tests for custom_components.duux.humidifier."""

from custom_components.duux import const
from custom_components.duux.humidifier import (
    DuuxBeamMiniDehumidifier,
    DuuxBoraDehumidifier,
    DuuxNeoHumidifier,
    async_setup_entry,
)
from homeassistant.components.humidifier.const import HumidifierAction


def attach_hass(entity, hass):
    entity.hass = hass
    return entity


# ---------------------------------------------------------------------------
# DuuxBoraDehumidifier
# ---------------------------------------------------------------------------


def test_bora_properties(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(62)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxBoraDehumidifier(coordinator, mock_api, device)

    assert entity.current_humidity == 52
    assert entity.target_humidity == 55
    assert entity.mode == entity.PRESET_AUTO  # mode == 0
    assert entity.available_modes == [entity.PRESET_AUTO, entity.PRESET_CONTINUOUS]
    assert entity.is_on is True
    assert entity.action == HumidifierAction.DRYING


async def test_bora_set_mode_continuous(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(62)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxBoraDehumidifier(coordinator, mock_api, device), make_hass()
    )

    await entity.async_set_mode(entity.PRESET_CONTINUOUS)

    mock_api.set_dry_mode.assert_called_once_with(device["deviceId"], "1")


async def test_bora_set_humidity(device_by_stid, make_coordinator, mock_api, make_hass):
    device = device_by_stid(62)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxBoraDehumidifier(coordinator, mock_api, device), make_hass()
    )

    await entity.async_set_humidity(60)

    mock_api.set_humidity.assert_called_once_with(device["deviceId"], 60)


async def test_bora_turn_off(device_by_stid, make_coordinator, mock_api, make_hass):
    device = device_by_stid(62)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxBoraDehumidifier(coordinator, mock_api, device), make_hass()
    )

    await entity.async_turn_off()

    mock_api.set_power.assert_called_once_with(device["deviceId"], False)
    assert entity.is_on is False
    assert coordinator.data["power"] == 0


async def test_bora_set_humidity_updates_coordinator_state(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(62)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxBoraDehumidifier(coordinator, mock_api, device), make_hass()
    )

    await entity.async_set_humidity(65)

    mock_api.set_humidity.assert_called_once_with(device["deviceId"], 65)
    assert coordinator.data["sp"] == 65


async def test_bora_set_mode_auto_sends_0(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    """PRESET_AUTO must map to mode string '0', not a mutated value."""
    device = device_by_stid(62)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxBoraDehumidifier(coordinator, mock_api, device), make_hass()
    )

    await entity.async_set_mode(entity.PRESET_AUTO)

    mock_api.set_dry_mode.assert_called_once_with(device["deviceId"], "0")


async def test_bora_set_mode_unknown_defaults_to_0(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    """Unknown mode must fall back to '0', not raise or send None."""
    device = device_by_stid(62)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxBoraDehumidifier(coordinator, mock_api, device), make_hass()
    )

    await entity.async_set_mode("not-a-real-mode")

    mock_api.set_dry_mode.assert_called_once_with(device["deviceId"], "0")


def test_bora_action_off_when_power_off(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(62)
    data = dict(device["latestData"]["fullData"])
    data["power"] = 0
    coordinator = make_coordinator(data)
    entity = DuuxBoraDehumidifier(coordinator, mock_api, device)

    assert entity.action == HumidifierAction.OFF


# ---------------------------------------------------------------------------
# DuuxBeamMiniDehumidifier
# ---------------------------------------------------------------------------


def test_beam_mini_properties(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(35)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxBeamMiniDehumidifier(coordinator, mock_api, device)

    assert entity.mode == entity.PRESET_MANUAL  # mode == 1
    assert entity.available_modes == [entity.PRESET_AUTO, entity.PRESET_MANUAL]
    assert entity._attr_min_humidity == 20
    assert entity._attr_max_humidity == 80


async def test_beam_mini_set_mode_auto(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    device = device_by_stid(35)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxBeamMiniDehumidifier(coordinator, mock_api, device), make_hass()
    )

    await entity.async_set_mode(entity.PRESET_AUTO)

    mock_api.set_dry_mode.assert_called_once_with(device["deviceId"], "0")


async def test_beam_mini_set_mode_manual_sends_1(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    """PRESET_MANUAL must map to mode string '1', not a mutated value."""
    device = device_by_stid(35)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(
        DuuxBeamMiniDehumidifier(coordinator, mock_api, device), make_hass()
    )

    await entity.async_set_mode(entity.PRESET_MANUAL)

    mock_api.set_dry_mode.assert_called_once_with(device["deviceId"], "1")


# ---------------------------------------------------------------------------
# DuuxNeoHumidifier -- mode comes back as a string from the API
# ---------------------------------------------------------------------------


def test_neo_mode_handles_string_value_from_api(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(47)
    coordinator = make_coordinator(device["latestData"]["fullData"])  # mode == "1"
    entity = DuuxNeoHumidifier(coordinator, mock_api, device)

    assert entity.mode == entity.PRESET_AUTO


def test_neo_mode_normal_when_not_one(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(47)
    data = dict(device["latestData"]["fullData"])
    data["mode"] = "0"
    coordinator = make_coordinator(data)
    entity = DuuxNeoHumidifier(coordinator, mock_api, device)

    assert entity.mode == entity.PRESET_NORMAL


async def test_neo_set_mode_sends_api_value_and_skips_sleep(
    device_by_stid, make_coordinator, mock_api, make_hass
):
    """Regression guard: async_set_mode must not block on asyncio.sleep(2)."""
    device = device_by_stid(47)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = attach_hass(DuuxNeoHumidifier(coordinator, mock_api, device), make_hass())

    await entity.async_set_mode(entity.PRESET_AUTO)

    mock_api.set_humidifier_mode.assert_called_once_with(device["deviceId"], "1")


def test_neo_action_humidifying_when_below_target(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(47)
    data = dict(device["latestData"]["fullData"])
    data["hum"] = 40
    data["sp"] = 60
    coordinator = make_coordinator(data)
    entity = DuuxNeoHumidifier(coordinator, mock_api, device)

    assert entity.action == HumidifierAction.HUMIDIFYING


def test_neo_action_idle_when_at_target(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(47)
    data = dict(device["latestData"]["fullData"])
    data["hum"] = 60
    data["sp"] = 60
    coordinator = make_coordinator(data)
    entity = DuuxNeoHumidifier(coordinator, mock_api, device)

    assert entity.action == HumidifierAction.IDLE


def test_neo_extra_state_attributes_spray_volume(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(47)
    coordinator = make_coordinator(device["latestData"]["fullData"])  # speed == 1
    entity = DuuxNeoHumidifier(coordinator, mock_api, device)

    assert entity.extra_state_attributes == {"spray_volume": "Mid"}


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

    assert classes_by_unique_id["duux_100005"] == "DuuxBoraDehumidifier"
    assert classes_by_unique_id["duux_100006"] == "DuuxBeamMiniDehumidifier"
    assert classes_by_unique_id["duux_100007"] == "DuuxNeoHumidifier"
    humidifier_device_ids = {"duux_100005", "duux_100006", "duux_100007"}
    assert set(classes_by_unique_id) == humidifier_device_ids
