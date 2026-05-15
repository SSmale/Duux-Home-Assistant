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
    PERCENTAGE,
    UnitOfTemperature,
    UnitOfTime,
)
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import *

_LOGGER = logging.getLogger(__name__)

@dataclass(frozen=True)
class DuuxSensorEntityDescription(SensorEntityDescription):
    """Class describing Duux sensor entities."""

    attrs: Callable[[dict[str, Any]], dict[str, Any]] = lambda data: {}

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
        coordinator = coordinators[device_id]
        
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxTimeRemainingSensor(coordinator, api, device))
        else:
            entities.append(DuuxTempSensor(coordinator, api, device))
    
    async_add_entities(entities)

class DuuxSensor(CoordinatorEntity, SensorEntity):
    """Define an Duux sensor."""

    _attr_attribution = ATTRIBUTION
    entity_description: DuuxSensorEntityDescription

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
        self._attr_native_value = coordinator.data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return (
            self.coordinator.last_update_success
            and (self.coordinator.data or {}).get("online", True)
        )

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        data = self.coordinator.data or {}
        self._attr_native_value = data.get(self.entity_description.key)
        self._attr_extra_state_attributes = self.entity_description.attrs(data)
        self.async_write_ha_state()

class DuuxTempSensor(DuuxSensor):
    def __init__(self, coordinator, api, device):
        super().__init__(coordinator, api, device, 
            DuuxSensorEntityDescription(
                key='temp',
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ))

class DuuxPM25Sensor(DuuxSensor):
    def __init__(self, coordinator, api, device):
        super().__init__(coordinator, api, device, 
            DuuxSensorEntityDescription(
                key='ppm',
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ))

class DuuxTVOCSensor(DuuxSensor):
    def __init__(self, coordinator, api, device):
        super().__init__(coordinator, api, device, 
            DuuxSensorEntityDescription(
                key='tvoc',
                translation_key="tvoc",
                device_class=SensorDeviceClass.VOLATILE_ORGANIC_COMPOUNDS,
                state_class=SensorStateClass.MEASUREMENT,
            ))

class DuuxFilterLifeSensor(DuuxSensor):
    def __init__(self, coordinator, api, device):
        super().__init__(coordinator, api, device, 
            DuuxSensorEntityDescription(
                key='filter',
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ))

class DuuxAirQualitySensor(DuuxSensor):
    def __init__(self, coordinator, api, device):
        super().__init__(coordinator, api, device, 
            DuuxSensorEntityDescription(
                key='aq',
                translation_key="air_quality_index",
            ))

    @property
    def native_value(self) -> str | int | None:
        """Return the state of the sensor."""
        value = (self.coordinator.data or {}).get("aq")
        if value is None:
            return None
        
        # Mapping: 0=Excellent, 1=Very Good, 2=Good, 3=Fair, 4=Poor, 5=Harmful
        mapping = {
            0: "excellent",
            1: "very_good",
            2: "good",
            3: "fair",
            4: "poor",
            5: "harmful"
        }
        return mapping.get(value, value)

class DuuxHumiditySensor(DuuxSensor):
    def __init__(self, coordinator, api, device):
        super().__init__(coordinator, api, device, 
            DuuxSensorEntityDescription(
                key='hum',
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ))

class DuuxTimeRemainingSensor(DuuxSensor):
    def __init__(self, coordinator, api, device):
        super().__init__(coordinator, api, device, 
            DuuxSensorEntityDescription(
                key='timerr',
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=0,
            ))