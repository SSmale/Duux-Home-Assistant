"""Support for Duux switches."""
import logging

from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators[device_id]

        # Only Edge heaters have night mode
        if sensor_type_id == 50 or sensor_type_id == 51:  # Edge heater v1, v2
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
    
    async_add_entities(entities)


class DuuxSwitch(CoordinatorEntity, SwitchEntity):
    """Base class for Duux switches."""

    def __init__(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
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


class DuuxChildLockSwitch(DuuxSwitch):
    """Representation of a Duux child lock switch."""

    def __init__(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_name = f"{self.device_name} Child Lock"
        self._attr_icon = "mdi:lock"

    @property
    def is_on(self):
        """Return true if child lock is on."""
        return self.coordinator.data.get("lock") == 1

    async def async_turn_on(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, True
        )
        await self._coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
              self._api.set_lock, self._device_mac, False
          )
        await self._coordinator.async_request_refresh()


class DuuxNightModeSwitch(DuuxSwitch):
    """Representation of a Duux night mode switch."""

    def __init__(self, coordinator, api,device):
        """Initialize the night mode switch."""
        super().__init__(coordinator,api, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_name = f"{self.device_name} Night Mode"
        self._attr_icon = "mdi:weather-night"

    @property
    def is_on(self):
        """Return true if night mode is on."""
        return self.coordinator.data.get("night") == 1

    async def async_turn_on(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, True
        )
        await self._coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
              self._api.set_night_mode, self._device_mac, False
          )
        await self._coordinator.async_request_refresh()