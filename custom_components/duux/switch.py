"""Support for Duux switches."""
import logging

from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import *

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
        if sensor_type_id in [DUUX_STID_EDGEHEATER_2023_V1, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))

    async_add_entities(entities)


class DuuxSwitch(CoordinatorEntity, SwitchEntity):
    """Base class for Duux switches."""

    def __init__(self, coordinator, api, device):
        """Initialize the switch."""
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


class DuuxChildLockSwitch(DuuxSwitch):
    """Representation of a Duux child lock switch."""

    def __init__(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_name = "Child Lock"
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
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
              self._api.set_lock, self._device_mac, False
          )
        await self.coordinator.async_request_refresh()


class DuuxNightModeSwitch(DuuxSwitch):
    """Representation of a Duux night mode switch."""

    def __init__(self, coordinator, api,device):
        """Initialize the night mode switch."""
        super().__init__(coordinator,api, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_name = "Night Mode"
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
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
              self._api.set_night_mode, self._device_mac, False
          )
        await self.coordinator.async_request_refresh()

class DuuxSleepModeSwitch(DuuxSwitch):
    """Representation of a Duux sleep mode switch."""

    def __init__(self, coordinator, api,device):
        """Initialize the sleep mode switch."""
        super().__init__(coordinator,api, device)
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_name = "Sleep Mode"
        self._attr_icon = "mdi:weather-night"

    @property
    def is_on(self):
        """Return true if night mode is on."""
        return self.coordinator.data.get("sleep") == 1

    async def async_turn_on(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, True
        )
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
              self._api.set_sleep_mode, self._device_mac, False
          )
        await self.coordinator.async_request_refresh()

class DuuxCleaningModeSwitch(DuuxSwitch):
    """Representation of a Duux self-cleaning mode switch."""

    def __init__(self, coordinator, api,device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(coordinator,api, device)
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_name = "Cleaning Mode"
        self._attr_icon = "mdi:air-filter"

    @property
    def is_on(self):
        """Return true if self-cleaning mode is on."""
        return self.coordinator.data.get("dry") == 1

    async def async_turn_on(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, True
        )
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
              self._api.set_cleaning_mode, self._device_mac, False
          )
        await self.coordinator.async_request_refresh()

class DuuxLaundryModeSwitch(DuuxSwitch):
    """Representation of a Duux laundry mode switch."""

    def __init__(self, coordinator, api,device):
        """Initialize the laundry mode switch."""
        super().__init__(coordinator,api, device)
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_name = "Laundry Mode"
        self._attr_icon = "mdi:tshirt-crew"

    @property
    def is_on(self):
        """Return true if laundry mode is on."""
        return self.coordinator.data.get("laundr") == 1

    async def async_turn_on(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, True
        )
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
              self._api.set_laundry_mode, self._device_mac, False
          )
        await self.coordinator.async_request_refresh()
