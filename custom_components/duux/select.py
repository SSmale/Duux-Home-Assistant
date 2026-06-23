"""Support for Duux selectors."""

import logging

from homeassistant.components.select import SelectEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from homeassistant.const import (
    EntityCategory,
    UnitOfTime,
)

from .const import (
    DOMAIN,
    DUUX_STID_BORA_2024,
    DUUX_STID_BEAM_MINI,
    DUUX_STID_BRIGHT_2,
    DUUX_STID_EDGEHEATER_V2,
    DUUX_STID_NEO,
    DUUX_STID_NORTH,
    DUUX_STID_WHISPER_FLEX_ELIVATE,
)

_LOGGER = logging.getLogger(__name__)

SWING_OFF = "Off"

# Horizontal swing button cycles through 3 stripe icons on the device.
# Levels are symmetric about centre (e.g. level 2 = 60 deg total = 30 deg
# each side). Raw values are inferred to be sequential indices, matching
# the pattern every other trait in this integration uses (mode/night/lock
# are all small sequential ints) — NOT confirmed against a trait schema,
# since horosc has no trait definition in the diagnostics sample.
HORIZONTAL_SWING_OPTIONS: dict[str, int] = {
    SWING_OFF: 0,
    "30°": 1,
    "60°": 2,
    "90°": 3,
}

