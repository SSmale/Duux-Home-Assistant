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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_async_setup_entry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_async_setup_entry__mutmut)
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


async def x_async_setup_entry__mutmut_orig(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_1(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = None

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


async def x_async_setup_entry__mutmut_2(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=None, password=entry.data["password"])

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


async def x_async_setup_entry__mutmut_3(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=None)

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


async def x_async_setup_entry__mutmut_4(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(password=entry.data["password"])

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


async def x_async_setup_entry__mutmut_5(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], )

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


async def x_async_setup_entry__mutmut_6(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["XXemailXX"], password=entry.data["password"])

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


async def x_async_setup_entry__mutmut_7(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["EMAIL"], password=entry.data["password"])

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


async def x_async_setup_entry__mutmut_8(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["XXpasswordXX"])

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


async def x_async_setup_entry__mutmut_9(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["PASSWORD"])

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


async def x_async_setup_entry__mutmut_10(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["password"])

    # Authenticate
    if await hass.async_add_executor_job(api.login):
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


async def x_async_setup_entry__mutmut_11(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["password"])

    # Authenticate
    if not await hass.async_add_executor_job(None):
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


async def x_async_setup_entry__mutmut_12(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["password"])

    # Authenticate
    if not await hass.async_add_executor_job(api.login):
        _LOGGER.error(None)
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


async def x_async_setup_entry__mutmut_13(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["password"])

    # Authenticate
    if not await hass.async_add_executor_job(api.login):
        _LOGGER.error("XXFailed to authenticate with Duux APIXX")
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


async def x_async_setup_entry__mutmut_14(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["password"])

    # Authenticate
    if not await hass.async_add_executor_job(api.login):
        _LOGGER.error("failed to authenticate with duux api")
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


async def x_async_setup_entry__mutmut_15(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["password"])

    # Authenticate
    if not await hass.async_add_executor_job(api.login):
        _LOGGER.error("FAILED TO AUTHENTICATE WITH DUUX API")
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


async def x_async_setup_entry__mutmut_16(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["password"])

    # Authenticate
    if not await hass.async_add_executor_job(api.login):
        _LOGGER.error("Failed to authenticate with Duux API")
        return True

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


async def x_async_setup_entry__mutmut_17(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["password"])

    # Authenticate
    if not await hass.async_add_executor_job(api.login):
        _LOGGER.error("Failed to authenticate with Duux API")
        return False

    # Get devices
    devices = None
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


async def x_async_setup_entry__mutmut_18(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["password"])

    # Authenticate
    if not await hass.async_add_executor_job(api.login):
        _LOGGER.error("Failed to authenticate with Duux API")
        return False

    # Get devices
    devices = await hass.async_add_executor_job(None)
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


async def x_async_setup_entry__mutmut_19(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["password"])

    # Authenticate
    if not await hass.async_add_executor_job(api.login):
        _LOGGER.error("Failed to authenticate with Duux API")
        return False

    # Get devices
    devices = await hass.async_add_executor_job(api.get_devices)
    if devices:
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


async def x_async_setup_entry__mutmut_20(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["password"])

    # Authenticate
    if not await hass.async_add_executor_job(api.login):
        _LOGGER.error("Failed to authenticate with Duux API")
        return False

    # Get devices
    devices = await hass.async_add_executor_job(api.get_devices)
    if not devices:
        _LOGGER.error(None)
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


async def x_async_setup_entry__mutmut_21(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["password"])

    # Authenticate
    if not await hass.async_add_executor_job(api.login):
        _LOGGER.error("Failed to authenticate with Duux API")
        return False

    # Get devices
    devices = await hass.async_add_executor_job(api.get_devices)
    if not devices:
        _LOGGER.error("XXNo Duux devices foundXX")
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


async def x_async_setup_entry__mutmut_22(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["password"])

    # Authenticate
    if not await hass.async_add_executor_job(api.login):
        _LOGGER.error("Failed to authenticate with Duux API")
        return False

    # Get devices
    devices = await hass.async_add_executor_job(api.get_devices)
    if not devices:
        _LOGGER.error("no duux devices found")
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


async def x_async_setup_entry__mutmut_23(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"], password=entry.data["password"])

    # Authenticate
    if not await hass.async_add_executor_job(api.login):
        _LOGGER.error("Failed to authenticate with Duux API")
        return False

    # Get devices
    devices = await hass.async_add_executor_job(api.get_devices)
    if not devices:
        _LOGGER.error("NO DUUX DEVICES FOUND")
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


async def x_async_setup_entry__mutmut_24(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        return True

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


async def x_async_setup_entry__mutmut_25(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
    coordinators = None
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


async def x_async_setup_entry__mutmut_26(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        sensor_type = None
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


async def x_async_setup_entry__mutmut_27(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        sensor_type = device.get("sensorType") and {}
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


async def x_async_setup_entry__mutmut_28(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        sensor_type = device.get(None) or {}
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


async def x_async_setup_entry__mutmut_29(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        sensor_type = device.get("XXsensorTypeXX") or {}
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


async def x_async_setup_entry__mutmut_30(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        sensor_type = device.get("sensortype") or {}
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


async def x_async_setup_entry__mutmut_31(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        sensor_type = device.get("SENSORTYPE") or {}
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


async def x_async_setup_entry__mutmut_32(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        sensor_type_id = None
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


async def x_async_setup_entry__mutmut_33(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        sensor_type_id = device.get(None)
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


async def x_async_setup_entry__mutmut_34(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        sensor_type_id = device.get("XXsensorTypeIdXX")
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


async def x_async_setup_entry__mutmut_35(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        sensor_type_id = device.get("sensortypeid")
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


async def x_async_setup_entry__mutmut_36(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        sensor_type_id = device.get("SENSORTYPEID")
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


async def x_async_setup_entry__mutmut_37(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        device_type_id = None
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


async def x_async_setup_entry__mutmut_38(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        device_type_id = sensor_type.get(None)
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


async def x_async_setup_entry__mutmut_39(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        device_type_id = sensor_type.get("XXtypeXX")
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


async def x_async_setup_entry__mutmut_40(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        device_type_id = sensor_type.get("TYPE")
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


async def x_async_setup_entry__mutmut_41(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        google_type = None
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


async def x_async_setup_entry__mutmut_42(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        google_type = sensor_type.get("googleDeviceType") and ""
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


async def x_async_setup_entry__mutmut_43(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        google_type = sensor_type.get(None) or ""
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


async def x_async_setup_entry__mutmut_44(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        google_type = sensor_type.get("XXgoogleDeviceTypeXX") or ""
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


async def x_async_setup_entry__mutmut_45(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        google_type = sensor_type.get("googledevicetype") or ""
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


async def x_async_setup_entry__mutmut_46(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        google_type = sensor_type.get("GOOGLEDEVICETYPE") or ""
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


async def x_async_setup_entry__mutmut_47(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        google_type = sensor_type.get("googleDeviceType") or "XXXX"
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


async def x_async_setup_entry__mutmut_48(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        last_word = None  # "HEATER" OR "THERMOSTAT"
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


async def x_async_setup_entry__mutmut_49(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            google_type.split(None)[-1] if google_type else ""
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


async def x_async_setup_entry__mutmut_50(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            google_type.split("XX.XX")[-1] if google_type else ""
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


async def x_async_setup_entry__mutmut_51(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            google_type.split(".")[+1] if google_type else ""
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


async def x_async_setup_entry__mutmut_52(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            google_type.split(".")[-2] if google_type else ""
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


async def x_async_setup_entry__mutmut_53(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            google_type.split(".")[-1] if google_type else "XXXX"
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


async def x_async_setup_entry__mutmut_54(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        device_name = None
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


async def x_async_setup_entry__mutmut_55(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        device_name = device.get("displayName") and device.get("name")
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


async def x_async_setup_entry__mutmut_56(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        device_name = device.get(None) or device.get("name")
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


async def x_async_setup_entry__mutmut_57(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        device_name = device.get("XXdisplayNameXX") or device.get("name")
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


async def x_async_setup_entry__mutmut_58(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        device_name = device.get("displayname") or device.get("name")
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


async def x_async_setup_entry__mutmut_59(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        device_name = device.get("DISPLAYNAME") or device.get("name")
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


async def x_async_setup_entry__mutmut_60(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        device_name = device.get("displayName") or device.get(None)
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


async def x_async_setup_entry__mutmut_61(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        device_name = device.get("displayName") or device.get("XXnameXX")
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


async def x_async_setup_entry__mutmut_62(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        device_name = device.get("displayName") or device.get("NAME")
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


async def x_async_setup_entry__mutmut_63(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        model = None

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


async def x_async_setup_entry__mutmut_64(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        model = sensor_type.get(None, "Unknown")

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


async def x_async_setup_entry__mutmut_65(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        model = sensor_type.get("name", None)

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


async def x_async_setup_entry__mutmut_66(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        model = sensor_type.get("Unknown")

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


async def x_async_setup_entry__mutmut_67(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        model = sensor_type.get("name", )

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


async def x_async_setup_entry__mutmut_68(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        model = sensor_type.get("XXnameXX", "Unknown")

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


async def x_async_setup_entry__mutmut_69(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        model = sensor_type.get("NAME", "Unknown")

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


async def x_async_setup_entry__mutmut_70(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        model = sensor_type.get("name", "XXUnknownXX")

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


async def x_async_setup_entry__mutmut_71(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        model = sensor_type.get("name", "unknown")

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


async def x_async_setup_entry__mutmut_72(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        model = sensor_type.get("name", "UNKNOWN")

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


async def x_async_setup_entry__mutmut_73(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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

        if device.get(None) != "mqtt":
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


async def x_async_setup_entry__mutmut_74(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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

        if device.get("XXconnectionTypeXX") != "mqtt":
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


async def x_async_setup_entry__mutmut_75(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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

        if device.get("connectiontype") != "mqtt":
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


async def x_async_setup_entry__mutmut_76(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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

        if device.get("CONNECTIONTYPE") != "mqtt":
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


async def x_async_setup_entry__mutmut_77(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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

        if device.get("connectionType") == "mqtt":
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


async def x_async_setup_entry__mutmut_78(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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

        if device.get("connectionType") != "XXmqttXX":
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


async def x_async_setup_entry__mutmut_79(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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

        if device.get("connectionType") != "MQTT":
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


async def x_async_setup_entry__mutmut_80(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                None,
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


async def x_async_setup_entry__mutmut_81(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                f"Device {device_name} (ID: {device.get(None)}) is not connected via MQTT. Some features may not work.",
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


async def x_async_setup_entry__mutmut_82(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                f"Device {device_name} (ID: {device.get('XXdeviceIdXX')}) is not connected via MQTT. Some features may not work.",
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


async def x_async_setup_entry__mutmut_83(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                f"Device {device_name} (ID: {device.get('deviceid')}) is not connected via MQTT. Some features may not work.",
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


async def x_async_setup_entry__mutmut_84(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                f"Device {device_name} (ID: {device.get('DEVICEID')}) is not connected via MQTT. Some features may not work.",
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


async def x_async_setup_entry__mutmut_85(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                None,
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


async def x_async_setup_entry__mutmut_86(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                None,
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


async def x_async_setup_entry__mutmut_87(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                None,
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


async def x_async_setup_entry__mutmut_88(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                is_fixable=None,
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


async def x_async_setup_entry__mutmut_89(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                severity=None,
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


async def x_async_setup_entry__mutmut_90(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                translation_key=None,
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


async def x_async_setup_entry__mutmut_91(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                learn_more_url=None,
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


async def x_async_setup_entry__mutmut_92(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                translation_placeholders=None,
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


async def x_async_setup_entry__mutmut_93(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_94(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_95(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_96(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_97(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_98(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_99(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_100(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_101(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                "XXdevice_not_mqttXX",
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


async def x_async_setup_entry__mutmut_102(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                "DEVICE_NOT_MQTT",
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


async def x_async_setup_entry__mutmut_103(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                is_fixable=True,
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


async def x_async_setup_entry__mutmut_104(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                translation_key="XXdevice_not_mqttXX",
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


async def x_async_setup_entry__mutmut_105(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                translation_key="DEVICE_NOT_MQTT",
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


async def x_async_setup_entry__mutmut_106(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                learn_more_url="XXhttps://github.com/SSmale/Duux-Home-Assistant/discussions/81XX",
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


async def x_async_setup_entry__mutmut_107(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                learn_more_url="https://github.com/ssmale/duux-home-assistant/discussions/81",
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


async def x_async_setup_entry__mutmut_108(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                learn_more_url="HTTPS://GITHUB.COM/SSMALE/DUUX-HOME-ASSISTANT/DISCUSSIONS/81",
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


async def x_async_setup_entry__mutmut_109(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                translation_placeholders={"XXdevice_nameXX": model},
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


async def x_async_setup_entry__mutmut_110(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                translation_placeholders={"DEVICE_NAME": model},
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


async def x_async_setup_entry__mutmut_111(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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

        if device_type_id in [
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


async def x_async_setup_entry__mutmut_112(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                None,
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


async def x_async_setup_entry__mutmut_113(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                None,
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


async def x_async_setup_entry__mutmut_114(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                None,
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


async def x_async_setup_entry__mutmut_115(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                is_fixable=None,
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


async def x_async_setup_entry__mutmut_116(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                severity=None,
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


async def x_async_setup_entry__mutmut_117(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                translation_key=None,
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


async def x_async_setup_entry__mutmut_118(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                learn_more_url=None,
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


async def x_async_setup_entry__mutmut_119(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                translation_placeholders=None,
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


async def x_async_setup_entry__mutmut_120(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_121(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_122(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_123(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_124(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_125(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_126(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_127(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_128(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                "XXdevice_not_recognisedXX",
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


async def x_async_setup_entry__mutmut_129(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                "DEVICE_NOT_RECOGNISED",
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


async def x_async_setup_entry__mutmut_130(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                is_fixable=True,
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


async def x_async_setup_entry__mutmut_131(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                translation_key="XXdevice_not_recognisedXX",
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


async def x_async_setup_entry__mutmut_132(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                translation_key="DEVICE_NOT_RECOGNISED",
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


async def x_async_setup_entry__mutmut_133(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                    "XXdevice_nameXX": model,
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


async def x_async_setup_entry__mutmut_134(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                    "DEVICE_NAME": model,
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


async def x_async_setup_entry__mutmut_135(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                    "XXdevice_type_idXX": str(device_type_id),
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


async def x_async_setup_entry__mutmut_136(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                    "DEVICE_TYPE_ID": str(device_type_id),
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


async def x_async_setup_entry__mutmut_137(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                    "device_type_id": str(None),
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


async def x_async_setup_entry__mutmut_138(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                    "XXsensor_type_idXX": str(sensor_type_id),
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


async def x_async_setup_entry__mutmut_139(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                    "SENSOR_TYPE_ID": str(sensor_type_id),
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


async def x_async_setup_entry__mutmut_140(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                    "sensor_type_id": str(None),
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


async def x_async_setup_entry__mutmut_141(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                    "XXreported_typeXX": google_type,
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


async def x_async_setup_entry__mutmut_142(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                    "REPORTED_TYPE": google_type,
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


async def x_async_setup_entry__mutmut_143(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            _LOGGER.warning(None)
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


async def x_async_setup_entry__mutmut_144(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            _LOGGER.warning("XXYour device has not been recognised.XX")
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


async def x_async_setup_entry__mutmut_145(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            _LOGGER.warning("your device has not been recognised.")
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


async def x_async_setup_entry__mutmut_146(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            _LOGGER.warning("YOUR DEVICE HAS NOT BEEN RECOGNISED.")
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


async def x_async_setup_entry__mutmut_147(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                None,
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


async def x_async_setup_entry__mutmut_148(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                None,
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


async def x_async_setup_entry__mutmut_149(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                "XXPlease report this to the integration developer so they can update the supported device list.XX",
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


async def x_async_setup_entry__mutmut_150(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                "please report this to the integration developer so they can update the supported device list.",
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


async def x_async_setup_entry__mutmut_151(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                "PLEASE REPORT THIS TO THE INTEGRATION DEVELOPER SO THEY CAN UPDATE THE SUPPORTED DEVICE LIST.",
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


async def x_async_setup_entry__mutmut_152(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                None,
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


async def x_async_setup_entry__mutmut_153(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            if last_word not in DUUX_SUPPORTED_TYPES:
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


async def x_async_setup_entry__mutmut_154(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                    None,
                )

            else:
                continue

        coordinator = DuuxDataUpdateCoordinator(
            hass,
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


async def x_async_setup_entry__mutmut_155(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
                break

        coordinator = DuuxDataUpdateCoordinator(
            hass,
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


async def x_async_setup_entry__mutmut_156(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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

        coordinator = None

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


async def x_async_setup_entry__mutmut_157(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            None,
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


async def x_async_setup_entry__mutmut_158(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=None,
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


async def x_async_setup_entry__mutmut_159(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=None,
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


async def x_async_setup_entry__mutmut_160(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("deviceId"),
            device_name=None,
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


async def x_async_setup_entry__mutmut_161(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("deviceId"),
            device_name=device_name,
            config_entry=None,
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


async def x_async_setup_entry__mutmut_162(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_163(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_164(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
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


async def x_async_setup_entry__mutmut_165(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("deviceId"),
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


async def x_async_setup_entry__mutmut_166(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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


async def x_async_setup_entry__mutmut_167(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get(None),
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


async def x_async_setup_entry__mutmut_168(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("XXdeviceIdXX"),
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


async def x_async_setup_entry__mutmut_169(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("deviceid"),
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


async def x_async_setup_entry__mutmut_170(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("DEVICEID"),
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


async def x_async_setup_entry__mutmut_171(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("deviceId"),
            device_name=device_name,
            config_entry=entry,
        )

        await coordinator.async_config_entry_first_refresh()
        coordinators[device["deviceId"]] = None

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "coordinators": coordinators,
        "devices": devices,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_172(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("deviceId"),
            device_name=device_name,
            config_entry=entry,
        )

        await coordinator.async_config_entry_first_refresh()
        coordinators[device["XXdeviceIdXX"]] = coordinator

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "coordinators": coordinators,
        "devices": devices,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_173(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("deviceId"),
            device_name=device_name,
            config_entry=entry,
        )

        await coordinator.async_config_entry_first_refresh()
        coordinators[device["deviceid"]] = coordinator

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "coordinators": coordinators,
        "devices": devices,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_174(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("deviceId"),
            device_name=device_name,
            config_entry=entry,
        )

        await coordinator.async_config_entry_first_refresh()
        coordinators[device["DEVICEID"]] = coordinator

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "coordinators": coordinators,
        "devices": devices,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_175(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("deviceId"),
            device_name=device_name,
            config_entry=entry,
        )

        await coordinator.async_config_entry_first_refresh()
        coordinators[device["deviceId"]] = coordinator

    hass.data.setdefault(None, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "coordinators": coordinators,
        "devices": devices,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_176(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("deviceId"),
            device_name=device_name,
            config_entry=entry,
        )

        await coordinator.async_config_entry_first_refresh()
        coordinators[device["deviceId"]] = coordinator

    hass.data.setdefault(DOMAIN, None)
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "coordinators": coordinators,
        "devices": devices,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_177(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("deviceId"),
            device_name=device_name,
            config_entry=entry,
        )

        await coordinator.async_config_entry_first_refresh()
        coordinators[device["deviceId"]] = coordinator

    hass.data.setdefault({})
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "coordinators": coordinators,
        "devices": devices,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_178(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("deviceId"),
            device_name=device_name,
            config_entry=entry,
        )

        await coordinator.async_config_entry_first_refresh()
        coordinators[device["deviceId"]] = coordinator

    hass.data.setdefault(DOMAIN, )
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "coordinators": coordinators,
        "devices": devices,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_179(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("deviceId"),
            device_name=device_name,
            config_entry=entry,
        )

        await coordinator.async_config_entry_first_refresh()
        coordinators[device["deviceId"]] = coordinator

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = None

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_180(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("deviceId"),
            device_name=device_name,
            config_entry=entry,
        )

        await coordinator.async_config_entry_first_refresh()
        coordinators[device["deviceId"]] = coordinator

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "XXapiXX": api,
        "coordinators": coordinators,
        "devices": devices,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_181(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
            api=api,
            device_id=device.get("deviceId"),
            device_name=device_name,
            config_entry=entry,
        )

        await coordinator.async_config_entry_first_refresh()
        coordinators[device["deviceId"]] = coordinator

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "API": api,
        "coordinators": coordinators,
        "devices": devices,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_182(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        "XXcoordinatorsXX": coordinators,
        "devices": devices,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_183(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        "COORDINATORS": coordinators,
        "devices": devices,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_184(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        "XXdevicesXX": devices,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_185(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
        "DEVICES": devices,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_186(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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

    await hass.config_entries.async_forward_entry_setups(None, PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_187(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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

    await hass.config_entries.async_forward_entry_setups(entry, None)
    return True


async def x_async_setup_entry__mutmut_188(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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

    await hass.config_entries.async_forward_entry_setups(PLATFORMS)
    return True


async def x_async_setup_entry__mutmut_189(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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

    await hass.config_entries.async_forward_entry_setups(entry, )
    return True


async def x_async_setup_entry__mutmut_190(hass: HomeAssistant, entry: ConfigEntry) -> bool:
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
    return False

mutants_x_async_setup_entry__mutmut['_mutmut_orig'] = x_async_setup_entry__mutmut_orig # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_1'] = x_async_setup_entry__mutmut_1 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_2'] = x_async_setup_entry__mutmut_2 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_3'] = x_async_setup_entry__mutmut_3 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_4'] = x_async_setup_entry__mutmut_4 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_5'] = x_async_setup_entry__mutmut_5 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_6'] = x_async_setup_entry__mutmut_6 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_7'] = x_async_setup_entry__mutmut_7 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_8'] = x_async_setup_entry__mutmut_8 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_9'] = x_async_setup_entry__mutmut_9 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_10'] = x_async_setup_entry__mutmut_10 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_11'] = x_async_setup_entry__mutmut_11 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_12'] = x_async_setup_entry__mutmut_12 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_13'] = x_async_setup_entry__mutmut_13 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_14'] = x_async_setup_entry__mutmut_14 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_15'] = x_async_setup_entry__mutmut_15 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_16'] = x_async_setup_entry__mutmut_16 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_17'] = x_async_setup_entry__mutmut_17 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_18'] = x_async_setup_entry__mutmut_18 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_19'] = x_async_setup_entry__mutmut_19 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_20'] = x_async_setup_entry__mutmut_20 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_21'] = x_async_setup_entry__mutmut_21 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_22'] = x_async_setup_entry__mutmut_22 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_23'] = x_async_setup_entry__mutmut_23 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_24'] = x_async_setup_entry__mutmut_24 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_25'] = x_async_setup_entry__mutmut_25 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_26'] = x_async_setup_entry__mutmut_26 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_27'] = x_async_setup_entry__mutmut_27 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_28'] = x_async_setup_entry__mutmut_28 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_29'] = x_async_setup_entry__mutmut_29 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_30'] = x_async_setup_entry__mutmut_30 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_31'] = x_async_setup_entry__mutmut_31 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_32'] = x_async_setup_entry__mutmut_32 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_33'] = x_async_setup_entry__mutmut_33 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_34'] = x_async_setup_entry__mutmut_34 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_35'] = x_async_setup_entry__mutmut_35 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_36'] = x_async_setup_entry__mutmut_36 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_37'] = x_async_setup_entry__mutmut_37 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_38'] = x_async_setup_entry__mutmut_38 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_39'] = x_async_setup_entry__mutmut_39 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_40'] = x_async_setup_entry__mutmut_40 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_41'] = x_async_setup_entry__mutmut_41 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_42'] = x_async_setup_entry__mutmut_42 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_43'] = x_async_setup_entry__mutmut_43 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_44'] = x_async_setup_entry__mutmut_44 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_45'] = x_async_setup_entry__mutmut_45 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_46'] = x_async_setup_entry__mutmut_46 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_47'] = x_async_setup_entry__mutmut_47 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_48'] = x_async_setup_entry__mutmut_48 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_49'] = x_async_setup_entry__mutmut_49 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_50'] = x_async_setup_entry__mutmut_50 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_51'] = x_async_setup_entry__mutmut_51 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_52'] = x_async_setup_entry__mutmut_52 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_53'] = x_async_setup_entry__mutmut_53 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_54'] = x_async_setup_entry__mutmut_54 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_55'] = x_async_setup_entry__mutmut_55 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_56'] = x_async_setup_entry__mutmut_56 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_57'] = x_async_setup_entry__mutmut_57 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_58'] = x_async_setup_entry__mutmut_58 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_59'] = x_async_setup_entry__mutmut_59 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_60'] = x_async_setup_entry__mutmut_60 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_61'] = x_async_setup_entry__mutmut_61 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_62'] = x_async_setup_entry__mutmut_62 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_63'] = x_async_setup_entry__mutmut_63 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_64'] = x_async_setup_entry__mutmut_64 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_65'] = x_async_setup_entry__mutmut_65 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_66'] = x_async_setup_entry__mutmut_66 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_67'] = x_async_setup_entry__mutmut_67 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_68'] = x_async_setup_entry__mutmut_68 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_69'] = x_async_setup_entry__mutmut_69 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_70'] = x_async_setup_entry__mutmut_70 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_71'] = x_async_setup_entry__mutmut_71 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_72'] = x_async_setup_entry__mutmut_72 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_73'] = x_async_setup_entry__mutmut_73 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_74'] = x_async_setup_entry__mutmut_74 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_75'] = x_async_setup_entry__mutmut_75 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_76'] = x_async_setup_entry__mutmut_76 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_77'] = x_async_setup_entry__mutmut_77 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_78'] = x_async_setup_entry__mutmut_78 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_79'] = x_async_setup_entry__mutmut_79 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_80'] = x_async_setup_entry__mutmut_80 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_81'] = x_async_setup_entry__mutmut_81 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_82'] = x_async_setup_entry__mutmut_82 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_83'] = x_async_setup_entry__mutmut_83 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_84'] = x_async_setup_entry__mutmut_84 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_85'] = x_async_setup_entry__mutmut_85 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_86'] = x_async_setup_entry__mutmut_86 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_87'] = x_async_setup_entry__mutmut_87 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_88'] = x_async_setup_entry__mutmut_88 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_89'] = x_async_setup_entry__mutmut_89 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_90'] = x_async_setup_entry__mutmut_90 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_91'] = x_async_setup_entry__mutmut_91 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_92'] = x_async_setup_entry__mutmut_92 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_93'] = x_async_setup_entry__mutmut_93 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_94'] = x_async_setup_entry__mutmut_94 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_95'] = x_async_setup_entry__mutmut_95 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_96'] = x_async_setup_entry__mutmut_96 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_97'] = x_async_setup_entry__mutmut_97 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_98'] = x_async_setup_entry__mutmut_98 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_99'] = x_async_setup_entry__mutmut_99 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_100'] = x_async_setup_entry__mutmut_100 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_101'] = x_async_setup_entry__mutmut_101 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_102'] = x_async_setup_entry__mutmut_102 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_103'] = x_async_setup_entry__mutmut_103 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_104'] = x_async_setup_entry__mutmut_104 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_105'] = x_async_setup_entry__mutmut_105 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_106'] = x_async_setup_entry__mutmut_106 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_107'] = x_async_setup_entry__mutmut_107 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_108'] = x_async_setup_entry__mutmut_108 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_109'] = x_async_setup_entry__mutmut_109 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_110'] = x_async_setup_entry__mutmut_110 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_111'] = x_async_setup_entry__mutmut_111 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_112'] = x_async_setup_entry__mutmut_112 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_113'] = x_async_setup_entry__mutmut_113 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_114'] = x_async_setup_entry__mutmut_114 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_115'] = x_async_setup_entry__mutmut_115 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_116'] = x_async_setup_entry__mutmut_116 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_117'] = x_async_setup_entry__mutmut_117 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_118'] = x_async_setup_entry__mutmut_118 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_119'] = x_async_setup_entry__mutmut_119 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_120'] = x_async_setup_entry__mutmut_120 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_121'] = x_async_setup_entry__mutmut_121 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_122'] = x_async_setup_entry__mutmut_122 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_123'] = x_async_setup_entry__mutmut_123 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_124'] = x_async_setup_entry__mutmut_124 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_125'] = x_async_setup_entry__mutmut_125 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_126'] = x_async_setup_entry__mutmut_126 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_127'] = x_async_setup_entry__mutmut_127 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_128'] = x_async_setup_entry__mutmut_128 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_129'] = x_async_setup_entry__mutmut_129 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_130'] = x_async_setup_entry__mutmut_130 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_131'] = x_async_setup_entry__mutmut_131 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_132'] = x_async_setup_entry__mutmut_132 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_133'] = x_async_setup_entry__mutmut_133 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_134'] = x_async_setup_entry__mutmut_134 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_135'] = x_async_setup_entry__mutmut_135 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_136'] = x_async_setup_entry__mutmut_136 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_137'] = x_async_setup_entry__mutmut_137 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_138'] = x_async_setup_entry__mutmut_138 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_139'] = x_async_setup_entry__mutmut_139 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_140'] = x_async_setup_entry__mutmut_140 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_141'] = x_async_setup_entry__mutmut_141 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_142'] = x_async_setup_entry__mutmut_142 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_143'] = x_async_setup_entry__mutmut_143 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_144'] = x_async_setup_entry__mutmut_144 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_145'] = x_async_setup_entry__mutmut_145 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_146'] = x_async_setup_entry__mutmut_146 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_147'] = x_async_setup_entry__mutmut_147 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_148'] = x_async_setup_entry__mutmut_148 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_149'] = x_async_setup_entry__mutmut_149 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_150'] = x_async_setup_entry__mutmut_150 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_151'] = x_async_setup_entry__mutmut_151 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_152'] = x_async_setup_entry__mutmut_152 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_153'] = x_async_setup_entry__mutmut_153 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_154'] = x_async_setup_entry__mutmut_154 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_155'] = x_async_setup_entry__mutmut_155 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_156'] = x_async_setup_entry__mutmut_156 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_157'] = x_async_setup_entry__mutmut_157 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_158'] = x_async_setup_entry__mutmut_158 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_159'] = x_async_setup_entry__mutmut_159 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_160'] = x_async_setup_entry__mutmut_160 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_161'] = x_async_setup_entry__mutmut_161 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_162'] = x_async_setup_entry__mutmut_162 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_163'] = x_async_setup_entry__mutmut_163 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_164'] = x_async_setup_entry__mutmut_164 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_165'] = x_async_setup_entry__mutmut_165 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_166'] = x_async_setup_entry__mutmut_166 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_167'] = x_async_setup_entry__mutmut_167 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_168'] = x_async_setup_entry__mutmut_168 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_169'] = x_async_setup_entry__mutmut_169 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_170'] = x_async_setup_entry__mutmut_170 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_171'] = x_async_setup_entry__mutmut_171 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_172'] = x_async_setup_entry__mutmut_172 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_173'] = x_async_setup_entry__mutmut_173 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_174'] = x_async_setup_entry__mutmut_174 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_175'] = x_async_setup_entry__mutmut_175 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_176'] = x_async_setup_entry__mutmut_176 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_177'] = x_async_setup_entry__mutmut_177 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_178'] = x_async_setup_entry__mutmut_178 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_179'] = x_async_setup_entry__mutmut_179 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_180'] = x_async_setup_entry__mutmut_180 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_181'] = x_async_setup_entry__mutmut_181 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_182'] = x_async_setup_entry__mutmut_182 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_183'] = x_async_setup_entry__mutmut_183 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_184'] = x_async_setup_entry__mutmut_184 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_185'] = x_async_setup_entry__mutmut_185 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_186'] = x_async_setup_entry__mutmut_186 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_187'] = x_async_setup_entry__mutmut_187 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_188'] = x_async_setup_entry__mutmut_188 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_189'] = x_async_setup_entry__mutmut_189 # type: ignore # mutmut generated
mutants_x_async_setup_entry__mutmut['x_async_setup_entry__mutmut_190'] = x_async_setup_entry__mutmut_190 # type: ignore # mutmut generated
mutants_x_async_unload_entry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_async_unload_entry__mutmut)
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def x_async_unload_entry__mutmut_orig(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def x_async_unload_entry__mutmut_1(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = None

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def x_async_unload_entry__mutmut_2(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(None, PLATFORMS)

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def x_async_unload_entry__mutmut_3(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, None)

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def x_async_unload_entry__mutmut_4(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(PLATFORMS)

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def x_async_unload_entry__mutmut_5(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, )

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def x_async_unload_entry__mutmut_6(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        hass.data[DOMAIN].pop(None)

    return unload_ok

mutants_x_async_unload_entry__mutmut['_mutmut_orig'] = x_async_unload_entry__mutmut_orig # type: ignore # mutmut generated
mutants_x_async_unload_entry__mutmut['x_async_unload_entry__mutmut_1'] = x_async_unload_entry__mutmut_1 # type: ignore # mutmut generated
mutants_x_async_unload_entry__mutmut['x_async_unload_entry__mutmut_2'] = x_async_unload_entry__mutmut_2 # type: ignore # mutmut generated
mutants_x_async_unload_entry__mutmut['x_async_unload_entry__mutmut_3'] = x_async_unload_entry__mutmut_3 # type: ignore # mutmut generated
mutants_x_async_unload_entry__mutmut['x_async_unload_entry__mutmut_4'] = x_async_unload_entry__mutmut_4 # type: ignore # mutmut generated
mutants_x_async_unload_entry__mutmut['x_async_unload_entry__mutmut_5'] = x_async_unload_entry__mutmut_5 # type: ignore # mutmut generated
mutants_x_async_unload_entry__mutmut['x_async_unload_entry__mutmut_6'] = x_async_unload_entry__mutmut_6 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_async_remove_config_entry_device__mutmut)
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


async def x_async_remove_config_entry_device__mutmut_orig(
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


async def x_async_remove_config_entry_device__mutmut_1(
    hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry
) -> bool:
    """Remove a config entry from a device."""
    # Get the entity registry
    entity_registry = None

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


async def x_async_remove_config_entry_device__mutmut_2(
    hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry
) -> bool:
    """Remove a config entry from a device."""
    # Get the entity registry
    entity_registry = er.async_get(None)

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


async def x_async_remove_config_entry_device__mutmut_3(
    hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry
) -> bool:
    """Remove a config entry from a device."""
    # Get the entity registry
    entity_registry = er.async_get(hass)

    # Get all entities for this config entry
    entities = None

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


async def x_async_remove_config_entry_device__mutmut_4(
    hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry
) -> bool:
    """Remove a config entry from a device."""
    # Get the entity registry
    entity_registry = er.async_get(hass)

    # Get all entities for this config entry
    entities = er.async_entries_for_config_entry(None, config_entry.entry_id)

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


async def x_async_remove_config_entry_device__mutmut_5(
    hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry
) -> bool:
    """Remove a config entry from a device."""
    # Get the entity registry
    entity_registry = er.async_get(hass)

    # Get all entities for this config entry
    entities = er.async_entries_for_config_entry(entity_registry, None)

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


async def x_async_remove_config_entry_device__mutmut_6(
    hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry
) -> bool:
    """Remove a config entry from a device."""
    # Get the entity registry
    entity_registry = er.async_get(hass)

    # Get all entities for this config entry
    entities = er.async_entries_for_config_entry(config_entry.entry_id)

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


async def x_async_remove_config_entry_device__mutmut_7(
    hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry
) -> bool:
    """Remove a config entry from a device."""
    # Get the entity registry
    entity_registry = er.async_get(hass)

    # Get all entities for this config entry
    entities = er.async_entries_for_config_entry(entity_registry, )

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


async def x_async_remove_config_entry_device__mutmut_8(
    hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry
) -> bool:
    """Remove a config entry from a device."""
    # Get the entity registry
    entity_registry = er.async_get(hass)

    # Get all entities for this config entry
    entities = er.async_entries_for_config_entry(entity_registry, config_entry.entry_id)

    # Filter entities for this specific device
    device_entities = None

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


async def x_async_remove_config_entry_device__mutmut_9(
    hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry
) -> bool:
    """Remove a config entry from a device."""
    # Get the entity registry
    entity_registry = er.async_get(hass)

    # Get all entities for this config entry
    entities = er.async_entries_for_config_entry(entity_registry, config_entry.entry_id)

    # Filter entities for this specific device
    device_entities = [
        entity for entity in entities if entity.device_id != device_entry.id
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


async def x_async_remove_config_entry_device__mutmut_10(
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
            None
        )
        entity_registry.async_remove(entity.entity_id)

    entities = er.async_entries_for_config_entry(entity_registry, config_entry.entry_id)

    # Filter entities for this specific device
    device_entities = [
        entity for entity in entities if entity.device_id == device_entry.id
    ]
    # Allow removal only if no entities remain for this device
    return len(device_entities) == 0


async def x_async_remove_config_entry_device__mutmut_11(
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
        entity_registry.async_remove(None)

    entities = er.async_entries_for_config_entry(entity_registry, config_entry.entry_id)

    # Filter entities for this specific device
    device_entities = [
        entity for entity in entities if entity.device_id == device_entry.id
    ]
    # Allow removal only if no entities remain for this device
    return len(device_entities) == 0


async def x_async_remove_config_entry_device__mutmut_12(
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

    entities = None

    # Filter entities for this specific device
    device_entities = [
        entity for entity in entities if entity.device_id == device_entry.id
    ]
    # Allow removal only if no entities remain for this device
    return len(device_entities) == 0


async def x_async_remove_config_entry_device__mutmut_13(
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

    entities = er.async_entries_for_config_entry(None, config_entry.entry_id)

    # Filter entities for this specific device
    device_entities = [
        entity for entity in entities if entity.device_id == device_entry.id
    ]
    # Allow removal only if no entities remain for this device
    return len(device_entities) == 0


async def x_async_remove_config_entry_device__mutmut_14(
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

    entities = er.async_entries_for_config_entry(entity_registry, None)

    # Filter entities for this specific device
    device_entities = [
        entity for entity in entities if entity.device_id == device_entry.id
    ]
    # Allow removal only if no entities remain for this device
    return len(device_entities) == 0


async def x_async_remove_config_entry_device__mutmut_15(
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

    entities = er.async_entries_for_config_entry(config_entry.entry_id)

    # Filter entities for this specific device
    device_entities = [
        entity for entity in entities if entity.device_id == device_entry.id
    ]
    # Allow removal only if no entities remain for this device
    return len(device_entities) == 0


async def x_async_remove_config_entry_device__mutmut_16(
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

    entities = er.async_entries_for_config_entry(entity_registry, )

    # Filter entities for this specific device
    device_entities = [
        entity for entity in entities if entity.device_id == device_entry.id
    ]
    # Allow removal only if no entities remain for this device
    return len(device_entities) == 0


async def x_async_remove_config_entry_device__mutmut_17(
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
    device_entities = None
    # Allow removal only if no entities remain for this device
    return len(device_entities) == 0


async def x_async_remove_config_entry_device__mutmut_18(
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
        entity for entity in entities if entity.device_id != device_entry.id
    ]
    # Allow removal only if no entities remain for this device
    return len(device_entities) == 0


async def x_async_remove_config_entry_device__mutmut_19(
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
    return len(device_entities) != 0


async def x_async_remove_config_entry_device__mutmut_20(
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
    return len(device_entities) == 1

mutants_x_async_remove_config_entry_device__mutmut['_mutmut_orig'] = x_async_remove_config_entry_device__mutmut_orig # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_1'] = x_async_remove_config_entry_device__mutmut_1 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_2'] = x_async_remove_config_entry_device__mutmut_2 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_3'] = x_async_remove_config_entry_device__mutmut_3 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_4'] = x_async_remove_config_entry_device__mutmut_4 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_5'] = x_async_remove_config_entry_device__mutmut_5 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_6'] = x_async_remove_config_entry_device__mutmut_6 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_7'] = x_async_remove_config_entry_device__mutmut_7 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_8'] = x_async_remove_config_entry_device__mutmut_8 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_9'] = x_async_remove_config_entry_device__mutmut_9 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_10'] = x_async_remove_config_entry_device__mutmut_10 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_11'] = x_async_remove_config_entry_device__mutmut_11 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_12'] = x_async_remove_config_entry_device__mutmut_12 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_13'] = x_async_remove_config_entry_device__mutmut_13 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_14'] = x_async_remove_config_entry_device__mutmut_14 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_15'] = x_async_remove_config_entry_device__mutmut_15 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_16'] = x_async_remove_config_entry_device__mutmut_16 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_17'] = x_async_remove_config_entry_device__mutmut_17 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_18'] = x_async_remove_config_entry_device__mutmut_18 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_19'] = x_async_remove_config_entry_device__mutmut_19 # type: ignore # mutmut generated
mutants_x_async_remove_config_entry_device__mutmut['x_async_remove_config_entry_device__mutmut_20'] = x_async_remove_config_entry_device__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut: MutantDict = {}  # type: ignore


class DuuxDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Duux data."""

    @_mutmut_mutated(mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut)
    def __init__(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name

        super().__init__(
            hass,
            _LOGGER,
            name=f"Duux {device_name}",
            update_interval=timedelta(seconds=30),
            config_entry=config_entry,
        )

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_orig(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name

        super().__init__(
            hass,
            _LOGGER,
            name=f"Duux {device_name}",
            update_interval=timedelta(seconds=30),
            config_entry=config_entry,
        )

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_1(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = None
        self.device_id = device_id
        self.device_name = device_name

        super().__init__(
            hass,
            _LOGGER,
            name=f"Duux {device_name}",
            update_interval=timedelta(seconds=30),
            config_entry=config_entry,
        )

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_2(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = None
        self.device_name = device_name

        super().__init__(
            hass,
            _LOGGER,
            name=f"Duux {device_name}",
            update_interval=timedelta(seconds=30),
            config_entry=config_entry,
        )

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_3(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = None

        super().__init__(
            hass,
            _LOGGER,
            name=f"Duux {device_name}",
            update_interval=timedelta(seconds=30),
            config_entry=config_entry,
        )

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_4(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name

        super().__init__(
            None,
            _LOGGER,
            name=f"Duux {device_name}",
            update_interval=timedelta(seconds=30),
            config_entry=config_entry,
        )

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_5(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name

        super().__init__(
            hass,
            None,
            name=f"Duux {device_name}",
            update_interval=timedelta(seconds=30),
            config_entry=config_entry,
        )

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_6(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name

        super().__init__(
            hass,
            _LOGGER,
            name=None,
            update_interval=timedelta(seconds=30),
            config_entry=config_entry,
        )

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_7(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name

        super().__init__(
            hass,
            _LOGGER,
            name=f"Duux {device_name}",
            update_interval=None,
            config_entry=config_entry,
        )

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_8(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name

        super().__init__(
            hass,
            _LOGGER,
            name=f"Duux {device_name}",
            update_interval=timedelta(seconds=30),
            config_entry=None,
        )

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_9(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name

        super().__init__(
            _LOGGER,
            name=f"Duux {device_name}",
            update_interval=timedelta(seconds=30),
            config_entry=config_entry,
        )

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_10(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name

        super().__init__(
            hass,
            name=f"Duux {device_name}",
            update_interval=timedelta(seconds=30),
            config_entry=config_entry,
        )

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_11(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name

        super().__init__(
            hass,
            _LOGGER,
            update_interval=timedelta(seconds=30),
            config_entry=config_entry,
        )

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_12(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name

        super().__init__(
            hass,
            _LOGGER,
            name=f"Duux {device_name}",
            config_entry=config_entry,
        )

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_13(self, hass, api, device_id, device_name, config_entry=None):
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

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_14(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name

        super().__init__(
            hass,
            _LOGGER,
            name=f"Duux {device_name}",
            update_interval=timedelta(seconds=None),
            config_entry=config_entry,
        )

    def xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_15(self, hass, api, device_id, device_name, config_entry=None):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name

        super().__init__(
            hass,
            _LOGGER,
            name=f"Duux {device_name}",
            update_interval=timedelta(seconds=31),
            config_entry=config_entry,
        )

    @_mutmut_mutated(mutants_xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut)
    async def _async_update_data(self):
        """Fetch data from API."""
        try:
            data = await self.hass.async_add_executor_job(
                self.api.get_device_status, self.device_id
            )
            return data
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")

    async def xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_orig(self):
        """Fetch data from API."""
        try:
            data = await self.hass.async_add_executor_job(
                self.api.get_device_status, self.device_id
            )
            return data
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")

    async def xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_1(self):
        """Fetch data from API."""
        try:
            data = None
            return data
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")

    async def xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_2(self):
        """Fetch data from API."""
        try:
            data = await self.hass.async_add_executor_job(
                None, self.device_id
            )
            return data
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")

    async def xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_3(self):
        """Fetch data from API."""
        try:
            data = await self.hass.async_add_executor_job(
                self.api.get_device_status, None
            )
            return data
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")

    async def xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_4(self):
        """Fetch data from API."""
        try:
            data = await self.hass.async_add_executor_job(
                self.device_id
            )
            return data
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")

    async def xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_5(self):
        """Fetch data from API."""
        try:
            data = await self.hass.async_add_executor_job(
                self.api.get_device_status, )
            return data
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")

    async def xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_6(self):
        """Fetch data from API."""
        try:
            data = await self.hass.async_add_executor_job(
                self.api.get_device_status, self.device_id
            )
            return data
        except Exception as err:
            raise UpdateFailed(None)

mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['_mutmut_orig'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_1'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_2'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_3'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_4'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_5'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_6'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_7'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_8'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_9'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_10'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_11'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_12'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_13'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_14'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ__init____mutmut['xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_15'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ__init____mutmut_15 # type: ignore # mutmut generated

mutants_xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut['_mutmut_orig'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut['xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_1'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut['xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_2'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut['xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_3'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut['xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_4'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut['xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_5'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut['xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_6'] = DuuxDataUpdateCoordinator.xǁDuuxDataUpdateCoordinatorǁ_async_update_data__mutmut_6 # type: ignore # mutmut generated
