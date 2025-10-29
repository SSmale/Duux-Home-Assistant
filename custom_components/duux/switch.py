"""Support for Duux switches."""
import logging

from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]
    
    entities = []
    for device in coordinator.data:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["id"]
        
        # All heaters have child lock
        entities.append(DuuxChildLockSwitch(coordinator, device))
        
        # Only Edge heaters have night mode
        if sensor_type_id == 50:  # Edge heater v2
            entities.append(DuuxNightModeSwitch(coordinator, device))
    
    async_add_entities(entities)


class DuuxSwitch(CoordinatorEntity, SwitchEntity):
    """Base class for Duux switches."""

    def __init__(self, coordinator, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._device = device
        self._device_id = device["id"]
        self._attr_name = device.get("displayName") or device.get("name")

    @property
    def device_info(self):
        """Return device information."""
        return {
            "identifiers": {(DOMAIN, str(self._device_id))},
            "name": self._attr_name,
            "manufacturer": "Duux",
            "model": self._device.get("sensorType", {}).get("name", "Unknown"),
        }

    def _get_device_data(self):
        """Get the latest device data from coordinator."""
        for device in self.coordinator.data:
            if device["id"] == self._device_id:
                return device
        return None


class DuuxChildLockSwitch(DuuxSwitch):
    """Representation of a Duux child lock switch."""

    def __init__(self, coordinator, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_name = f"{self._attr_name} Child Lock"
        self._attr_icon = "mdi:lock"

    @property
    def is_on(self):
        """Return true if child lock is on."""
        data = self._get_device_data()
        if data and "latestData" in data and "fullData" in data["latestData"]:
            return data["latestData"]["fullData"].get("lock") == 1
        return False

    async def async_turn_on(self, **kwargs):
        """Turn on child lock."""
        api = self.coordinator.api
        await api.set_child_lock(self._device_id, "1")
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        """Turn off child lock."""
        api = self.coordinator.api
        await api.set_child_lock(self._device_id, "0")
        await self.coordinator.async_request_refresh()


class DuuxNightModeSwitch(DuuxSwitch):
    """Representation of a Duux night mode switch."""

    def __init__(self, coordinator, device):
        """Initialize the night mode switch."""
        super().__init__(coordinator, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_name = f"{self._attr_name} Night Mode"
        self._attr_icon = "mdi:weather-night"

    @property
    def is_on(self):
        """Return true if night mode is on."""
        data = self._get_device_data()
        if data and "latestData" in data and "fullData" in data["latestData"]:
            return data["latestData"]["fullData"].get("night") == 1
        return False

    async def async_turn_on(self, **kwargs):
        """Turn on night mode."""
        api = self.coordinator.api
        await api.set_night_mode(self._device_id, "1")
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        """Turn off night mode."""
        api = self.coordinator.api
        await api.set_night_mode(self._device_id, "0")
        await self.coordinator.async_request_refresh()