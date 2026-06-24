"""Platform for DUUX fan integration."""

from __future__ import annotations

import logging
from collections.abc import Iterator
from typing import Any

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
    percentage_to_ranged_value,
    ranged_value_to_percentage,
)

from .const import (
    DOMAIN,
    DUUX_DTID_AIR_PURIFIER,
    DUUX_DTID_FAN,
    DUUX_FAN_TYPES,
    DUUX_STID_BRIGHT_2,
    DUUX_STID_WHISPER_FLEX,
    DUUX_STID_WHISPER_FLEX_2,
    DUUX_STID_WHISPER_FLEX_ELIVATE,
    DUUX_STID_WHISPER_FLEX_ULTIMATE,
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device.get("deviceId")
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_FAN, *DUUX_DTID_AIR_PURIFIER]:
            if last_word in DUUX_FAN_TYPES:
                _LOGGER.warning(
                    "Device '%s' (type=%s, sensorTypeId=%s, googleType=%s) is not "
                    "officially categorised as a fan but matches a known fan Google "
                    "type — attempting to set up as fan. Please report this to the "
                    "integration developer.",
                    model,
                    device_type_id,
                    sensor_type_id,
                    google_type,
                )
            else:
                continue

        if sensor_type_id == DUUX_STID_WHISPER_FLEX_2:
            entities.append(DuuxWhisperFlexTwoFan(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_WHISPER_FLEX:
            entities.append(DuuxWhisperFlexFan(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxAirPurifierFan(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_WHISPER_FLEX_ULTIMATE:
            entities.append(DuuxWhisperFlexUltimateFan(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_WHISPER_FLEX_ELIVATE:
            entities.append(DuuxWhisperFlexElevateFan(coordinator, api, device))
        else:
            entities.append(DuuxFanAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                "Unknown fan sensorTypeId %s for device '%s' — using generic autodiscovery entity.",
                sensor_type_id,
                model,
            )

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
            FanEntityFeature.SET_SPEED
            | FanEntityFeature.PRESET_MODE
            | FanEntityFeature.TURN_ON
            | FanEntityFeature.TURN_OFF
        )

        self._speed_range = []  # To be defined in subclasses
        self._attr_preset_modes = []  # To be defined in subclasses
        self._attr_speed_count = 0  # To be defined in subclasses

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
            "name": self._attr_name,
            "manufacturer": self._device.get("manufacturer", "Duux"),
            "model": self._device.get("sensorType", {}).get("name", "Unknown"),
        }

    @property
    def is_on(self) -> bool:
        return (self.coordinator.data or {}).get("power") == 1

    @property
    def percentage(self) -> int | None:
        speed = (self.coordinator.data or {}).get("speed")
        if speed is None:
            return None
        try:
            return ordered_list_item_to_percentage(self._speed_range, int(speed))
        except (ValueError, KeyError):
            return None

    @property
    def preset_mode(self) -> str | None:
        """Return the current preset mode."""
        mode = (self.coordinator.data or {}).get("mode")

        return {0: PRESET_MODE_NORMAL, 1: PRESET_MODE_NATURAL, 2: PRESET_MODE_NIGHT}.get(mode)

    async def async_turn_on(
        self,
        percentage: int | None = None,
        preset_mode: str | None = None,
        **kwargs: Any,
    ) -> None:
        """Turn on the fan."""
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["power"] = True
        self.coordinator.async_set_updated_data(newData)

        if percentage is not None:
            await self.async_set_percentage(percentage)

        if preset_mode is not None:
            await self.async_set_preset_mode(preset_mode)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the fan off."""
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["power"] = False
        self.coordinator.async_set_updated_data(newData)

    async def async_set_percentage(self, percentage: int) -> None:
        """Set the speed percentage of the fan."""
        if percentage == 0:
            await self.async_turn_off()
            return

        speed = percentage_to_ordered_list_item(self._speed_range, percentage)
        if speed is not None:
            await self.hass.async_add_executor_job(
                self._api.set_speed,
                self._device_mac,
                speed,
                self._speed_range[0],
                self._speed_range[-1],
            )
            newData = self.coordinator.data
            newData["speed"] = speed
            self.coordinator.async_set_updated_data(newData)

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
            newData = self.coordinator.data
            newData["mode"] = mode_value
            self.coordinator.async_set_updated_data(newData)


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
        SPEED_RANGE_WHISPER_FLEX_2 = list(range(1, 31))
        self._speed_range = SPEED_RANGE_WHISPER_FLEX_2
        self._attr_preset_modes = [PRESET_MODE_NORMAL, PRESET_MODE_NATURAL]
        self._attr_speed_count = len(self._speed_range)


class DuuxWhisperFlexElevateFan(DuuxFan):
    """Representation of a DUUX Whisper Flex Elevatefan."""

    def __init__(
        self,
        coordinator,
        api,
        device,
    ) -> None:
        """Initialize the fan."""
        super().__init__(coordinator, api, device)
        SPEED_RANGE_WHISPER_FLEX_ELEVATE = list(range(1, 27))
        self._speed_range = SPEED_RANGE_WHISPER_FLEX_ELEVATE
        self._attr_preset_modes = [PRESET_MODE_NORMAL, PRESET_MODE_NATURAL]
        self._attr_speed_count = len(self._speed_range)
        self._attr_supported_features = (
            FanEntityFeature.SET_SPEED
            | FanEntityFeature.PRESET_MODE
            | FanEntityFeature.TURN_ON
            | FanEntityFeature.TURN_OFF
            | FanEntityFeature.OSCILLATE
        )

    @property
    def oscillating(self) -> bool:
        """Is the fan oscillating."""
        return (self.coordinator.data or {}).get("horosc") == 1

    async def async_oscillate(self, oscillating: bool) -> None:
        """Oscillate the fan."""
        await self.hass.async_add_executor_job(
            self._api.set_horosc_bool, self._device_mac, 1 if oscillating else 0
        )
        newData = self.coordinator.data
        newData["horosc"] = 1 if oscillating else 0
        self.coordinator.async_set_updated_data(newData)


class DuuxWhisperFlexUltimateFan(DuuxFan):
    """Representation of a DUUX Whisper Flex Ultimate fan (sensorTypeId 40)."""

    def __init__(self, coordinator, api, device):
        super().__init__(coordinator, api, device)

        self._speed_range = list(range(1, 31))
        self._attr_speed_count = len(self._speed_range)

        self._attr_preset_modes = [
            PRESET_MODE_NORMAL,  # value 0
            PRESET_MODE_NATURAL,  # value 1
            PRESET_MODE_NIGHT,  # value 2
        ]


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
    """Duux fan autodiscovery — builds speed list and presets from device traits."""

    def __init__(self, coordinator, api, device):
        super().__init__(coordinator, api, device)
        self._speed_presets = (
            self._discover_speeds()
        )  # list of {"speed", "label", "command"}
        self._mode_presets = (
            self._discover_modes()
        )  # list of {"name", "value", "label", "command"}

        # Wire up the speed range HA needs for percentage conversion
        numeric = [int(p["speed"]) for p in self._speed_presets if p["speed"].isdigit()]
        self._speed_range = (
            list(range(min(numeric), max(numeric) + 1)) if numeric else []
        )
        self._attr_speed_count = len(self._speed_range)

        # Preset modes come from the Modes trait, not speeds
        self._attr_preset_modes = [p["name"] for p in self._mode_presets] or None

    # ── Trait discovery helpers ────────────────────────────────────────────────

    def _get_traits(self) -> list:
        """Return the Traits list from the device's sensorType."""
        sensor_type: dict = self._device.get("sensorType") or {}
        traits = sensor_type.get("Traits")
        if isinstance(traits, list):
            return traits
        # Fallback deep-search (handles unexpected nesting)
        return list(DuuxFanAutoDiscovery._deep_find(self._device, "Traits"))

    def _discover_speeds(self) -> list[dict]:
        """Parse the FanSpeed trait into a list of speed dicts."""
        traits = self._get_traits()

        fan_speed_trait = next(
            (
                t
                for t in traits
                if isinstance(t, dict)
                and (
                    t.get("name") == "FanSpeed"
                    or (t.get("config") or {})
                    .get("unique_name", "")
                    .startswith("FanSpeed")
                )
            ),
            None,
        )

        if fan_speed_trait is None:
            _LOGGER.debug("%s: no FanSpeed trait found", self._attr_name)
            return []

        commands: list = fan_speed_trait.get("commands") or []
        cmd_template: str = commands[0] if commands else "tune set speed {fanSpeed}"

        settings: dict = fan_speed_trait.get("settings") or {}
        raw_speeds: list = (settings.get("availableFanSpeeds") or {}).get(
            "speeds"
        ) or []

        speeds = []
        for raw in raw_speeds:
            if not isinstance(raw, dict):
                continue
            speed_name: str = raw.get("speed_name") or raw.get("speedName") or ""
            if not speed_name:
                continue

            label = speed_name
            for sv in raw.get("speed_values") or []:
                if isinstance(sv, dict) and sv.get("lang") == "en":
                    synonyms = sv.get("speed_synonym") or []
                    if synonyms:
                        label = synonyms[0]
                    break

            speeds.append(
                {
                    "speed": speed_name,
                    "label": label,
                    "command": cmd_template.replace("{fanSpeed}", speed_name),
                }
            )

        _LOGGER.debug("%s: discovered %d speeds", self._attr_name, len(speeds))
        return speeds

    def _discover_modes(self) -> list[dict]:
        """Parse all Modes traits into a flat list of preset dicts."""
        traits = self._get_traits()
        presets: list[dict] = []

        for trait in traits:
            if not isinstance(trait, dict) or trait.get("name") != "Modes":
                continue

            commands: list = trait.get("commands") or []
            cmd_template: str = commands[0] if commands else ""
            settings: dict = trait.get("settings") or {}

            for mode_group in settings.get("availableModes") or []:
                if not isinstance(mode_group, dict):
                    continue

                command_key: str = (
                    mode_group.get("command_key") or mode_group.get("commandKey") or ""
                )

                for raw_setting in mode_group.get("settings") or []:
                    if not isinstance(raw_setting, dict):
                        continue

                    setting_name: str = (
                        raw_setting.get("setting_name")
                        or raw_setting.get("settingName")
                        or ""
                    )
                    setting_value: str = (
                        raw_setting.get("setting_value")
                        or raw_setting.get("settingValue")
                        or ""
                    )

                    label = setting_name
                    for sv in raw_setting.get("setting_values") or []:
                        if isinstance(sv, dict) and sv.get("lang") == "en":
                            synonyms = sv.get("setting_synonym") or []
                            if synonyms:
                                label = synonyms[0]
                            break

                    command = cmd_template.replace(f"{{{command_key}}}", setting_value)

                    presets.append(
                        {
                            "name": label,  # display name, e.g. "Night"
                            "setting_name": setting_name,  # raw key, e.g. "low"
                            "value": setting_value,  # raw value, e.g. "2"
                            "command": command,  # e.g. "tune set mode 2"
                        }
                    )

        _LOGGER.debug("%s: discovered mode presets: %s", self._attr_name, presets)
        return presets

    # ── HA properties ─────────────────────────────────────────────────────────

    @property
    def percentage(self) -> int | None:
        """Return current speed as a percentage."""
        speed = (self.coordinator.data or {}).get("speed")
        if speed is None or not self._speed_range:
            return None
        try:
            return ordered_list_item_to_percentage(self._speed_range, int(speed))
        except (ValueError, KeyError):
            return None

    @property
    def preset_mode(self) -> str | None:
        """Return current preset mode label."""
        if not self._mode_presets:
            return None
        mode = (self.coordinator.data or {}).get("mode")
        if mode is None:
            return None
        for preset in self._mode_presets:
            if preset["value"] == str(mode):
                return preset["name"]
        return None

    @property
    def preset_modes(self) -> list[str] | None:
        """Return available preset mode labels."""
        return [p["name"] for p in self._mode_presets] or None

    # ── HA commands ───────────────────────────────────────────────────────────

    async def async_set_percentage(self, percentage: int) -> None:
        """Set speed by percentage."""
        if percentage == 0:
            await self.async_turn_off()
            return
        if not self._speed_range:
            return
        speed = percentage_to_ordered_list_item(self._speed_range, percentage)
        # Find the matching preset to get the pre-built command
        preset = next(
            (p for p in self._speed_presets if int(p["speed"]) == speed), None
        )
        command = preset["command"] if preset else f"tune set speed {speed}"
        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, command
        )
        newData = self.coordinator.data
        newData["speed"] = speed
        self.coordinator.async_set_updated_data(newData)

    async def async_set_preset_mode(self, preset_mode: str) -> None:
        """Set preset mode by label."""
        preset = next((p for p in self._mode_presets if p["name"] == preset_mode), None)
        if preset is None:
            _LOGGER.warning(
                "%s: unknown preset mode '%s'", self._attr_name, preset_mode
            )
            return
        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, preset["command"]
        )
        newData = self.coordinator.data
        newData["mode"] = preset["value"]
        self.coordinator.async_set_updated_data(newData)

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


class DuuxAirPurifierFan(DuuxFan):
    """Representation of a Duux air purifier fan."""

    SPEED_RANGE = (1, 4)

    def __init__(self, coordinator, api, device):
        """Initialize the fan."""
        super().__init__(coordinator, api, device)
        self._attr_supported_features = (
            FanEntityFeature.SET_SPEED
            | FanEntityFeature.PRESET_MODE
            | FanEntityFeature.TURN_ON
            | FanEntityFeature.TURN_OFF
        )
        SPEED_RANGE_AIR_PURIFIER = list(range(1, 4))
        self._speed_range = SPEED_RANGE_AIR_PURIFIER
        self._attr_speed_count = len(self._speed_range)
        self._attr_preset_modes = ["Auto"]

    @property
    def is_on(self) -> bool:
        """Return true if fan is on."""
        return (self.coordinator.data or {}).get("power") == 1

    @property
    def percentage(self) -> int | None:
        """Return the current speed percentage."""
        data = self.coordinator.data or {}
        speed = data.get("speed")
        if speed is None:
            return None
        if speed == 0:
            # Auto mode: estimate effective speed from air quality sensors
            # TVOC>1 (Polluted or Harmful) → max speed immediately
            tvoc = data.get("tvoc") or 0
            if tvoc > 1:
                return ranged_value_to_percentage(self.SPEED_RANGE, self.SPEED_RANGE[1])
            # Otherwise derive from AQ: aq=0→speed 1, aq=1→2, aq=2→3, aq≥3→4
            aq = data.get("aq") or 0
            estimated = min(aq + 1, self.SPEED_RANGE[1])
            return ranged_value_to_percentage(self.SPEED_RANGE, estimated)
        return ranged_value_to_percentage(self.SPEED_RANGE, speed)

    @property
    def speed_count(self) -> int:
        """Return the number of speeds the fan supports."""
        return self.SPEED_RANGE[1]

    @property
    def preset_mode(self) -> str | None:
        """Return the current preset mode."""
        speed = (self.coordinator.data or {}).get("speed")
        if speed == 0:
            return "Auto"
        return None

    async def async_set_percentage(self, percentage: int) -> None:
        """Set the speed percentage of the fan."""
        if percentage == 0:
            await self.async_turn_off()
            return

        speed = round(percentage_to_ranged_value(self.SPEED_RANGE, percentage))

        # Ensure power is ON before sending speed command
        if not self.is_on:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )

        await self.hass.async_add_executor_job(
            self._api.set_purifier_speed, self._device_mac, speed
        )

        newData = self.coordinator.data
        newData["speed"] = speed

        # Constraint: Ionizer must be OFF if speed is at lowest (1)
        if speed == 1 and newData.get("ion") == 1:
            await self.hass.async_add_executor_job(
                self._api.set_ionizer, self._device_mac, False
            )
            newData["ion"] = 0

        self.coordinator.async_set_updated_data(newData)

    async def async_set_preset_mode(self, preset_mode: str) -> None:
        """Set the preset mode of the fan."""
        if preset_mode == "Auto":
            newData = self.coordinator.data
            # Ensure power is ON before sending mode command
            if not self.is_on:
                await self.hass.async_add_executor_job(
                    self._api.set_power, self._device_mac, True
                )
                newData["power"] = 1
            await self.hass.async_add_executor_job(
                self._api.set_purifier_speed, self._device_mac, 0
            )
            newData["speed"] = 0
            self.coordinator.async_set_updated_data(newData)

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
            newData = self.coordinator.data
            newData["power"] = 1
            self.coordinator.async_set_updated_data(newData)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn off the fan."""
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["power"] = 0
        self.coordinator.async_set_updated_data(newData)