# Vertical swing button cycles through 2 stripe icons on the device.
# Arc is NOT symmetric about horizontal (level 1 = 10 deg below to 35 deg
# above; level 2 = 10 deg below to 90 deg above). Same caveat as above —
# raw values are inferred, not confirmed.
VERTICAL_SWING_OPTIONS: dict[str, int] = {
    SWING_OFF: 0,
    "45°": 1,
    "100°": 2,
}


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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_NORTH:
            entities.append(DuuxNorthTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None and sensor_type_id not in [
            DUUX_STID_NORTH
        ]:
            # North's "tilt" is an on/off toggle (Louver Swing), not
            # an angle level like the Ultimate Fan's
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


class DuuxSwingSelect(CoordinatorEntity, SelectEntity):
    """Base class for a DUUX swing-level select entity.

    Subclasses only need to set `_options_map` and `_data_key`, override
    `_set_value` to call the matching duux_api method, and set a
    name/icon — everything else (device linkage, availability, refresh)
    lives here. To attach a swing select to another fan model,
    instantiate the relevant subclass with that device's
    (coordinator, api, device), the same way entities are added in
    fan.py.
    """

    _options_map: dict[str, int] = {}
    _data_key: str = ""

    def _set_value(self, device_mac: str, value: int):
        """Call the duux_api method for this axis. Override in subclasses."""
        raise NotImplementedError

    def __init__(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(self._options_map.keys())

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self.coordinator.last_update_success and (
                self.coordinator.data or {}
        ).get("online", True)

    @property
    def device_info(self):
        """Return device information, linking this select to its fan device."""
        return {
            "identifiers": {(DOMAIN, str(self._device_id))},
            "name": self._device.get("displayName") or self._device.get("name"),
            "manufacturer": self._device.get("manufacturer", "Duux"),
            "model": self._device.get("sensorType", {}).get("name", "Unknown"),
        }

    @property
    def current_option(self) -> str | None:
        """Return the currently selected swing level."""
        raw_value = (self.coordinator.data or {}).get(self._data_key)
        if raw_value is None:
            return None

        for label, value in self._options_map.items():
            if value == raw_value:
                return label

        _LOGGER.debug(
            "%s: raw value %s for '%s' doesn't match any known option",
            getattr(self, "_attr_name", None),
            raw_value,
            self._data_key,
        )
        return None

    async def async_select_option(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)


class DuuxHorizontalOscillationSelect(DuuxSwingSelect):
    """Select entity controlling horizontal oscillation level."""

    _options_map = HORIZONTAL_SWING_OPTIONS
    _data_key = "horosc"

    def _set_value(self, device_mac: str, value: int):
        return self._api.set_horosc(device_mac, value)

    def __init__(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"


class DuuxVerticalOscillationSelect(DuuxSwingSelect):
    """Select entity controlling vertical swing level."""

    _options_map = VERTICAL_SWING_OPTIONS
    _data_key = "verosc"

    def _set_value(self, device_mac: str, value: int):
        return self._api.set_verosc(device_mac, value)

    def __init__(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"


class DuuxHorizontalSwingSelect(DuuxSwingSelect):
    """Select entity controlling horizontal swing level."""

    _options_map = HORIZONTAL_SWING_OPTIONS
    _data_key = "swing"

    def _set_value(self, device_mac: str, value: int):
        return self._api.set_swing(device_mac, value)

    def __init__(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"


class DuuxVerticalTiltSelect(DuuxSwingSelect):
    """Select entity controlling vertical tilt level."""

    _options_map = VERTICAL_SWING_OPTIONS
    _data_key = "tilt"

    def _set_value(self, device_mac: str, value: int):
        return self._api.set_tilt(device_mac, value)

    def __init__(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"


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


class DuuxFanSpeedSelector(DuuxSelector):
    """Representation of a Duux fan speed selector."""

    FAN_HIGH = "high"
    FAN_LOW = "low"

    def __init__(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_translation_key = "fan_speed"
        self._attr_icon = "mdi:fan"

    @property
    def options(self):
        """Return available fan modes."""
        return [self.FAN_LOW, self.FAN_HIGH]

    @property
    def current_option(self):
        """Return current fan mode."""
        mode = (self.coordinator.data or {}).get("fan")
        mode_map = {
            1: self.FAN_LOW,
            0: self.FAN_HIGH,
        }
        return mode_map.get(int(mode) if mode is not None else 1, self.FAN_LOW)

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
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)


class DuuxTimerSelector(DuuxSelector):
    """Representation of a Duux timer selector."""

    def __init__(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    @property
    def current_option(self):
        """Return current timer."""
        timer = (self.coordinator.data or {}).get("timer")
        return str(timer) if timer is not None else None

    async def async_select_option(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)


class DuuxBright2TimerSelector(DuuxTimerSelector):
    """Representation of a Duux Bright 2 timer selector."""

    def __init__(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        # Bright 2 supports specific timer presets only (hours): 0=off, 1, 2, 4, 8
        self._attr_options = ["0", "1", "2", "4", "8"]


class DuuxNeoSpeedSelector(DuuxSelector):
    """Representation of a Duux Neo spray speed selector."""

    SPEED_LOW = "Low"
    SPEED_MID = "Mid"
    SPEED_HIGH = "High"

    def __init__(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = "spray_volume"
        self._attr_icon = "mdi:weather-partly-rainy"
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    @property
    def current_option(self):
        """Return current speed."""
        mode = self.coordinator.data.get("speed", self.SPEED_LOW)
        mode_map = {
            0: self.SPEED_LOW,
            1: self.SPEED_MID,
            2: self.SPEED_HIGH,
        }
        return mode_map.get(mode, self.SPEED_LOW)

    async def async_select_option(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)


class DuuxNorthTimerSelector(DuuxTimerSelector):
    """North-specific Timer: also powers the unit on for non zero
    values. Kept as a subclass rather than
    changing the shared DuuxTimerSelector, since this behaviour isn't
    confirmed for the other devices that use it (Bora/Neo/BeamMini/
    Bright2/Edge).
    """

    async def async_select_option(self, option):
        """Set timer amount, turning the unit on first if non-zero."""
        try:
            amount = max(0, min(24, int(option)))
        except (TypeError, ValueError):
            amount = 0

        if amount > 0:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        if amount > 0:
            newData["power"] = 1
        self.coordinator.async_set_updated_data(newData)
