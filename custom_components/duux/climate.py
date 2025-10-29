"""Support for Duux climate devices."""
import logging

from homeassistant.components.climate import (
    ClimateEntity
)
from homeassistant.components.climate.const import (
    ClimateEntityFeature,
    HVACMode,
    PRESET_BOOST, PRESET_COMFORT, PRESET_ECO,
)
from homeassistant.const import ATTR_TEMPERATURE, UnitOfTemperature
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN

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
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators[device_id]
        # Create the appropriate climate entity based on heater type
        if sensor_type_id == 49:  # Threesixty 2023
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == 50:  # Edge heater v2
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimate(coordinator, api, device))
            _LOGGER.warning(f"Unknown heater type {sensor_type_id}, using generic entity")
    
    async_add_entities(entities)


class DuuxClimate(CoordinatorEntity, ClimateEntity):
    """Representation of a Duux climate device."""

    def __init__(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
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
            ClimateEntityFeature.TARGET_TEMPERATURE | 
            ClimateEntityFeature.PRESET_MODE |
            ClimateEntityFeature.TURN_OFF |
            ClimateEntityFeature.TURN_ON
        )

    @property
    def device_info(self):
        """Return device information."""
        return {
            "identifiers": {(DOMAIN, str(self._device_id))},
            "name": self._attr_name,
            "manufacturer":  self._device.get("manufacturer", "Duux"),
            "model": self._device.get("sensorType", {}).get("name", "Unknown"),
        }

    @property
    def current_temperature(self):
        """Return the current temperature."""
        return self._coordinator.data.get("temp")

    @property
    def target_temperature(self):
        """Return the temperature we try to reach."""
        return self._coordinator.data.get("sp")

    @property
    def hvac_mode(self):
        """Return current operation."""
        power = self.coordinator.data.get("power", 0)
        return HVACMode.HEAT if power == 1 else HVACMode.OFF

    @property
    def preset_mode(self):
        """Return current preset mode."""
        # Base implementation - override in subclasses
        return str()

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
            await self._coordinator.async_request_refresh()

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
        await self._coordinator.async_request_refresh()

    async def async_set_preset_mode(self, preset_mode):
        """Set preset mode."""
        # Base implementation - override in subclasses
        pass

    @property
    def should_poll(self):
        """No need to poll, coordinator handles it."""
        return False

    @property
    def available(self):
        """Return if entity is available."""
        return self._coordinator.last_update_success

    async def async_added_to_hass(self):
        """When entity is added to hass."""
        self.async_on_remove(
            self._coordinator.async_add_listener(self.async_write_ha_state)
        )

    async def async_update(self):
        """Update the entity."""
        await self._coordinator.async_request_refresh()


class DuuxThreesixtyClimate(DuuxClimate):
    """Duux Threesixty 2023 heater."""
    # Preset constants
    PRESET_LOW = PRESET_ECO
    PRESET_HIGH = PRESET_BOOST
    PRESET_MID = PRESET_COMFORT
    
    def __init__(self, coordinator, api, device):
        """Initialize the Threesixty climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Threesixty
        self._attr_min_temp = 18
        self._attr_max_temp = 30
    
    @property
    def preset_modes(self):
        """Return available preset modes."""
        return [self.PRESET_LOW, self.PRESET_MID, self.PRESET_HIGH]
    
    @property
    def preset_mode(self):
        """Return current preset mode."""
        mode  = self._coordinator.data.get("mode")
        mode_map = {
            0: self.PRESET_LOW,
            1: self.PRESET_MID,
            2: self.PRESET_HIGH
        }
        return mode_map.get(mode, self.PRESET_LOW)
    
    async def async_set_preset_mode(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "0",
            self.PRESET_MID: "1",
            self.PRESET_HIGH: "2"
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        await self._coordinator.async_request_refresh()


class DuuxEdgeClimate(DuuxClimate):
    """Duux Edge heater v2."""
    PRESET_LOW = PRESET_ECO
    PRESET_BOOST = PRESET_BOOST
    PRESET_HIGH = PRESET_COMFORT

    def __init__(self, coordinator, api,device):
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
        mode = self._coordinator.data.get("heatin")
        mode_map = {
            1: self.PRESET_LOW,
            2: self.PRESET_HIGH,
            3: self.PRESET_BOOST
        }
        return mode_map.get(mode, self.PRESET_LOW)
    
    async def async_set_preset_mode(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
            self.PRESET_BOOST: "3"
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        await self._coordinator.async_request_refresh()