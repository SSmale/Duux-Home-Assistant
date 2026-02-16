"""Platform for DUUX fan integration."""

from __future__ import annotations

import logging
from typing import Any, Iterator

from homeassistant.components.fan import (
    FanEntity,
    FanEntityFeature,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util.percentage import (
    ordered_list_item_to_percentage,
    percentage_to_ordered_list_item,
)

from .const import (
    DOMAIN,
    DUUX_FAN_TYPES,
    DUUX_DTID_FAN,
    DUUX_STID_WHISPER_FLEX,
    DUUX_STID_WHISPER_FLEX_2,
)

_LOGGER = logging.getLogger(__name__)

# Define preset modes
PRESET_MODE_NORMAL = "normal"
PRESET_MODE_NATURAL = "natural"
PRESET_MODE_NIGHT = "night"


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up DUUX fan based on a config entry."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_type_id = device.get("sensorType").get("type")
        google_type = device.get("sensorType").get("googleDeviceType")
        last_word = google_type.split(".")[-1]  # "FAN"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators[device_id]

        model = device.get("sensorType", {}).get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_FAN]:
            if last_word in DUUX_FAN_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the fan platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a fan device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate fan entity based on heater type
        if sensor_type_id == DUUX_STID_WHISPER_FLEX_2:
            entities.append(DuuxWhisperFlexTwoFan(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_WHISPER_FLEX:
            entities.append(DuuxWhisperFlexFan(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxFanAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(f"Unknown fan type {sensor_type_id}, using generic entity")

    async_add_entities(entities)


class DuuxFan(CoordinatorEntity, FanEntity):
    """Representation of a DUUX fan."""

    def __init__(
        self,
        coordinator,
        api,
        device,
    ) -> None:
        """Initialize the fan."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_supported_features = (
            FanEntityFeature.SET_SPEED | FanEntityFeature.PRESET_MODE
        )

        self._speed_range = []  # To be defined in subclasses
        self._attr_preset_modes = []  # To be defined in subclasses
        self._attr_speed_count = 0  # To be defined in subclasses

    @property
    def is_on(self):
        power = self.coordinator.data.get("power", 0)
        return power == 1

    @property
    def percentage(self) -> int | None:
        """Return the current speed percentage."""
        speed = self.coordinator.data.get("speed")
        if speed is None:
            return None

        return ordered_list_item_to_percentage(self._speed_range, speed)

    @property
    def preset_mode(self) -> str | None:
        """Return the current preset mode."""
        mode = self.coordinator.data.get("mode")

        if mode == 0:
            return PRESET_MODE_NORMAL
        elif mode == 1:
            return PRESET_MODE_NATURAL
        elif mode == 2:
            return PRESET_MODE_NIGHT

        return None

    async def async_turn_on(
        self,
        percentage: int | None = None,
        preset_mode: str | None = None,
        **kwargs: Any,
    ) -> None:
        """Turn on the fan."""
        await self.hass.async_add_executor_job(self._api.set_power, self._device_mac, 1)
        await self.coordinator.async_request_refresh()

        if percentage is not None:
            await self.async_set_percentage(percentage)

        if preset_mode is not None:
            await self.async_set_preset_mode(preset_mode)

        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the fan off."""
        await self.hass.async_add_executor_job(self._api.set_power, self._device_mac, 0)
        await self.coordinator.async_request_refresh()

    async def async_set_percentage(self, percentage: int) -> None:
        """Set the speed percentage of the fan."""
        if percentage == 0:
            await self.async_turn_off()
            return

        speed = percentage_to_ordered_list_item(self._speed_range, percentage)
        if speed is not None:
            await self.hass.async_add_executor_job(
                self._api.set_speed, self._device_mac, speed
            )
            await self.coordinator.async_request_refresh()

    async def async_set_preset_mode(self, preset_mode: str) -> None:
        """Set the preset mode of the fan."""
        mode_value = None

        if preset_mode == PRESET_MODE_NORMAL:
            mode_value = 0
        elif preset_mode == PRESET_MODE_NATURAL:
            mode_value = 1
        elif preset_mode == PRESET_MODE_NIGHT:
            mode_value = 2

        if mode_value is not None:
            await self.hass.async_add_executor_job(
                self._api.set_mode, self._device_mac, mode_value
            )
            await self.coordinator.async_request_refresh()


class DuuxWhisperFlexTwoFan(DuuxFan):
    """Representation of a DUUX Whisper Flex 2 fan."""

    def __init__(
        self,
        coordinator,
        api,
        device,
    ) -> None:
        """Initialize the fan."""
        super().__init__(coordinator, api, device)
        SPEED_RANGE_WHISPER_FLEX_2 = list(range(1, 30))
        self._speed_range = SPEED_RANGE_WHISPER_FLEX_2
        self._attr_preset_modes = [PRESET_MODE_NORMAL, PRESET_MODE_NATURAL]
        self._attr_speed_count = len(self._speed_range)


class DuuxWhisperFlexFan(DuuxFan):
    """Representation of a DUUX Whisper Flex 2 fan."""

    def __init__(
        self,
        coordinator,
        api,
        device,
    ) -> None:
        """Initialize the fan."""
        super().__init__(coordinator, api, device)
        SPEED_RANGE_WHISPER_FLEX = list(range(1, 26))
        self._speed_range = SPEED_RANGE_WHISPER_FLEX
        self._attr_preset_modes = [
            PRESET_MODE_NORMAL,
            PRESET_MODE_NATURAL,
            PRESET_MODE_NIGHT,
        ]
        self._attr_speed_count = len(self._speed_range)


class DuuxFanAutoDiscovery(DuuxFan):
    """Duux fan autodiscovery."""

    def __init__(self, coordinator, api, device):
        """Initialize the fan device."""
        super().__init__(coordinator, api, device)
        self._presets = self.presets_discovery()

    def presets_discovery(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availableModes")
        if modes is None:
            modes = next(
                DuuxFanAutoDiscovery._deep_find(self._device, "availableModes"),
                None,
            )

        if isinstance(modes, list):
            modes = next(
                (
                    candidate
                    for candidate in modes
                    if isinstance(candidate, dict) and candidate.get("settings")
                ),
                None,
            )

        if not isinstance(modes, dict):
            _LOGGER.debug("No available modes found")
            return []

        settings = modes.get("settings")
        if not isinstance(settings, list):
            _LOGGER.debug("No settings found in available modes")
            return []

        command_prefix = (
            modes.get("command_key") or modes.get("commandKey") or modes.get("key")
        )

        presets = []
        for setting in settings:
            if not isinstance(setting, dict):
                continue

            name = (
                setting.get("setting_name")
                or setting.get("settingName")
                or setting.get("name")
            )

            value = (
                setting.get("setting_value")
                or setting.get("settingValue")
                or setting.get("value")
            )

            name = self._normalize_mode_name(name, value)

            command = setting.get("command")
            if command is None and command_prefix and value is not None:
                command = f"{command_prefix} {value}"
            elif command is None:
                command = value

            if name and command is not None:
                normalized_command = str(command)
                normalized_value = None if value is None else str(value)
                presets.append(
                    {
                        "name": str(name),
                        "command": normalized_command,
                        "value": normalized_value,
                    }
                )

        _LOGGER.debug("Discovered presets: %s", presets)

        return presets

    def _normalize_mode_name(self, name, value: Any) -> Any:
        """Return normalized mode value."""
        return name

    @property
    def preset_mode(self):
        """Return current preset mode."""
        mode = self.coordinator.data.get("mode")
        for preset in self._presets:
            if preset["value"] == str(mode):
                return preset["name"]
        return None

    @property
    def preset_modes(self):
        """Return available preset modes."""
        # Base implementation - override in subclasses if needed
        return [preset["name"] for preset in self._presets]

    async def async_set_preset_mode(self, preset_mode):
        """Set preset mode."""
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        await self.coordinator.async_request_refresh()

    @staticmethod
    def _deep_find(obj: Any, key: str) -> Iterator[Any]:
        """Yield every value for `key` inside a nested dict/list structure."""
        if isinstance(obj, dict):
            if key in obj:
                yield obj[key]
            for value in obj.values():
                yield from DuuxFanAutoDiscovery._deep_find(value, key)
        elif isinstance(obj, list):
            for item in obj:
                yield from DuuxFanAutoDiscovery._deep_find(item, key)
