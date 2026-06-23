# custom_components/duux/__init__.py

import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import issue_registry as ir
from homeassistant.helpers.device_registry import DeviceEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    DOMAIN,
    DUUX_DTID_FAN,
    DUUX_DTID_HEATER,
    DUUX_DTID_HUMIDIFIER,
    DUUX_DTID_AIR_PURIFIER,
    DUUX_DTID_OTHER_HEATER,
    DUUX_DTID_THERMOSTAT,
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
    Platform.FAN,
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
        sensor_type = device.get("sensorType") or {}
        sensor_type_id = device.get("sensorTypeId")
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        device_name = device.get("displayName") or device.get("name")
        model = sensor_type.get("name", "Unknown")

        if device.get("connectionType") != "mqtt":
            _LOGGER.warning(
                f"Device {device_name} (ID: {device.get('deviceId')}) is not connected via MQTT. Some features may not work.",
            )
            ir.async_create_issue(
                hass,
                DOMAIN,
                "device_not_mqtt",
                is_fixable=False,
                severity=ir.IssueSeverity.WARNING,
                translation_key="device_not_mqtt",
                learn_more_url="https://github.com/SSmale/Duux-Home-Assistant/discussions/81",
                translation_placeholders={"device_name": model},
            )

        if device_type_id not in [
            *DUUX_DTID_HEATER,
            *DUUX_DTID_THERMOSTAT,
            *DUUX_DTID_HUMIDIFIER,
            *DUUX_DTID_AIR_PURIFIER,
            *DUUX_DTID_OTHER_HEATER,
            *DUUX_DTID_FAN,
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
                    "device_type_id": str(device_type_id),
                    "sensor_type_id": str(sensor_type_id),
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
            # config_entry=entry,
            api=api,
            device_id=device.get("deviceId"),
            device_name=device_name,
            config_entry=entry,
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


async def async_remove_config_entry_device(
    hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry
) -> bool:
    """Remove a config entry from a device."""
    # Get the entity registry
    entity_registry = er.async_get(hass)

    # Get all entities for this config entry
    entities = er.async_entries_for_config_entry(entity_registry, config_entry.entry_id)

    # Filter entities for this specific device
    device_entities = [
        entity for entity in entities if entity.device_id == device_entry.id
    ]

    for entity in device_entities:
        _LOGGER.debug(
            f"Removing entity {entity.entity_id} for device {device_entry.id}"
        )
        entity_registry.async_remove(entity.entity_id)

    entities = er.async_entries_for_config_entry(entity_registry, config_entry.entry_id)

    # Filter entities for this specific device
    device_entities = [
        entity for entity in entities if entity.device_id == device_entry.id
    ]
    # Allow removal only if no entities remain for this device
    return len(device_entities) == 0


class DuuxDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Duux data."""

    def __init__(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name
        super().__init__(
            hass,
            _LOGGER,
            # config_entry=config_entry,
            name=f"Duux {device_name}",
            update_interval=timedelta(seconds=30),
            config_entry=config_entry,
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
