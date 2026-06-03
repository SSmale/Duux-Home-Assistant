"""Support for Duux selectors."""

import logging

from homeassistant.components.select import SelectEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from homeassistant.const import (
    UnitOfTime,
)

from .const import (
    DOMAIN,
    DUUX_STID_BORA_2024,
    DUUX_STID_WHISPER_FLEX,
    DUUX_STID_WHISPER_FLEX_2,
    DUUX_STID_WHISPER_FLEX_ELIVATE,
)

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
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if sensor_type_id in (DUUX_STID_WHISPER_FLEX_2, DUUX_STID_WHISPER_FLEX):
            entities.append(DuuxHorizontalOscillationSelector(coordinator, api, device))
            entities.append(DuuxVerticalOscillationSelector(coordinator, api, device))

        if sensor_type_id == DUUX_STID_WHISPER_FLEX_ELIVATE:
            entities.append(DuuxHorizontalOscillationSelector(coordinator, api, device))
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))

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
            "manufacturer": self._device.get("manufacturer", "Duux"),
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
        mode = self.coordinator.data.get("fan", 1)
        mode_map = {
            1: self.FAN_LOW,
            0: self.FAN_HIGH,
        }
        return mode_map.get(mode)

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


class DuuxHorizontalOscillationSelector(DuuxSelector):
    """Selector for horizontal oscillation angle."""

    OPTIONS = {"Off": 0, "30°": 1, "60°": 2, "90°": 3}

    def __init__(self, coordinator, api, device):
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horosc"
        self._attr_name = "Horizontal Oscillation"
        self._attr_icon = "mdi:rotate-left"
        self._attr_options = list(self.OPTIONS.keys())

    @property
    def current_option(self):
        value = self.coordinator.data.get("horosc", 0)
        return next((k for k, v in self.OPTIONS.items() if v == value), "Off")

    async def async_select_option(self, option):
        value = self.OPTIONS.get(option, 0)
        await self.hass.async_add_executor_job(
            self._api.set_horosc, self._device_mac, value
        )
        await self.coordinator.async_request_refresh()


class DuuxVerticalOscillationSelector(DuuxSelector):
    """Selector for vertical oscillation angle."""

    OPTIONS = {"Off": 0, "45°": 1, "100°": 2}

    def __init__(self, coordinator, api, device):
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_verosc"
        self._attr_name = "Vertical Oscillation"
        self._attr_icon = "mdi:rotate-right"
        self._attr_options = list(self.OPTIONS.keys())

    @property
    def current_option(self):
        value = self.coordinator.data.get("verosc", 0)
        return next((k for k, v in self.OPTIONS.items() if v == value), "Off")

    async def async_select_option(self, option):
        value = self.OPTIONS.get(option, 0)
        await self.hass.async_add_executor_job(
            self._api.set_verosc, self._device_mac, value
        )
        await self.coordinator.async_request_refresh()


class DuuxTimerSelector(DuuxSelector):
    """Representation of a Duux timer selector."""

    def __init__(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_name = "Timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    @property
    def current_option(self):
        """Return current timer."""
        return str(self.coordinator.data.get("timer"))

    async def async_select_option(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except:
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        await self.coordinator.async_request_refresh()
