"""Support for Duux climate devices."""

import logging
from collections.abc import Iterator
from typing import Any

from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import (
    PRESET_BOOST,
    PRESET_COMFORT,
    PRESET_ECO,
    ClimateEntityFeature,
    HVACMode,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE, UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    DOMAIN,
    DUUX_DTID_HEATER,
    DUUX_DTID_THERMOSTAT,
    DUUX_STID_EDGEHEATER_2023_V1,
    DUUX_STID_EDGEHEATER_V2,
    DUUX_STID_THREESIXTY_2023,
    DUUX_STID_THREESIXTY_TWO,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux climate entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_type_id = device.get("sensorType").get("type")
        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators[device_id]
        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_2023_V1:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


class DuuxClimate(CoordinatorEntity, ClimateEntity):
    """Representation of a Duux climate device."""

    def __init__(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        # Default temperature range (can be overridden by subclasses)
        self._attr_min_temp = 18
        self._attr_max_temp = 30
        self._attr_target_temperature_step = 1

        self._attr_temperature_unit = UnitOfTemperature.CELSIUS
        self._attr_hvac_modes = [HVACMode.OFF, HVACMode.HEAT]
        self._attr_supported_features = (
            ClimateEntityFeature.TARGET_TEMPERATURE
            | ClimateEntityFeature.PRESET_MODE
            | ClimateEntityFeature.TURN_OFF
            | ClimateEntityFeature.TURN_ON
        )

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
    def current_temperature(self):
        """Return the current temperature."""
        return self.coordinator.data.get("temp")

    @property
    def target_temperature(self):
        """Return the temperature we try to reach."""
        return self.coordinator.data.get("sp")

    @property
    def hvac_mode(self):
        """Return current operation."""
        power = self.coordinator.data.get("power", 0)
        return HVACMode.HEAT if power == 1 else HVACMode.OFF

    @property
    def preset_mode(self):
        """Return current preset mode."""
        # Base implementation - override in subclasses
        return ""

    @property
    def preset_modes(self):
        """Return available preset modes."""
        # Base implementation - override in subclasses
        return []

    async def async_set_temperature(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, self._device_mac, temperature
            )
            await self.coordinator.async_request_refresh()

    async def async_set_hvac_mode(self, hvac_mode):
        """Set new HVAC mode."""
        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        await self.coordinator.async_request_refresh()

    async def async_set_preset_mode(self, preset_mode):
        """Set preset mode."""
        # Base implementation - override in subclasses

    @property
    def should_poll(self):
        """No need to poll, coordinator handles it."""
        return False

    @property
    def available(self):
        """Return if entity is available."""
        return self.coordinator.last_update_success

    async def async_added_to_hass(self):
        """When entity is added to hass."""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    async def async_update(self):
        """Update the entity."""
        await self.coordinator.async_request_refresh()


class DuuxClimateAutoDiscovery(DuuxClimate):
    """Duux climate autodiscovery."""

    def __init__(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator, api, device)
        self._presets = self.presets_discovery()

    def presets_discovery(self):
        """Discover available presets."""
        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availableModes")
        if modes is None:
            modes = next(
                DuuxClimateAutoDiscovery._deep_find(self._device, "availableModes"),
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
                yield from DuuxClimateAutoDiscovery._deep_find(value, key)
        elif isinstance(obj, list):
            for item in obj:
                yield from DuuxClimateAutoDiscovery._deep_find(item, key)


class DuuxThreesixtyBase(DuuxClimateAutoDiscovery):
    """Shared base for Threesixty devices."""

    PRESET_LOW = PRESET_ECO
    PRESET_HIGH = PRESET_BOOST
    PRESET_MID = PRESET_COMFORT

    def __init__(self, coordinator, api, device):
        """Initialize the Threesixty climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Threesixty
        self._attr_min_temp = 18
        self._attr_max_temp = 30

    def _normalize_mode_name(self, name, value: Any) -> Any:
        """Change the name for the HA presets for Threesixty models."""
        if value is not None:
            if value == "2":
                return PRESET_ECO
            if value == "1":
                return PRESET_COMFORT
            if value == "0":
                return PRESET_BOOST
        return name


class DuuxThreesixtyClimate(DuuxThreesixtyBase):
    """Duux Threesixty 2023 heater."""


class DuuxThreesixtyTwoClimate(DuuxThreesixtyBase):
    """Duux Threesixty Two 2022 heater."""


class DuuxEdgeTwoClimate(DuuxClimate):
    """Duux Edge heater v2."""

    PRESET_LOW = PRESET_ECO
    PRESET_BOOST = PRESET_BOOST
    PRESET_HIGH = PRESET_COMFORT

    def __init__(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    @property
    def preset_modes(self):
        """Return available preset modes."""
        return [self.PRESET_LOW, self.PRESET_HIGH, self.PRESET_BOOST]

    @property
    def preset_mode(self):
        """Return current preset mode."""
        mode = int(self.coordinator.data.get("heatin") or self.PRESET_LOW)
        mode_map = {1: self.PRESET_LOW, 2: self.PRESET_HIGH, 3: self.PRESET_BOOST}
        return mode_map.get(mode, self.PRESET_LOW)

    async def async_set_preset_mode(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        await self.coordinator.async_request_refresh()


class DuuxEdgeClimate(DuuxClimate):
    """Duux Edge heater 2023 (v1)."""

    PRESET_LOW = PRESET_ECO
    PRESET_HIGH = PRESET_COMFORT

    def __init__(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    @property
    def preset_modes(self):
        """Return available preset modes."""
        return [self.PRESET_LOW, self.PRESET_HIGH]

    @property
    def preset_mode(self):
        """Return current preset mode."""
        mode = int(self.coordinator.data.get("heatin") or self.PRESET_LOW)
        mode_map = {
            1: self.PRESET_LOW,
            2: self.PRESET_HIGH,
        }
        return mode_map.get(mode, self.PRESET_LOW)

    async def async_set_preset_mode(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        await self.coordinator.async_request_refresh()
