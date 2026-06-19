"""Support for Duux switches."""

import logging

from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from custom_components.duux.const import (
    DOMAIN,
    DUUX_STID_BORA_2024,
    DUUX_STID_BRIGHT_2,
    DUUX_STID_EDGEHEATER_2000,
    DUUX_STID_EDGEHEATER_2023_V1,
    DUUX_STID_EDGEHEATER_V2,
    DUUX_STID_WHISPER_FLEX_2,
    DUUX_STID_WHISPER_FLEX_ELIVATE,
    DUUX_STID_NEO,
)

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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

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
    def available(self) -> bool:
        """Return True if entity is available."""
        return self.coordinator.last_update_success and (
            self.coordinator.data or {}
        ).get("online", True)

    @property
    def device_info(self):
        """Return device information."""
        return {
            "identifiers": {(DOMAIN, str(self._device_id))},
            "name": self.device_name,
            "manufacturer": self._device.get("manufacturer", "Duux"),
            "model": self._device.get("sensorType", {}).get("name", "Unknown"),
        }


class DuuxChildLockSwitch(DuuxSwitch):
    """Representation of a Duux child lock switch."""

    def __init__(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_translation_key = "child_lock"
        self._attr_icon = "mdi:lock"

    @property
    def is_on(self):
        """Return true if child lock is on."""
        return (self.coordinator.data or {}).get("lock") == 1

    async def async_turn_on(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["lock"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def async_turn_off(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["lock"] = 0
        self.coordinator.async_set_updated_data(newData)


class DuuxNightModeSwitch(DuuxSwitch):
    """Representation of a Duux night mode switch."""

    def __init__(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_translation_key = "night_mode"
        self._attr_icon = "mdi:weather-night"

    @property
    def is_on(self):
        """Return true if night mode is on."""
        return (self.coordinator.data or {}).get("night") == 1

    async def async_turn_on(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["night"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def async_turn_off(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["night"] = 0
        self.coordinator.async_set_updated_data(newData)


class DuuxSleepModeSwitch(DuuxSwitch):
    """Representation of a Duux sleep mode switch."""

    def __init__(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_translation_key = "sleep_mode"
        self._attr_icon = "mdi:weather-night"

    @property
    def is_on(self):
        """Return true if night mode is on."""
        return (self.coordinator.data or {}).get("sleep") == 1

    async def async_turn_on(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["sleep"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def async_turn_off(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["sleep"] = 0
        self.coordinator.async_set_updated_data(newData)


class DuuxCleaningModeSwitch(DuuxSwitch):
    """Representation of a Duux self-cleaning mode switch."""

    def __init__(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_translation_key = "cleaning_mode"
        self._attr_icon = "mdi:air-filter"

    @property
    def is_on(self):
        """Return true if self-cleaning mode is on."""
        return (self.coordinator.data or {}).get("dry") == 1

    async def async_turn_on(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["dry"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def async_turn_off(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["dry"] = 0
        self.coordinator.async_set_updated_data(newData)


class DuuxLaundryModeSwitch(DuuxSwitch):
    """Representation of a Duux laundry mode switch."""

    def __init__(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_translation_key = "laundry_mode"
        self._attr_icon = "mdi:tshirt-crew"

    @property
    def is_on(self):
        """Return true if laundry mode is on."""
        return (self.coordinator.data or {}).get("laundr") == 1

    async def async_turn_on(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["laundr"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def async_turn_off(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["laundr"] = 0
        self.coordinator.async_set_updated_data(newData)


class DuuxIonizerSwitch(DuuxSwitch):
    """Representation of a Duux ionizer switch."""

    def __init__(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_ionizer"
        self._attr_translation_key = "ionizer"
        self._attr_icon = "mdi:air-filter"

    @property
    def is_on(self):
        """Return true if ionizer is on."""
        return (self.coordinator.data or {}).get("ion") == 1

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        if not super().available:
            return False

        # Constraint for Bright 2: Ionizer unavailable if speed is 1 (manual mode)
        # Note: In Auto mode (speed 0), it should be available.
        data = self.coordinator.data or {}
        speed = data.get("speed")
        sensor_type_id = self._device.get("sensorTypeId")

        if sensor_type_id == DUUX_STID_BRIGHT_2 and speed == 1:
            return False

        return True

    async def async_turn_on(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def async_turn_off(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["ion"] = 0
        self.coordinator.async_set_updated_data(newData)
