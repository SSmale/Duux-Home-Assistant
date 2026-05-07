"""Support for Duux fans."""

import logging
import math
from typing import Any

from homeassistant.components.fan import FanEntity, FanEntityFeature
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util.percentage import (
    int_states_in_range,
    percentage_to_ranged_value,
    ranged_value_to_percentage,
)

from .const import DOMAIN, DUUX_STID_BRIGHT_2

_LOGGER = logging.getLogger(__name__)

SPEED_RANGE = (1, 4)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Duux fan entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators[device_id]

        if sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxAirPurifierFan(coordinator, api, device))

    async_add_entities(entities)


class DuuxFan(CoordinatorEntity, FanEntity):
    """Base class for Duux fans."""

    def __init__(self, coordinator, api, device):
        """Initialize the fan."""
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


class DuuxAirPurifierFan(DuuxFan):
    """Representation of a Duux air purifier fan."""

    def __init__(self, coordinator, api, device):
        """Initialize the fan."""
        super().__init__(coordinator, api, device)
        self._attr_supported_features = (
            FanEntityFeature.SET_SPEED | FanEntityFeature.PRESET_MODE
        )
        self._attr_preset_modes = ["Auto"]

    @property
    def is_on(self) -> bool:
        """Return true if fan is on."""
        return self.coordinator.data.get("power") == 1

    @property
    def percentage(self) -> int | None:
        """Return the current speed percentage."""
        speed = self.coordinator.data.get("speed")
        if speed is None or speed == 0:
            return None
        return ranged_value_to_percentage(SPEED_RANGE, speed)

    @property
    def speed_count(self) -> int:
        """Return the number of speeds the fan supports."""
        return int_states_in_range(SPEED_RANGE)

    @property
    def preset_mode(self) -> str | None:
        """Return the current preset mode."""
        speed = self.coordinator.data.get("speed")
        if speed == 0:
            return "Auto"
        return None

    async def async_set_percentage(self, percentage: int) -> None:
        """Set the speed percentage of the fan."""
        if percentage == 0:
            await self.async_turn_off()
            return

        speed = math.ceil(percentage_to_ranged_value(SPEED_RANGE, percentage))
        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, speed
        )
        # Ensure power is ON when setting speed
        if not self.is_on:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        await self.coordinator.async_request_refresh()

    async def async_set_preset_mode(self, preset_mode: str) -> None:
        """Set the preset mode of the fan."""
        if preset_mode == "Auto":
            await self.hass.async_add_executor_job(
                self._api.set_speed, self._device_mac, 0
            )
            # Ensure power is ON when setting auto mode
            if not self.is_on:
                await self.hass.async_add_executor_job(
                    self._api.set_power, self._device_mac, True
                )
        await self.coordinator.async_request_refresh()

    async def async_turn_on(
        self,
        percentage: int | None = None,
        preset_mode: str | None = None,
        **kwargs: Any,
    ) -> None:
        """Turn on the fan."""
        if percentage is not None:
            await self.async_set_percentage(percentage)
        elif preset_mode is not None:
            await self.async_set_preset_mode(preset_mode)
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
            await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn off the fan."""
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, False
        )
        await self.coordinator.async_request_refresh()
