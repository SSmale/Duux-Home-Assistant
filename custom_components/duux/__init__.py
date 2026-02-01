# custom_components/duux/__init__.py

import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.helpers import issue_registry as ir


from .const import (
    DOMAIN,
    DUUX_DTID_HEATER,
    DUUX_DTID_THERMOSTAT,
    DUUX_DTID_HUMIDIFIER,
    DUUX_DTID_OTHER_HEATER,
    DUUX_SUPPORTED_TYPES,
)
from .duux_api import DuuxAPI

_LOGGER = logging.getLogger(__name__)

PLATFORMS = [
    Platform.CLIMATE,
    Platform.HUMIDIFIER,
    Platform.SWITCH,
    Platform.SELECT,
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["password"])

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
        sensor_type_id = device.get("sensorTypeId")
        device_type_id = device.get("sensorType").get("type")
        google_type = device.get("sensorType").get("googleDeviceType")
        last_word = google_type.split(".")[-1]  # "HEATER" OR ""THERMOSTAT"
        device_name = device.get("displayName") or device.get("name")
        model = device.get("sensorType", {}).get("name", "Unknown")

        if device_type_id not in [
            *DUUX_DTID_HEATER,
            *DUUX_DTID_THERMOSTAT,
            *DUUX_DTID_HUMIDIFIER,
            *DUUX_DTID_OTHER_HEATER,
        ]:
            ir.async_create_issue(
                hass,
                DOMAIN,
                "device_not_recognised",
                is_fixable=False,
                severity=ir.IssueSeverity.WARNING,
                translation_key="device_not_recognised",
                learn_more_url=f"https://github.com/SSmale/Duux-Home-Assistant/issues/new?template=device_not_supported.yaml&title=Device+not+recognised+-+{model}&device_name={model}&device_type_id={device_type_id}&sensor_type_id={sensor_type_id}&reported_type={google_type}",
                translation_placeholders={
                    "device_name": model,
                    "device_type_id": device_type_id,
                    "sensor_type_id": sensor_type_id,
                    "reported_type": google_type,
                },
            )
            _LOGGER.warning("Your device has not been recognised.")
            _LOGGER.warning(
                f"It is classified as type {last_word}, so maybe loaded as such.",
            )
            _LOGGER.warning(
                "Please report this to the integration developer so they can update the supported device list.",
            )
            _LOGGER.warning(
                f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
            )
            if last_word in DUUX_SUPPORTED_TYPES:
                _LOGGER.warning(
                    f"Attempting to load device as type {last_word}.",
                )

            else:
                continue

        coordinator = DuuxDataUpdateCoordinator(
            hass,
            api=api,
            device_id=device.get("deviceId"),
            device_name=device_name,
        )

        await coordinator.async_config_entry_first_refresh()
        coordinators[device["deviceId"]] = coordinator

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "coordinators": coordinators,
        "devices": devices,
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
