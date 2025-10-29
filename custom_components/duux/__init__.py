# custom_components/duux/__init__.py

import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN
from .duux_api import DuuxAPI

_LOGGER = logging.getLogger(__name__)

PLATFORMS = [Platform.CLIMATE, Platform.SWITCH]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(
        email=entry.data["email"],
        password=entry.data["password"]
    )
    
    # Authenticate
    if not await hass.async_add_executor_job(api.login):
        _LOGGER.error("Failed to authenticate with Duux API")
        return False
    
    # Get devices
    devices = await hass.async_add_executor_job(api.get_devices)
    if not devices:
        _LOGGER.error("No Duux devices found")
        return False
    
    # Create coordinator for each device
    coordinators = {}
    for device in devices:
        coordinator = DuuxDataUpdateCoordinator(
            hass,
            api=api,
            device_id=device.get("deviceId"),
            device_name=device.get("displayName", "Duux Heater")
        )
        
        await coordinator.async_config_entry_first_refresh()
        coordinators[device["deviceId"]] = coordinator
    
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "coordinators": coordinators,
        "devices": devices
    }
    
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    
    return unload_ok


class DuuxDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Duux data."""
    
    def __init__(self, hass, api, device_id, device_name):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name
        
        super().__init__(
            hass,
            _LOGGER,
            name=f"Duux {device_name}",
            update_interval=timedelta(seconds=30),
        )
    
    async def _async_update_data(self):
        """Fetch data from API."""
        try:
            data = await self.hass.async_add_executor_job(
                self.api.get_device_status, self.device_id
            )
            return data
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")