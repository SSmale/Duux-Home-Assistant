"""Support for Duux selectors."""
import logging

from homeassistant.components.select import SelectEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import *

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators[device_id]
        
        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
    
    async_add_entities(entities)


class DuuxSelector(CoordinatorEntity, SelectEntity):
    """Base class for Duux selectors."""

    def __init__(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    @property
    def device_info(self):
        """Return device information."""
        return {
            "identifiers": {(DOMAIN, str(self._device_id))},
            "name": self.device_name,
            "manufacturer":  self._device.get("manufacturer", "Duux"),
            "model": self._device.get("sensorType", {}).get("name", "Unknown"),
        }


class DuuxFanSpeedSelector(DuuxSelector):
    """Representation of a Duux fan speed selector."""
    
    FAN_HIGH = "high"
    FAN_LOW = "low"

    def __init__(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_name = "Fan Speed"
        self._attr_icon = "mdi:fan"

    @property
    def options(self):
        """Return available fan modes."""
        return [self.FAN_LOW, self.FAN_HIGH]

    @property
    def current_option(self):
        """Return current fan mode."""
        mode = self.coordinator.data.get("fan")
        mode_map = {
            1: self.FAN_LOW,
            0: self.FAN_HIGH,
        }
        return mode_map.get(mode, self.FAN_LOW)

    async def async_select_option(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        await self.coordinator.async_request_refresh()