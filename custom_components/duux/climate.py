# custom_components/duux/climate.py

from homeassistant.components.climate import (
    ClimateEntity,
    ClimateEntityFeature,
    HVACMode,
    ECO,
    COMFORT,
    BOOST
)
from homeassistant.const import ATTR_TEMPERATURE, UnitOfTemperature
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN

PRESET_LOW = ECO
PRESET_BOOST = BOOST
PRESET_HIGH = COMFORT

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
        device_id = device["deviceId"]
        coordinator = coordinators[device_id]
        entities.append(DuuxClimate(coordinator, api, device))
    
    async_add_entities(entities)


class DuuxClimate(CoordinatorEntity, ClimateEntity):
    """Representation of a Duux Heater."""
    
    _attr_temperature_unit = UnitOfTemperature.CELSIUS
    _attr_hvac_modes = [HVACMode.HEAT, HVACMode.OFF]
    _attr_preset_modes = [PRESET_LOW, PRESET_HIGH, PRESET_BOOST]
    _attr_supported_features = (
        ClimateEntityFeature.TARGET_TEMPERATURE
        | ClimateEntityFeature.PRESET_MODE
        | ClimateEntityFeature.TURN_OFF
        | ClimateEntityFeature.TURN_ON
    )
    _attr_min_temp = 5
    _attr_max_temp = 36
    _attr_target_temperature_step = 1
    
    def __init__(self, coordinator, api, device):
        """Initialize the climate entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["deviceId"]
        self._device_mac = device["deviceId"]  # MAC address
        
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName", "Duux Heater")
        self._attr_device_info = {
            "identifiers": {(DOMAIN, self._device_id)},
            "name": self._attr_name,
            "manufacturer": device.get("manufacturer", "Duux"),
            "model": device.get("sensorType", {}).get("name", "Edge Heater"),
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
        """Return the current preset mode."""
        mode = self.coordinator.data.get("heatin", 0)
        if mode == 1:
            return PRESET_LOW
        elif mode == 2:
            return PRESET_HIGH
        elif mode == 3:
            return PRESET_BOOST
        else:
            return "UNKNOWN"
    
    async def async_set_hvac_mode(self, hvac_mode):
        """Set new target hvac mode."""
        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        await self.coordinator.async_request_refresh()
    
    async def async_set_temperature(self, **kwargs):
        """Set new target temperature."""
        temperature = kwargs.get(ATTR_TEMPERATURE)
        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, self._device_mac, temperature
            )
            await self.coordinator.async_request_refresh()
    
    async def async_set_preset_mode(self, preset_mode):
        """Set new preset mode."""
        mode_map = {
            PRESET_LOW: 1,
            PRESET_HIGH: 2,
            PRESET_BOOST: 3,
        }
        mode = mode_map.get(preset_mode, 1)
        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        await self.coordinator.async_request_refresh()
