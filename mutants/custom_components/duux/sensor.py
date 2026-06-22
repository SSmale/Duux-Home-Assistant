"""Support for Duux sensors."""

from __future__ import annotations
import logging

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import (
    EntityCategory,
    PERCENTAGE,
    UnitOfTemperature,
    UnitOfTime,
)
from homeassistant.core import callback
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    DOMAIN,
    DUUX_STID_BORA_2024,
    DUUX_STID_BRIGHT_2,
    ATTRIBUTION,
    DUUX_STID_BEAM_MINI,
    DUUX_ERRID,
)

_LOGGER = logging.getLogger(__name__)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class DuuxSensorEntityDescription(SensorEntityDescription):
    """Class describing Duux sensor entities."""

    attrs: Callable[[dict[str, Any]], dict[str, Any]] = lambda data: {}
mutants_x_async_setup_entry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_async_setup_entry__mutmut)
async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_orig(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_1(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = None
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_2(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = None
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_3(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["XXapiXX"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_4(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["API"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_5(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = None
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_6(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["XXcoordinatorsXX"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_7(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["COORDINATORS"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_8(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = None

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_9(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["XXdevicesXX"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_10(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["DEVICES"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_11(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = None
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_12(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = None
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_13(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get(None)
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_14(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("XXsensorTypeIdXX")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_15(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensortypeid")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_16(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("SENSORTYPEID")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_17(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = None
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_18(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["XXdeviceIdXX"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_19(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceid"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_20(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["DEVICEID"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_21(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = None

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_22(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(None)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_23(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is not None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_24(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            break

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_25(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id != DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_26(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(None)
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_27(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(None, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_28(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, None, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_29(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, None))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_30(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_31(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_32(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, ))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_33(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(None)
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_34(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(None, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_35(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, None, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_36(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, None))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_37(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_38(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_39(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, ))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_40(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id != DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_41(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(None)
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_42(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(None, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_43(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, None, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_44(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, None))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_45(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_46(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_47(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, ))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_48(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(None)
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_49(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(None, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_50(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, None, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_51(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, None))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_52(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_53(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_54(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, ))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_55(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(None)
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_56(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(None, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_57(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, None, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_58(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, None))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_59(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_60(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_61(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, ))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_62(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(None)
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_63(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(None, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_64(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, None, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_65(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, None))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_66(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_67(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_68(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, ))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_69(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(None)
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_70(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(None, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_71(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, None, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_72(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, None))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_73(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_74(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_75(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, ))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_76(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id != DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_77(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(None)
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_78(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(None, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_79(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, None, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_80(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, None))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_81(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_82(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_83(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, ))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_84(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(None)
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_85(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(None, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_86(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, None, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_87(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, None))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_88(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_89(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_90(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, ))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_91(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get(None) is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_92(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("XXtempXX") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_93(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("TEMP") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_94(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_95(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(None)

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_96(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(None, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_97(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, None, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_98(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, None))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_99(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_100(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_101(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, ))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_102(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(None)
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_103(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(None, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_104(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, None, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_105(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, None))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_106(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_107(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_108(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, ))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_109(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(None)

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_110(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(None, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_111(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, None, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_112(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, None))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_113(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_114(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_115(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, ))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_116(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

    async_add_entities(None)

mutants_x_async_setup_entry__mutmut['_mutmut_orig'] = x_async_setup_entry__mutmut_orig # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_1'] = x_async_setup_entry__mutmut_1 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_2'] = x_async_setup_entry__mutmut_2 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_3'] = x_async_setup_entry__mutmut_3 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_4'] = x_async_setup_entry__mutmut_4 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_5'] = x_async_setup_entry__mutmut_5 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_6'] = x_async_setup_entry__mutmut_6 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_7'] = x_async_setup_entry__mutmut_7 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_8'] = x_async_setup_entry__mutmut_8 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_9'] = x_async_setup_entry__mutmut_9 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_10'] = x_async_setup_entry__mutmut_10 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_11'] = x_async_setup_entry__mutmut_11 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_12'] = x_async_setup_entry__mutmut_12 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_13'] = x_async_setup_entry__mutmut_13 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_14'] = x_async_setup_entry__mutmut_14 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_15'] = x_async_setup_entry__mutmut_15 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_16'] = x_async_setup_entry__mutmut_16 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_17'] = x_async_setup_entry__mutmut_17 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_18'] = x_async_setup_entry__mutmut_18 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_19'] = x_async_setup_entry__mutmut_19 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_20'] = x_async_setup_entry__mutmut_20 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_21'] = x_async_setup_entry__mutmut_21 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_22'] = x_async_setup_entry__mutmut_22 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_23'] = x_async_setup_entry__mutmut_23 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_24'] = x_async_setup_entry__mutmut_24 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_25'] = x_async_setup_entry__mutmut_25 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_26'] = x_async_setup_entry__mutmut_26 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_27'] = x_async_setup_entry__mutmut_27 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_28'] = x_async_setup_entry__mutmut_28 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_29'] = x_async_setup_entry__mutmut_29 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_30'] = x_async_setup_entry__mutmut_30 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_31'] = x_async_setup_entry__mutmut_31 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_32'] = x_async_setup_entry__mutmut_32 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_33'] = x_async_setup_entry__mutmut_33 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_34'] = x_async_setup_entry__mutmut_34 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_35'] = x_async_setup_entry__mutmut_35 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_36'] = x_async_setup_entry__mutmut_36 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_37'] = x_async_setup_entry__mutmut_37 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_38'] = x_async_setup_entry__mutmut_38 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_39'] = x_async_setup_entry__mutmut_39 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_40'] = x_async_setup_entry__mutmut_40 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_41'] = x_async_setup_entry__mutmut_41 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_42'] = x_async_setup_entry__mutmut_42 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_43'] = x_async_setup_entry__mutmut_43 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_44'] = x_async_setup_entry__mutmut_44 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_45'] = x_async_setup_entry__mutmut_45 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_46'] = x_async_setup_entry__mutmut_46 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_47'] = x_async_setup_entry__mutmut_47 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_48'] = x_async_setup_entry__mutmut_48 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_49'] = x_async_setup_entry__mutmut_49 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_50'] = x_async_setup_entry__mutmut_50 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_51'] = x_async_setup_entry__mutmut_51 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_52'] = x_async_setup_entry__mutmut_52 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_53'] = x_async_setup_entry__mutmut_53 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_54'] = x_async_setup_entry__mutmut_54 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_55'] = x_async_setup_entry__mutmut_55 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_56'] = x_async_setup_entry__mutmut_56 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_57'] = x_async_setup_entry__mutmut_57 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_58'] = x_async_setup_entry__mutmut_58 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_59'] = x_async_setup_entry__mutmut_59 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_60'] = x_async_setup_entry__mutmut_60 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_61'] = x_async_setup_entry__mutmut_61 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_62'] = x_async_setup_entry__mutmut_62 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_63'] = x_async_setup_entry__mutmut_63 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_64'] = x_async_setup_entry__mutmut_64 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_65'] = x_async_setup_entry__mutmut_65 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_66'] = x_async_setup_entry__mutmut_66 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_67'] = x_async_setup_entry__mutmut_67 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_68'] = x_async_setup_entry__mutmut_68 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_69'] = x_async_setup_entry__mutmut_69 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_70'] = x_async_setup_entry__mutmut_70 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_71'] = x_async_setup_entry__mutmut_71 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_72'] = x_async_setup_entry__mutmut_72 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_73'] = x_async_setup_entry__mutmut_73 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_74'] = x_async_setup_entry__mutmut_74 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_75'] = x_async_setup_entry__mutmut_75 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_76'] = x_async_setup_entry__mutmut_76 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_77'] = x_async_setup_entry__mutmut_77 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_78'] = x_async_setup_entry__mutmut_78 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_79'] = x_async_setup_entry__mutmut_79 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_80'] = x_async_setup_entry__mutmut_80 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_81'] = x_async_setup_entry__mutmut_81 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_82'] = x_async_setup_entry__mutmut_82 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_83'] = x_async_setup_entry__mutmut_83 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_84'] = x_async_setup_entry__mutmut_84 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_85'] = x_async_setup_entry__mutmut_85 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_86'] = x_async_setup_entry__mutmut_86 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_87'] = x_async_setup_entry__mutmut_87 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_88'] = x_async_setup_entry__mutmut_88 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_89'] = x_async_setup_entry__mutmut_89 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_90'] = x_async_setup_entry__mutmut_90 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_91'] = x_async_setup_entry__mutmut_91 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_92'] = x_async_setup_entry__mutmut_92 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_93'] = x_async_setup_entry__mutmut_93 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_94'] = x_async_setup_entry__mutmut_94 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_95'] = x_async_setup_entry__mutmut_95 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_96'] = x_async_setup_entry__mutmut_96 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_97'] = x_async_setup_entry__mutmut_97 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_98'] = x_async_setup_entry__mutmut_98 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_99'] = x_async_setup_entry__mutmut_99 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_100'] = x_async_setup_entry__mutmut_100 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_101'] = x_async_setup_entry__mutmut_101 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_102'] = x_async_setup_entry__mutmut_102 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_103'] = x_async_setup_entry__mutmut_103 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_104'] = x_async_setup_entry__mutmut_104 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_105'] = x_async_setup_entry__mutmut_105 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_106'] = x_async_setup_entry__mutmut_106 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_107'] = x_async_setup_entry__mutmut_107 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_108'] = x_async_setup_entry__mutmut_108 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_109'] = x_async_setup_entry__mutmut_109 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_110'] = x_async_setup_entry__mutmut_110 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_111'] = x_async_setup_entry__mutmut_111 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_112'] = x_async_setup_entry__mutmut_112 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_113'] = x_async_setup_entry__mutmut_113 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_114'] = x_async_setup_entry__mutmut_114 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_115'] = x_async_setup_entry__mutmut_115 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_116'] = x_async_setup_entry__mutmut_116 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxSensor(CoordinatorEntity, SensorEntity):
    """Define an Duux sensor."""

    _attr_attribution = ATTRIBUTION
    entity_description: DuuxSensorEntityDescription

    @_mutmut_mutated(mutants_xǁDuuxSensorǁ__init____mutmut)
    def __init__(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_orig(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_1(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(None)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_2(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = None
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_3(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = None
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_4(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = None
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_5(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = None
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_6(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["XXidXX"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_7(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["ID"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_8(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = None  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_9(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["XXdeviceIdXX"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_10(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceid"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_11(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["DEVICEID"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_12(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = None
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_13(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = None
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_14(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") and device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_15(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get(None) or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_16(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("XXdisplayNameXX") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_17(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayname") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_18(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("DISPLAYNAME") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_19(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get(None)
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_20(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("XXnameXX")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_21(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("NAME")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_22(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = None

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_23(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = False

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_24(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = None
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_25(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers=None,
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_26(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=None,
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_27(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=None,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_28(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_29(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_30(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_31(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(None))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_32(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get(None, "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_33(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", None),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_34(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_35(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", ),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_36(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("XXmanufacturerXX", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_37(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("MANUFACTURER", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_38(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "XXDuuxXX"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_39(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_40(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "DUUX"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_41(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = None
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_42(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data and {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_43(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = None
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_44(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(None)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_45(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = None
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_46(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(None)
        self.entity_description = description

    def xǁDuuxSensorǁ__init____mutmut_47(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = None

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.last_update_success and (
            self.coordinator.data or {}
        ).get("online", True)

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        data = self.coordinator.data or {}
        self._attr_native_value = data.get(self.entity_description.key)
        self._attr_extra_state_attributes = self.entity_description.attrs(data)
        self.async_write_ha_state()

mutants_xǁDuuxSensorǁ__init____mutmut['_mutmut_orig'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_1'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_2'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_3'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_4'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_5'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_6'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_7'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_8'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_9'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_10'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_11'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_12'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_13'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_14'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_15'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_16'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_17'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_18'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_19'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_20'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_21'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_22'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_23'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_24'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_25'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_26'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_27'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_27 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_28'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_28 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_29'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_29 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_30'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_30 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_31'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_31 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_32'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_32 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_33'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_33 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_34'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_34 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_35'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_35 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_36'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_36 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_37'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_37 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_38'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_38 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_39'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_39 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_40'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_40 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_41'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_41 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_42'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_42 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_43'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_43 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_44'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_44 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_45'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_45 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_46'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_46 # type: ignore # mutmut generated
mutants_xǁDuuxSensorǁ__init____mutmut['xǁDuuxSensorǁ__init____mutmut_47'] = DuuxSensor.xǁDuuxSensorǁ__init____mutmut_47 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxTempSensor(DuuxSensor):
    @_mutmut_mutated(mutants_xǁDuuxTempSensorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_orig(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_1(self, coordinator, api, device):
        super().__init__(
            None,
            api,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_2(self, coordinator, api, device):
        super().__init__(
            coordinator,
            None,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_3(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            None,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_4(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            None,
        )
    def xǁDuuxTempSensorǁ__init____mutmut_5(self, coordinator, api, device):
        super().__init__(
            api,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_6(self, coordinator, api, device):
        super().__init__(
            coordinator,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_7(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_8(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            )
    def xǁDuuxTempSensorǁ__init____mutmut_9(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=None,
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_10(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=None,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_11(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=None,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_12(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=None,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_13(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=None,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_14(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_15(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_16(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_17(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_18(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_19(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="XXtempXX",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_20(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="TEMP",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxTempSensorǁ__init____mutmut_21(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=2,
            ),
        )

mutants_xǁDuuxTempSensorǁ__init____mutmut['_mutmut_orig'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_1'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_2'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_3'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_4'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_5'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_6'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_7'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_8'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_9'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_10'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_11'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_12'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_13'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_14'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_15'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_16'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_17'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_18'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_19'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_20'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxTempSensorǁ__init____mutmut['xǁDuuxTempSensorǁ__init____mutmut_21'] = DuuxTempSensor.xǁDuuxTempSensorǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxPM25Sensor(DuuxSensor):
    @_mutmut_mutated(mutants_xǁDuuxPM25Sensorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_orig(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_1(self, coordinator, api, device):
        super().__init__(
            None,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_2(self, coordinator, api, device):
        super().__init__(
            coordinator,
            None,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_3(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            None,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_4(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            None,
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_5(self, coordinator, api, device):
        super().__init__(
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_6(self, coordinator, api, device):
        super().__init__(
            coordinator,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_7(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_8(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            )
    def xǁDuuxPM25Sensorǁ__init____mutmut_9(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=None,
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_10(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key=None,
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_11(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=None,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_12(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement=None,
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_13(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=None,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_14(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_15(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_16(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_17(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_18(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_19(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="XXppmXX",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_20(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="PPM",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_21(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="XXpm25XX",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_22(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="PM25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_23(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="XXµg/m³XX",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )
    def xǁDuuxPM25Sensorǁ__init____mutmut_24(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="ΜG/M³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )

mutants_xǁDuuxPM25Sensorǁ__init____mutmut['_mutmut_orig'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_1'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_2'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_3'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_4'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_5'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_6'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_7'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_8'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_9'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_10'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_11'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_12'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_13'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_14'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_15'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_16'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_17'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_18'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_19'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_20'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_21'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_22'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_23'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxPM25Sensorǁ__init____mutmut['xǁDuuxPM25Sensorǁ__init____mutmut_24'] = DuuxPM25Sensor.xǁDuuxPM25Sensorǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxTVOCSensor(DuuxSensor):
    @_mutmut_mutated(mutants_xǁDuuxTVOCSensorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="tvoc",
                translation_key="tvoc",
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_orig(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="tvoc",
                translation_key="tvoc",
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_1(self, coordinator, api, device):
        super().__init__(
            None,
            api,
            device,
            DuuxSensorEntityDescription(
                key="tvoc",
                translation_key="tvoc",
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_2(self, coordinator, api, device):
        super().__init__(
            coordinator,
            None,
            device,
            DuuxSensorEntityDescription(
                key="tvoc",
                translation_key="tvoc",
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_3(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            None,
            DuuxSensorEntityDescription(
                key="tvoc",
                translation_key="tvoc",
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_4(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            None,
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_5(self, coordinator, api, device):
        super().__init__(
            api,
            device,
            DuuxSensorEntityDescription(
                key="tvoc",
                translation_key="tvoc",
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_6(self, coordinator, api, device):
        super().__init__(
            coordinator,
            device,
            DuuxSensorEntityDescription(
                key="tvoc",
                translation_key="tvoc",
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_7(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            DuuxSensorEntityDescription(
                key="tvoc",
                translation_key="tvoc",
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_8(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            )
    def xǁDuuxTVOCSensorǁ__init____mutmut_9(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=None,
                translation_key="tvoc",
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_10(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="tvoc",
                translation_key=None,
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_11(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                translation_key="tvoc",
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_12(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="tvoc",
                ),
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_13(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="XXtvocXX",
                translation_key="tvoc",
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_14(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="TVOC",
                translation_key="tvoc",
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_15(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="tvoc",
                translation_key="XXtvocXX",
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )
    def xǁDuuxTVOCSensorǁ__init____mutmut_16(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="tvoc",
                translation_key="TVOC",
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )

    _TVOC_MAP = {
        0: "healthy",
        1: "acceptable",
        2: "polluted",
        3: "harmful",
    }

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        data = self.coordinator.data or {}
        raw = data.get("tvoc")
        self._attr_native_value = (
            self._TVOC_MAP.get(raw, raw) if raw is not None else None
        )
        self._attr_extra_state_attributes = self.entity_description.attrs(data)
        self.async_write_ha_state()

mutants_xǁDuuxTVOCSensorǁ__init____mutmut['_mutmut_orig'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_1'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_2'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_3'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_4'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_5'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_6'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_7'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_8'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_9'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_10'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_11'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_12'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_13'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_14'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_15'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxTVOCSensorǁ__init____mutmut['xǁDuuxTVOCSensorǁ__init____mutmut_16'] = DuuxTVOCSensor.xǁDuuxTVOCSensorǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxFilterLifeSensor(DuuxSensor):
    @_mutmut_mutated(mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_orig(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_1(self, coordinator, api, device):
        super().__init__(
            None,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_2(self, coordinator, api, device):
        super().__init__(
            coordinator,
            None,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_3(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            None,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_4(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            None,
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_5(self, coordinator, api, device):
        super().__init__(
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_6(self, coordinator, api, device):
        super().__init__(
            coordinator,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_7(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_8(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_9(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=None,
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_10(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key=None,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_11(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=None,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_12(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=None,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_13(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon=None,
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_14(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_15(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_16(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_17(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_18(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_19(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="XXfilterXX",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_20(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="FILTER",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_21(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="XXfilter_lifeXX",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_22(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="FILTER_LIFE",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_23(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="XXmdi:air-filterXX",
            ),
        )
    def xǁDuuxFilterLifeSensorǁ__init____mutmut_24(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="MDI:AIR-FILTER",
            ),
        )

mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['_mutmut_orig'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_1'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_2'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_3'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_4'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_5'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_6'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_7'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_8'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_9'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_10'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_11'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_12'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_13'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_14'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_15'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_16'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_17'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_18'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_19'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_20'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_21'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_22'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_23'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxFilterLifeSensorǁ__init____mutmut['xǁDuuxFilterLifeSensorǁ__init____mutmut_24'] = DuuxFilterLifeSensor.xǁDuuxFilterLifeSensorǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxAirQualitySensor(DuuxSensor):
    @_mutmut_mutated(mutants_xǁDuuxAirQualitySensorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="aq",
                translation_key="air_quality_index",
            ),
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_orig(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="aq",
                translation_key="air_quality_index",
            ),
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_1(self, coordinator, api, device):
        super().__init__(
            None,
            api,
            device,
            DuuxSensorEntityDescription(
                key="aq",
                translation_key="air_quality_index",
            ),
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_2(self, coordinator, api, device):
        super().__init__(
            coordinator,
            None,
            device,
            DuuxSensorEntityDescription(
                key="aq",
                translation_key="air_quality_index",
            ),
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_3(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            None,
            DuuxSensorEntityDescription(
                key="aq",
                translation_key="air_quality_index",
            ),
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_4(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            None,
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_5(self, coordinator, api, device):
        super().__init__(
            api,
            device,
            DuuxSensorEntityDescription(
                key="aq",
                translation_key="air_quality_index",
            ),
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_6(self, coordinator, api, device):
        super().__init__(
            coordinator,
            device,
            DuuxSensorEntityDescription(
                key="aq",
                translation_key="air_quality_index",
            ),
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_7(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            DuuxSensorEntityDescription(
                key="aq",
                translation_key="air_quality_index",
            ),
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_8(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_9(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=None,
                translation_key="air_quality_index",
            ),
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_10(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="aq",
                translation_key=None,
            ),
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_11(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                translation_key="air_quality_index",
            ),
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_12(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="aq",
                ),
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_13(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="XXaqXX",
                translation_key="air_quality_index",
            ),
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_14(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="AQ",
                translation_key="air_quality_index",
            ),
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_15(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="aq",
                translation_key="XXair_quality_indexXX",
            ),
        )
    def xǁDuuxAirQualitySensorǁ__init____mutmut_16(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="aq",
                translation_key="AIR_QUALITY_INDEX",
            ),
        )

    _AQ_MAP = {
        0: "excellent",
        1: "very_good",
        2: "good",
        3: "fair",
        4: "poor",
        5: "harmful",
    }

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        data = self.coordinator.data or {}
        raw = data.get("aq")
        # Map integer API value to translation key; fall back to raw value if unknown
        self._attr_native_value = (
            self._AQ_MAP.get(raw, raw) if raw is not None else None
        )
        self._attr_extra_state_attributes = self.entity_description.attrs(data)
        self.async_write_ha_state()

mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['_mutmut_orig'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_1'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_2'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_3'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_4'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_5'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_6'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_7'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_8'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_9'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_10'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_11'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_12'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_13'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_14'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_15'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxAirQualitySensorǁ__init____mutmut['xǁDuuxAirQualitySensorǁ__init____mutmut_16'] = DuuxAirQualitySensor.xǁDuuxAirQualitySensorǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxHumiditySensor(DuuxSensor):
    @_mutmut_mutated(mutants_xǁDuuxHumiditySensorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_orig(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_1(self, coordinator, api, device):
        super().__init__(
            None,
            api,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_2(self, coordinator, api, device):
        super().__init__(
            coordinator,
            None,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_3(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            None,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_4(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            None,
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_5(self, coordinator, api, device):
        super().__init__(
            api,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_6(self, coordinator, api, device):
        super().__init__(
            coordinator,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_7(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_8(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            )
    def xǁDuuxHumiditySensorǁ__init____mutmut_9(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=None,
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_10(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=None,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_11(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=None,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_12(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=None,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_13(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=None,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_14(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_15(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_16(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_17(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_18(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_19(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="XXhumXX",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_20(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="HUM",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )
    def xǁDuuxHumiditySensorǁ__init____mutmut_21(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=2,
            ),
        )

mutants_xǁDuuxHumiditySensorǁ__init____mutmut['_mutmut_orig'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_1'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_2'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_3'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_4'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_5'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_6'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_7'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_8'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_9'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_10'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_11'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_12'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_13'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_14'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_15'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_16'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_17'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_18'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_19'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_20'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxHumiditySensorǁ__init____mutmut['xǁDuuxHumiditySensorǁ__init____mutmut_21'] = DuuxHumiditySensor.xǁDuuxHumiditySensorǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxTimeRemainingSensor(DuuxSensor):
    """Base time remaining sensor — subclass per device to set the correct API key."""

    @_mutmut_mutated(mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut)
    def __init__(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_orig(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_1(self, coordinator, api, device, key: str):
        super().__init__(
            None,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_2(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            None,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_3(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            None,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_4(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            None,
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_5(self, coordinator, api, device, key: str):
        super().__init__(
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_6(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_7(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_8(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_9(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=None,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_10(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key=None,
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_11(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=None,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_12(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=None,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_13(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=None,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_14(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=None,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_15(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_16(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_17(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_18(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_19(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_20(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_21(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="XXtime_remainingXX",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_22(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="TIME_REMAINING",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )

    def xǁDuuxTimeRemainingSensorǁ__init____mutmut_23(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=2,
            ),
        )

mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['_mutmut_orig'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_1'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_2'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_3'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_4'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_5'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_6'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_7'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_8'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_9'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_10'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_11'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_12'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_13'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_14'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_15'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_16'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_17'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_18'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_19'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_20'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_21'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_22'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxTimeRemainingSensorǁ__init____mutmut['xǁDuuxTimeRemainingSensorǁ__init____mutmut_23'] = DuuxTimeRemainingSensor.xǁDuuxTimeRemainingSensorǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxErrorSensor(DuuxSensor):
    @_mutmut_mutated(mutants_xǁDuuxErrorSensorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="err",
                translation_key="error_message",
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_orig(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="err",
                translation_key="error_message",
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_1(self, coordinator, api, device):
        super().__init__(
            None,
            api,
            device,
            DuuxSensorEntityDescription(
                key="err",
                translation_key="error_message",
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_2(self, coordinator, api, device):
        super().__init__(
            coordinator,
            None,
            device,
            DuuxSensorEntityDescription(
                key="err",
                translation_key="error_message",
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_3(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            None,
            DuuxSensorEntityDescription(
                key="err",
                translation_key="error_message",
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_4(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            None,
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_5(self, coordinator, api, device):
        super().__init__(
            api,
            device,
            DuuxSensorEntityDescription(
                key="err",
                translation_key="error_message",
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_6(self, coordinator, api, device):
        super().__init__(
            coordinator,
            device,
            DuuxSensorEntityDescription(
                key="err",
                translation_key="error_message",
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_7(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            DuuxSensorEntityDescription(
                key="err",
                translation_key="error_message",
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_8(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_9(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=None,
                translation_key="error_message",
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_10(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="err",
                translation_key=None,
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_11(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                translation_key="error_message",
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_12(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="err",
                ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_13(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="XXerrXX",
                translation_key="error_message",
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_14(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ERR",
                translation_key="error_message",
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_15(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="err",
                translation_key="XXerror_messageXX",
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_16(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="err",
                translation_key="ERROR_MESSAGE",
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"
    def xǁDuuxErrorSensorǁ__init____mutmut_17(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="err",
                translation_key="error_message",
            ),
        )
        self._attr_icon = None
    def xǁDuuxErrorSensorǁ__init____mutmut_18(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="err",
                translation_key="error_message",
            ),
        )
        self._attr_icon = "XXmdi:comment-alert-outlineXX"
    def xǁDuuxErrorSensorǁ__init____mutmut_19(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="err",
                translation_key="error_message",
            ),
        )
        self._attr_icon = "MDI:COMMENT-ALERT-OUTLINE"

    @property
    def native_value(self):
        data = self.coordinator.data or {}
        key = self.entity_description.key
        errid = DUUX_ERRID(data[key]) if key in data else DUUX_ERRID.Unavailable
        return errid.name.replace("_", " ")

mutants_xǁDuuxErrorSensorǁ__init____mutmut['_mutmut_orig'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_1'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_2'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_3'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_4'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_5'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_6'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_7'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_8'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_9'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_10'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_11'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_12'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_13'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_14'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_15'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_16'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_17'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_18'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_19'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxConnectionTypeSensor(DuuxSensor):
    """Enum sensor reporting whether the device is connected via MQTT or TCP.

    'connectionType' lives on the device envelope returned by /smarthome/sensors
    rather than in the polled status payload, but DuuxAPI.get_device_status()
    stitches it into the coordinator data (the same way it already does for
    'online'), so this updates on every coordinator refresh rather than being
    frozen at integration setup.
    """

    @_mutmut_mutated(mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_orig(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_1(self, coordinator, api, device):
        super().__init__(
            None,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_2(self, coordinator, api, device):
        super().__init__(
            coordinator,
            None,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_3(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            None,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_4(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            None,
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_5(self, coordinator, api, device):
        super().__init__(
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_6(self, coordinator, api, device):
        super().__init__(
            coordinator,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_7(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_8(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_9(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=None,
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_10(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key=None,
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_11(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=None,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_12(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=None,
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_13(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=None,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_14(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon=None,
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_15(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_16(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_17(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_18(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_19(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_20(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_21(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="XXconnectionTypeXX",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_22(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectiontype",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_23(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="CONNECTIONTYPE",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_24(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="XXconnection_typeXX",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_25(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="CONNECTION_TYPE",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_26(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["XXmqttXX", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_27(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["MQTT", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_28(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "XXtcpXX"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_29(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "TCP"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_30(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="XXmdi:wanXX",
            ),
        )

    def xǁDuuxConnectionTypeSensorǁ__init____mutmut_31(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="MDI:WAN",
            ),
        )

    @property
    def native_value(self):
        """Return the connection type, normalised to match the declared options."""
        value = (self.coordinator.data or {}).get(self.entity_description.key)
        return value.lower() if isinstance(value, str) else None

mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['_mutmut_orig'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_1'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_2'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_3'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_4'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_5'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_6'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_7'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_8'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_9'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_10'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_11'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_12'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_13'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_14'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_15'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_16'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_17'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_18'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_19'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_20'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_21'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_22'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_23'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_24'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_25'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_26'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_27'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_27 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_28'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_28 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_29'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_29 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_30'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_30 # type: ignore # mutmut generated
mutants_xǁDuuxConnectionTypeSensorǁ__init____mutmut['xǁDuuxConnectionTypeSensorǁ__init____mutmut_31'] = DuuxConnectionTypeSensor.xǁDuuxConnectionTypeSensorǁ__init____mutmut_31 # type: ignore # mutmut generated
mutants_xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxBora2024TimeRemainingSensor(DuuxTimeRemainingSensor):
    """Time remaining sensor for Duux Bora 2024 (API key: 'timrm')."""

    @_mutmut_mutated(mutants_xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        super().__init__(coordinator, api, device, key="timrm")

    def xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_orig(self, coordinator, api, device):
        super().__init__(coordinator, api, device, key="timrm")

    def xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_1(self, coordinator, api, device):
        super().__init__(None, api, device, key="timrm")

    def xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_2(self, coordinator, api, device):
        super().__init__(coordinator, None, device, key="timrm")

    def xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_3(self, coordinator, api, device):
        super().__init__(coordinator, api, None, key="timrm")

    def xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_4(self, coordinator, api, device):
        super().__init__(coordinator, api, device, key=None)

    def xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_5(self, coordinator, api, device):
        super().__init__(api, device, key="timrm")

    def xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_6(self, coordinator, api, device):
        super().__init__(coordinator, device, key="timrm")

    def xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_7(self, coordinator, api, device):
        super().__init__(coordinator, api, key="timrm")

    def xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_8(self, coordinator, api, device):
        super().__init__(coordinator, api, device, )

    def xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_9(self, coordinator, api, device):
        super().__init__(coordinator, api, device, key="XXtimrmXX")

    def xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_10(self, coordinator, api, device):
        super().__init__(coordinator, api, device, key="TIMRM")

mutants_xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut['_mutmut_orig'] = DuuxBora2024TimeRemainingSensor.xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut['xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_1'] = DuuxBora2024TimeRemainingSensor.xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut['xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_2'] = DuuxBora2024TimeRemainingSensor.xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut['xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_3'] = DuuxBora2024TimeRemainingSensor.xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut['xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_4'] = DuuxBora2024TimeRemainingSensor.xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut['xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_5'] = DuuxBora2024TimeRemainingSensor.xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut['xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_6'] = DuuxBora2024TimeRemainingSensor.xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut['xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_7'] = DuuxBora2024TimeRemainingSensor.xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut['xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_8'] = DuuxBora2024TimeRemainingSensor.xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut['xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_9'] = DuuxBora2024TimeRemainingSensor.xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut['xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_10'] = DuuxBora2024TimeRemainingSensor.xǁDuuxBora2024TimeRemainingSensorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxBright2TimeRemainingSensor(DuuxTimeRemainingSensor):
    """Time remaining sensor for Duux Bright 2 (API key: 'timerr')."""

    @_mutmut_mutated(mutants_xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        super().__init__(coordinator, api, device, key="timerr")

    def xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_orig(self, coordinator, api, device):
        super().__init__(coordinator, api, device, key="timerr")

    def xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_1(self, coordinator, api, device):
        super().__init__(None, api, device, key="timerr")

    def xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_2(self, coordinator, api, device):
        super().__init__(coordinator, None, device, key="timerr")

    def xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_3(self, coordinator, api, device):
        super().__init__(coordinator, api, None, key="timerr")

    def xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_4(self, coordinator, api, device):
        super().__init__(coordinator, api, device, key=None)

    def xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_5(self, coordinator, api, device):
        super().__init__(api, device, key="timerr")

    def xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_6(self, coordinator, api, device):
        super().__init__(coordinator, device, key="timerr")

    def xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_7(self, coordinator, api, device):
        super().__init__(coordinator, api, key="timerr")

    def xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_8(self, coordinator, api, device):
        super().__init__(coordinator, api, device, )

    def xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_9(self, coordinator, api, device):
        super().__init__(coordinator, api, device, key="XXtimerrXX")

    def xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_10(self, coordinator, api, device):
        super().__init__(coordinator, api, device, key="TIMERR")

mutants_xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut['_mutmut_orig'] = DuuxBright2TimeRemainingSensor.xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut['xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_1'] = DuuxBright2TimeRemainingSensor.xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut['xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_2'] = DuuxBright2TimeRemainingSensor.xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut['xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_3'] = DuuxBright2TimeRemainingSensor.xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut['xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_4'] = DuuxBright2TimeRemainingSensor.xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut['xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_5'] = DuuxBright2TimeRemainingSensor.xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut['xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_6'] = DuuxBright2TimeRemainingSensor.xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut['xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_7'] = DuuxBright2TimeRemainingSensor.xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut['xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_8'] = DuuxBright2TimeRemainingSensor.xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut['xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_9'] = DuuxBright2TimeRemainingSensor.xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut['xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_10'] = DuuxBright2TimeRemainingSensor.xǁDuuxBright2TimeRemainingSensorǁ__init____mutmut_10 # type: ignore # mutmut generated
