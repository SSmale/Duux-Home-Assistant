"""Support for Duux de/humidifier devices."""

import logging

from homeassistant.components.humidifier import HumidifierDeviceClass, HumidifierEntity
from homeassistant.components.humidifier.const import (
    MODE_AUTO,
    MODE_NORMAL,
    MODE_BOOST,
    HumidifierAction,
    HumidifierEntityFeature,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    DOMAIN,
    DUUX_DTID_HUMIDIFIER,
    DUUX_STID_BEAM_MINI,
    DUUX_STID_BORA_2024,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux de/humidifier entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_type_id = device.get("sensorType").get("type")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators[device_id]
        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


class DuuxBase(CoordinatorEntity, HumidifierEntity):
    """Representation of a Duux de/humidifier device."""

    def __init__(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

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
    def mode(self):
        """Return current preset mode."""
        # Base implementation - override in subclasses
        return str()

    @property
    def available_modes(self):
        """Return available preset modes."""
        # Base implementation - override in subclasses
        return []

    async def async_set_mode(self, mode):
        """Set preset mode."""
        # Base implementation - override in subclasses
        pass

    async def async_turn_on(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, True
        )
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, False
        )
        await self.coordinator.async_request_refresh()

    @property
    def is_on(self):
        power = self.coordinator.data.get("power", 0)
        return power == 1

    @property
    def action(self):
        """Return current action."""
        # Base implementation - override in subclasses
        pass

    @property
    def current_humidity(self):
        """Return the current humidity."""
        return self.coordinator.data.get("hum")

    @property
    def target_humidity(self):
        """Return the humidity we try to reach."""
        return self.coordinator.data.get("sp")

    async def async_set_humidity(self, humidity: int):
        """Set new target humidity."""
        await self.hass.async_add_executor_job(
            self._api.set_humidity, self._device_mac, humidity
        )
        await self.coordinator.async_request_refresh()

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


class DuuxDehumidifier(DuuxBase):
    """Representation of a Duux dehumidifier device."""

    def __init__(self, coordinator, api, device):
        """Initialize the dehumidifier device."""
        super().__init__(coordinator, api, device)

        self._attr_device_class = HumidifierDeviceClass.DEHUMIDIFIER

    @property
    def action(self):
        """Return current action."""
        power = self.coordinator.data.get("power", 0)
        return HumidifierAction.DRYING if power == 1 else HumidifierAction.OFF


class DuuxHumidifier(DuuxBase):
    """Representation of a Duux humidifier device."""

    def __init__(self, coordinator, api, device):
        """Initialize the humidifier device."""
        super().__init__(coordinator, api, device)

        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

    @property
    def action(self):
        """Return current action."""
        power = self.coordinator.data.get("power", 0)
        return HumidifierAction.HUMIDIFYING if power == 1 else HumidifierAction.OFF


class DuuxBoraDehumidifier(DuuxDehumidifier):
    """Duux Bora Dehumidifier."""

    PRESET_AUTO = MODE_AUTO
    PRESET_CONTINUOUS = MODE_BOOST

    def __init__(self, coordinator, api, device):
        """Initialize the Bora dehumidifier device."""
        super().__init__(coordinator, api, device)

        # min/max humidity settings for Bora.
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    @property
    def available_modes(self):
        """Return available preset modes."""
        return [self.PRESET_AUTO, self.PRESET_CONTINUOUS]

    @property
    def mode(self):
        """Return current preset mode."""
        mode = self.coordinator.data.get("mode", self.PRESET_AUTO)
        mode_map = {
            0: self.PRESET_AUTO,
            1: self.PRESET_CONTINUOUS,
        }
        return mode_map.get(mode, self.PRESET_AUTO)

    async def async_set_mode(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        await self.coordinator.async_request_refresh()


class DuuxBeamMiniDehumidifier(DuuxHumidifier):
    """Duux Beam Mini Humidifier."""

    PRESET_AUTO = MODE_AUTO
    PRESET_MANUAL = MODE_NORMAL

    def __init__(self, coordinator, api, device):
        """Initialize the Beam Mini humidifier device."""
        super().__init__(coordinator, api, device)

        # min/max humidity settings for Beam Mini.
        self._attr_min_humidity = 20
        self._attr_max_humidity = 80

    @property
    def available_modes(self):
        """Return available preset modes."""
        return [self.PRESET_AUTO, self.PRESET_MANUAL]

    @property
    def mode(self):
        """Return current preset mode."""
        mode = self.coordinator.data.get("mode", self.PRESET_AUTO)
        mode_map = {
            0: self.PRESET_AUTO,
            1: self.PRESET_MANUAL,
        }
        return mode_map.get(mode, self.PRESET_AUTO)

    async def async_set_mode(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        await self.coordinator.async_request_refresh()
