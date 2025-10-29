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


from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Duux climate entities from a config entry."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]
    
    entities = []
    for device in coordinator.data:
        sensor_type_id = device.get("sensorTypeId")
        
        # Create the appropriate climate entity based on heater type
        if sensor_type_id == 49:  # Threesixty 2023
            entities.append(DuuxThreesixtyClimate(coordinator, device))
        elif sensor_type_id == 50:  # Edge heater v2
            entities.append(DuuxEdgeClimate(coordinator, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimate(coordinator, device))
            _LOGGER.warning(f"Unknown heater type {sensor_type_id}, using generic entity")
    
    async_add_entities(entities)


class DuuxClimate(ClimateEntity):
    """Representation of a Duux climate device."""

    def __init__(self, coordinator, device):
        """Initialize the climate device."""
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("name")
        
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
        data = self._get_device_data()
        if data and "latestData" in data and "fullData" in data["latestData"]:
            return data["latestData"]["fullData"].get("temp")
        return None

    @property
    def target_temperature(self):
        """Return the temperature we try to reach."""
        data = self._get_device_data()
        if data and "latestData" in data and "fullData" in data["latestData"]:
            return data["latestData"]["fullData"].get("sp")
        return None

    @property
    def hvac_mode(self):
        """Return current HVAC mode."""
        data = self._get_device_data()
        if data and "latestData" in data and "fullData" in data["latestData"]:
            power = data["latestData"]["fullData"].get("power")
            return HVACMode.HEAT if power == 1 else HVACMode.OFF
        return HVACMode.OFF

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
        
        api = self._coordinator.api
        await api.set_temperature(self._device_id, int(temperature))
        await self._coordinator.async_request_refresh()

    async def async_set_hvac_mode(self, hvac_mode):
        """Set new HVAC mode."""
        api = self._coordinator.api
        if hvac_mode == HVACMode.OFF:
            await api.set_power(self._device_id, "0")
        elif hvac_mode == HVACMode.HEAT:
            await api.set_power(self._device_id, "1")
        await self._coordinator.async_request_refresh()

    async def async_set_preset_mode(self, preset_mode):
        """Set preset mode."""
        # Base implementation - override in subclasses
        pass

    def _get_device_data(self):
        """Get the latest device data from coordinator."""
        for device in self._coordinator.data:
            if device["id"] == self._device_id:
                return device
        return None

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
    
    def __init__(self, coordinator, device):
        """Initialize the Threesixty climate device."""
        super().__init__(coordinator, device)
        # Temperature range for Threesixty
        self._attr_min_temp = 18
        self._attr_max_temp = 30
    
    @property
    def preset_modes(self):
        """Return available preset modes."""
        return [self.self.PRESET_LOW, self.PRESET_MID, self.PRESET_HIGH]
    
    @property
    def preset_mode(self):
        """Return current preset mode."""
        data = self._get_device_data()
        if data and "latestData" in data and "fullData" in data["latestData"]:
            mode = data["latestData"]["fullData"].get("mode")
            mode_map = {
                0: self.PRESET_LOW,
                1: self.PRESET_MID,
                2: self.PRESET_HIGH
            }
            return mode_map.get(mode, self.PRESET_LOW)
        return self.PRESET_LOW
    
    async def async_set_preset_mode(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "0",
            self.PRESET_MID: "1",
            self.PRESET_HIGH: "2"
        }
        if preset_mode in mode_map:
            api = self._coordinator.api
            await api.set_mode(self._device_id, mode_map[preset_mode])
            await self._coordinator.async_request_refresh()


class DuuxEdgeClimate(DuuxClimate):
    """Duux Edge heater v2."""
    PRESET_LOW = PRESET_ECO
    PRESET_BOOST = PRESET_BOOST
    PRESET_HIGH = PRESET_COMFORT

    def __init__(self, coordinator, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, device)
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
        data = self._get_device_data()
        if data and "latestData" in data and "fullData" in data["latestData"]:
            mode = data["latestData"]["fullData"].get("mode")
            mode_map = {
                0: self.PRESET_LOW,
                1: self.PRESET_HIGH,
                2: self.PRESET_BOOST
            }
            return mode_map.get(mode, self.PRESET_LOW)
        return self.PRESET_LOW
    
    async def async_set_preset_mode(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "0",
            self.PRESET_HIGH: "1",
            self.PRESET_BOOST: "2"
        }
        if preset_mode in mode_map:
            api = self._coordinator.api
            await api.set_mode(self._device_id, mode_map[preset_mode])
            await self._coordinator.async_request_refresh()