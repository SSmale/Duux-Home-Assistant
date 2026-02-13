import pytest
from unittest.mock import MagicMock

from custom_components.duux.__init__ import DuuxDataUpdateCoordinator
from custom_components.duux.switch import DuuxChildLockSwitch
from custom_components.duux.select import DuuxFanSpeedSelector
from custom_components.duux.sensor import DuuxTempSensor, DuuxSensorEntityDescription


@pytest.mark.asyncio
async def test_child_lock_switch_calls_api(hass):
    """Child lock switch should reflect coordinator data and call API for turn_on/turn_off."""

    class SimpleAPI:
        def __init__(self):
            self.set_lock = MagicMock(return_value=True)

    api = SimpleAPI()
    # coordinator uses api.get_device_status; we will bypass that and set .data directly
    coordinator = DuuxDataUpdateCoordinator(
        hass, api, device_id="AA:BB:CC", device_name="Test"
    )
    # seed coordinator data
    coordinator.data = {"lock": 1}

    device = {
        "id": 1,
        "deviceId": "AA:BB:CC",
        "displayName": "Device",
        "sensorType": {"name": "Mock"},
    }
    switch = DuuxChildLockSwitch(coordinator, api, device)

    # is_on should reflect coordinator.data
    assert switch.is_on is True

    await switch.async_turn_off()
    # API set_lock should be called with False
    api.set_lock.assert_called_with("AA:BB:CC", False)

    await switch.async_turn_on()
    api.set_lock.assert_called_with("AA:BB:CC", True)


@pytest.mark.asyncio
async def test_fan_speed_selector_calls_api_and_maps_options(hass):
    class SimpleAPI:
        def __init__(self):
            self.set_fan = MagicMock(return_value=True)

    api = SimpleAPI()
    coordinator = DuuxDataUpdateCoordinator(
        hass, api, device_id="AA:BB:CC", device_name="Test"
    )
    coordinator.data = {"fan": 1}  # 1 -> low according to mapping in selector

    device = {
        "id": 2,
        "deviceId": "AA:BB:CC",
        "displayName": "Device",
        "sensorType": {"name": "Mock"},
    }
    selector = DuuxFanSpeedSelector(coordinator, api, device)
    assert selector.current_option == "low"
    await selector.async_select_option("high")
    api.set_fan.assert_called()  # called with mapped value


def test_temp_sensor_reflects_coordinator_data(hass):
    class SimpleAPI:
        pass

    api = SimpleAPI()
    coordinator = DuuxDataUpdateCoordinator(
        hass, api, device_id="AA:BB:CC", device_name="Test"
    )
    coordinator.data = {"temp": 19.5}

    device = {
        "id": 3,
        "deviceId": "AA:BB:CC",
        "displayName": "Device",
        "sensorType": {"name": "Mock"},
    }
    desc = DuuxSensorEntityDescription(key="temp")
    sensor = DuuxTempSensor(coordinator, api, device)
    # the DuuxTempSensor inherits and sets _attr_native_value from coordinator in constructor
    assert sensor._attr_native_value == coordinator.data.get("temp")


# @pytest.mark.asyncio
# async def test_child_lock_switch_calls_api(hass):
#     """Child lock switch should reflect coordinator data and call API for turn_on/turn_off."""

#     class SimpleAPI:
#         def __init__(self):
#             self.set_lock = MagicMock(return_value=True)

#     api = SimpleAPI()
#     coordinator = DuuxDataUpdateCoordinator(
#         hass, api, device_id="AA:BB:CC", device_name="Test"
#     )
#     coordinator.data = {"lock": 1}

#     device = {
#         "id": 1,
#         "deviceId": "AA:BB:CC",
#         "displayName": "Device",
#         "sensorType": {"name": "Mock"},
#     }
#     switch = DuuxChildLockSwitch(coordinator, api, device)

#     # The entity's .hass is normally set when Home Assistant adds the entity.
#     # Set it here so async_turn_on/async_turn_off can use hass.async_add_executor_job.
#     switch.hass = hass

#     # is_on should reflect coordinator.data
#     assert switch.is_on is True

#     await switch.async_turn_off()
#     api.set_lock.assert_called_with("AA:BB:CC", False)

#     await switch.async_turn_on()
#     api.set_lock.assert_called_with("AA:BB:CC", True)


# @pytest.mark.asyncio
# async def test_fan_speed_selector_calls_api_and_maps_options(hass):
#     class SimpleAPI:
#         def __init__(self):
#             self.set_fan = MagicMock(return_value=True)

#     api = SimpleAPI()
#     coordinator = DuuxDataUpdateCoordinator(
#         hass, api, device_id="AA:BB:CC", device_name="Test"
#     )
#     coordinator.data = {"fan": 1}  # 1 -> low according to mapping in selector

#     device = {
#         "id": 2,
#         "deviceId": "AA:BB:CC",
#         "displayName": "Device",
#         "sensorType": {"name": "Mock"},
#     }
#     selector = DuuxFanSpeedSelector(coordinator, api, device)

#     # Set hass so the selector can use hass.async_add_executor_job in async_select_option
#     selector.hass = hass

#     assert selector.current_option == "low"
#     await selector.async_select_option("high")
#     api.set_fan.assert_called()  # called with mapped value


# def test_temp_sensor_reflects_coordinator_data(hass):
#     class SimpleAPI:
#         pass

#     api = SimpleAPI()
#     coordinator = DuuxDataUpdateCoordinator(
#         hass, api, device_id="AA:BB:CC", device_name="Test"
#     )
#     coordinator.data = {"temp": 19.5}

#     device = {
#         "id": 3,
#         "deviceId": "AA:BB:CC",
#         "displayName": "Device",
#         "sensorType": {"name": "Mock"},
#     }
#     sensor = DuuxTempSensor(coordinator, api, device)

#     # sensor entity may rely on hass for some ops; set it defensively
#     sensor.hass = hass

#     assert sensor._attr_native_value == coordinator.data.get("temp")
