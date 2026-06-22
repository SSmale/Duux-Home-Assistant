"""Support for Duux climate devices."""

import logging
from typing import Any, Iterator

from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import (
    ClimateEntityFeature,
    HVACMode,
    PRESET_BOOST,
    PRESET_COMFORT,
    PRESET_ECO,
)
from homeassistant.const import ATTR_TEMPERATURE, UnitOfTemperature
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    DUUX_CLIMATE_TYPES,
    DUUX_DTID_THERMOSTAT,
    DUUX_DTID_HEATER,
    DOMAIN,
    DUUX_STID_THREESIXTY_2023,
    DUUX_STID_EDGEHEATER_V2,
    DUUX_STID_EDGEHEATER_2000,
    DUUX_STID_EDGEHEATER_2023_V1,
    DUUX_STID_THREESIXTY_TWO,
)

_LOGGER = logging.getLogger(__name__)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_async_setup_entry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_async_setup_entry__mutmut)
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_orig(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_1(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux climate entities."""
    data = None
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_2(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux climate entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = None
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_3(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux climate entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["XXapiXX"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_4(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux climate entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["API"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_5(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux climate entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = None
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_6(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux climate entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["XXcoordinatorsXX"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_7(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux climate entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["COORDINATORS"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_8(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux climate entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = None

    entities = []
    for device in devices:
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_9(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux climate entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["XXdevicesXX"]

    entities = []
    for device in devices:
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_10(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux climate entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["DEVICES"]

    entities = []
    for device in devices:
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_11(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux climate entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = None
    for device in devices:
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_12(
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
        sensor_type = None
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_13(
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
        sensor_type = device.get("sensorType") and {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_14(
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
        sensor_type = device.get(None) or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_15(
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
        sensor_type = device.get("XXsensorTypeXX") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_16(
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
        sensor_type = device.get("sensortype") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_17(
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
        sensor_type = device.get("SENSORTYPE") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_18(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = None
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_19(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get(None)
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_20(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("XXtypeXX")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_21(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("TYPE")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_22(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = None
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_23(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") and ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_24(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get(None) or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_25(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("XXgoogleDeviceTypeXX") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_26(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googledevicetype") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_27(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("GOOGLEDEVICETYPE") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_28(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or "XXXX"
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_29(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = None  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_30(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(None)[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_31(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split("XX.XX")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_32(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[+1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_33(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-2] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_34(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else "XXXX"
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_35(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = None
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_36(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get(None)
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_37(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("XXsensorTypeIdXX")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_38(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensortypeid")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_39(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("SENSORTYPEID")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_40(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = None
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_41(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["XXdeviceIdXX"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_42(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceid"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_43(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["DEVICEID"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_44(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = None

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_45(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(None)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_46(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is not None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_47(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            break

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_48(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = None

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_49(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get(None, "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_50(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", None)

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_51(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_52(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", )

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_53(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("XXnameXX", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_54(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("NAME", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_55(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "XXUnknownXX")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_56(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_57(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "UNKNOWN")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_58(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_59(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word not in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_60(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    None
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_61(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "XXYour device has not been officially catagorised as supporting the climate platform.XX"
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_62(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_63(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "YOUR DEVICE HAS NOT BEEN OFFICIALLY CATAGORISED AS SUPPORTING THE CLIMATE PLATFORM."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_64(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    None,
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_65(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    None,
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_66(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "XXPlease report this to the integration developer so they can update the supported device list.XX",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_67(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_68(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "PLEASE REPORT THIS TO THE INTEGRATION DEVELOPER SO THEY CAN UPDATE THE SUPPORTED DEVICE LIST.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_69(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    None,
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_70(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                break

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_71(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id != DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_72(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(None)
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_73(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(None, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_74(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, None, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_75(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, None))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_76(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_77(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_78(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, ))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_79(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id != DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_80(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(None)
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_81(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(None, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_82(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, None, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_83(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, None))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_84(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_85(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_86(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, ))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_87(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id not in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
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


async def x_async_setup_entry__mutmut_88(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(None)
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_89(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(None, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_90(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, None, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_91(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, None))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_92(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_93(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_94(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, ))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_95(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id != DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_96(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(None)
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_97(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(None, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_98(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, None, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_99(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, None))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_100(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_101(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_102(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, ))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_103(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(None)
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_104(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(None, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_105(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, None, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_106(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, None))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_107(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_108(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_109(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, ))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_110(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                None
            )

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_111(
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
        sensor_type = device.get("sensorType") or {}
        device_type_id = sensor_type.get("type")
        google_type = sensor_type.get("googleDeviceType") or ""
        last_word = (
            google_type.split(".")[-1] if google_type else ""
        )  # "HEATER" OR "THERMOSTAT"
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        model = sensor_type.get("name", "Unknown")

        if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            if last_word in DUUX_CLIMATE_TYPES:
                _LOGGER.warning(
                    "Your device has not been officially catagorised as supporting the climate platform."
                )
                _LOGGER.warning(
                    f"It is classified as type {last_word}, so attempting to set up as a climate device.",
                )
                _LOGGER.warning(
                    "Please report this to the integration developer so they can update the supported device list.",
                )
                _LOGGER.warning(
                    f"Required details: Device Name: {model}, Device Type ID: {device_type_id}, Sensor Type ID: {sensor_type_id}, Google Device Type: {google_type}",
                )

            else:
                continue

        # Create the appropriate climate entity based on heater type
        if sensor_type_id == DUUX_STID_THREESIXTY_2023:
            entities.append(DuuxThreesixtyClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_EDGEHEATER_V2:
            entities.append(DuuxEdgeTwoClimate(coordinator, api, device))
        elif sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_2000,
        ]:
            entities.append(DuuxEdgeClimate(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_THREESIXTY_TWO:
            entities.append(DuuxThreesixtyTwoClimate(coordinator, api, device))
        else:
            # Fallback to generic entity for unknown types
            entities.append(DuuxClimateAutoDiscovery(coordinator, api, device))
            _LOGGER.warning(
                f"Unknown heater type {sensor_type_id}, using generic entity"
            )

    async_add_entities(None)

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
mutants_xǁDuuxClimateǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxClimateǁasync_set_temperature__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxClimateǁasync_added_to_hass__mutmut: MutantDict = {}  # type: ignore


class DuuxClimate(CoordinatorEntity, ClimateEntity):
    """Representation of a Duux climate device."""

    @_mutmut_mutated(mutants_xǁDuuxClimateǁ__init____mutmut)
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

    def xǁDuuxClimateǁ__init____mutmut_orig(self, coordinator, api, device):
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

    def xǁDuuxClimateǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(None)
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

    def xǁDuuxClimateǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = None
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

    def xǁDuuxClimateǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = None
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

    def xǁDuuxClimateǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = None
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

    def xǁDuuxClimateǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["XXidXX"]
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

    def xǁDuuxClimateǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["ID"]
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

    def xǁDuuxClimateǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = None  # MAC address
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

    def xǁDuuxClimateǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["XXdeviceIdXX"]  # MAC address
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

    def xǁDuuxClimateǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceid"]  # MAC address
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

    def xǁDuuxClimateǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["DEVICEID"]  # MAC address
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

    def xǁDuuxClimateǁ__init____mutmut_11(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = None
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

    def xǁDuuxClimateǁ__init____mutmut_12(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = None
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

    def xǁDuuxClimateǁ__init____mutmut_13(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") and device.get("name")
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

    def xǁDuuxClimateǁ__init____mutmut_14(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get(None) or device.get("name")
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

    def xǁDuuxClimateǁ__init____mutmut_15(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("XXdisplayNameXX") or device.get("name")
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

    def xǁDuuxClimateǁ__init____mutmut_16(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayname") or device.get("name")
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

    def xǁDuuxClimateǁ__init____mutmut_17(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("DISPLAYNAME") or device.get("name")
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

    def xǁDuuxClimateǁ__init____mutmut_18(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get(None)
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

    def xǁDuuxClimateǁ__init____mutmut_19(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("XXnameXX")
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

    def xǁDuuxClimateǁ__init____mutmut_20(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("NAME")
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

    def xǁDuuxClimateǁ__init____mutmut_21(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = None

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

    def xǁDuuxClimateǁ__init____mutmut_22(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = False

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

    def xǁDuuxClimateǁ__init____mutmut_23(self, coordinator, api, device):
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
        self._attr_min_temp = None
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

    def xǁDuuxClimateǁ__init____mutmut_24(self, coordinator, api, device):
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
        self._attr_min_temp = 19
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

    def xǁDuuxClimateǁ__init____mutmut_25(self, coordinator, api, device):
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
        self._attr_max_temp = None
        self._attr_target_temperature_step = 1

        self._attr_temperature_unit = UnitOfTemperature.CELSIUS
        self._attr_hvac_modes = [HVACMode.OFF, HVACMode.HEAT]
        self._attr_supported_features = (
            ClimateEntityFeature.TARGET_TEMPERATURE
            | ClimateEntityFeature.PRESET_MODE
            | ClimateEntityFeature.TURN_OFF
            | ClimateEntityFeature.TURN_ON
        )

    def xǁDuuxClimateǁ__init____mutmut_26(self, coordinator, api, device):
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
        self._attr_max_temp = 31
        self._attr_target_temperature_step = 1

        self._attr_temperature_unit = UnitOfTemperature.CELSIUS
        self._attr_hvac_modes = [HVACMode.OFF, HVACMode.HEAT]
        self._attr_supported_features = (
            ClimateEntityFeature.TARGET_TEMPERATURE
            | ClimateEntityFeature.PRESET_MODE
            | ClimateEntityFeature.TURN_OFF
            | ClimateEntityFeature.TURN_ON
        )

    def xǁDuuxClimateǁ__init____mutmut_27(self, coordinator, api, device):
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
        self._attr_target_temperature_step = None

        self._attr_temperature_unit = UnitOfTemperature.CELSIUS
        self._attr_hvac_modes = [HVACMode.OFF, HVACMode.HEAT]
        self._attr_supported_features = (
            ClimateEntityFeature.TARGET_TEMPERATURE
            | ClimateEntityFeature.PRESET_MODE
            | ClimateEntityFeature.TURN_OFF
            | ClimateEntityFeature.TURN_ON
        )

    def xǁDuuxClimateǁ__init____mutmut_28(self, coordinator, api, device):
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
        self._attr_target_temperature_step = 2

        self._attr_temperature_unit = UnitOfTemperature.CELSIUS
        self._attr_hvac_modes = [HVACMode.OFF, HVACMode.HEAT]
        self._attr_supported_features = (
            ClimateEntityFeature.TARGET_TEMPERATURE
            | ClimateEntityFeature.PRESET_MODE
            | ClimateEntityFeature.TURN_OFF
            | ClimateEntityFeature.TURN_ON
        )

    def xǁDuuxClimateǁ__init____mutmut_29(self, coordinator, api, device):
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

        self._attr_temperature_unit = None
        self._attr_hvac_modes = [HVACMode.OFF, HVACMode.HEAT]
        self._attr_supported_features = (
            ClimateEntityFeature.TARGET_TEMPERATURE
            | ClimateEntityFeature.PRESET_MODE
            | ClimateEntityFeature.TURN_OFF
            | ClimateEntityFeature.TURN_ON
        )

    def xǁDuuxClimateǁ__init____mutmut_30(self, coordinator, api, device):
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
        self._attr_hvac_modes = None
        self._attr_supported_features = (
            ClimateEntityFeature.TARGET_TEMPERATURE
            | ClimateEntityFeature.PRESET_MODE
            | ClimateEntityFeature.TURN_OFF
            | ClimateEntityFeature.TURN_ON
        )

    def xǁDuuxClimateǁ__init____mutmut_31(self, coordinator, api, device):
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
        self._attr_supported_features = None

    def xǁDuuxClimateǁ__init____mutmut_32(self, coordinator, api, device):
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
            | ClimateEntityFeature.TURN_OFF & ClimateEntityFeature.TURN_ON
        )

    def xǁDuuxClimateǁ__init____mutmut_33(self, coordinator, api, device):
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
            | ClimateEntityFeature.PRESET_MODE & ClimateEntityFeature.TURN_OFF
            | ClimateEntityFeature.TURN_ON
        )

    def xǁDuuxClimateǁ__init____mutmut_34(self, coordinator, api, device):
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
            ClimateEntityFeature.TARGET_TEMPERATURE & ClimateEntityFeature.PRESET_MODE
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
        return (self.coordinator.data or {}).get("temp")

    @property
    def target_temperature(self):
        """Return the temperature we try to reach."""
        return (self.coordinator.data or {}).get("sp")

    @property
    def hvac_mode(self):
        """Return current operation."""
        power = (self.coordinator.data or {}).get("power", 0)
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

    @_mutmut_mutated(mutants_xǁDuuxClimateǁasync_set_temperature__mutmut)
    async def async_set_temperature(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, self._device_mac, temperature
            )
            newData = self.coordinator.data
            newData["sp"] = temperature
            self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_temperature__mutmut_orig(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, self._device_mac, temperature
            )
            newData = self.coordinator.data
            newData["sp"] = temperature
            self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_temperature__mutmut_1(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(None)) is None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, self._device_mac, temperature
            )
            newData = self.coordinator.data
            newData["sp"] = temperature
            self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_temperature__mutmut_2(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is not None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, self._device_mac, temperature
            )
            newData = self.coordinator.data
            newData["sp"] = temperature
            self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_temperature__mutmut_3(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is None:
            return

        if temperature is None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, self._device_mac, temperature
            )
            newData = self.coordinator.data
            newData["sp"] = temperature
            self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_temperature__mutmut_4(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                None, self._device_mac, temperature
            )
            newData = self.coordinator.data
            newData["sp"] = temperature
            self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_temperature__mutmut_5(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, None, temperature
            )
            newData = self.coordinator.data
            newData["sp"] = temperature
            self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_temperature__mutmut_6(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, self._device_mac, None
            )
            newData = self.coordinator.data
            newData["sp"] = temperature
            self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_temperature__mutmut_7(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._device_mac, temperature
            )
            newData = self.coordinator.data
            newData["sp"] = temperature
            self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_temperature__mutmut_8(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, temperature
            )
            newData = self.coordinator.data
            newData["sp"] = temperature
            self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_temperature__mutmut_9(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, self._device_mac, )
            newData = self.coordinator.data
            newData["sp"] = temperature
            self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_temperature__mutmut_10(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, self._device_mac, temperature
            )
            newData = None
            newData["sp"] = temperature
            self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_temperature__mutmut_11(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, self._device_mac, temperature
            )
            newData = self.coordinator.data
            newData["sp"] = None
            self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_temperature__mutmut_12(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, self._device_mac, temperature
            )
            newData = self.coordinator.data
            newData["XXspXX"] = temperature
            self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_temperature__mutmut_13(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, self._device_mac, temperature
            )
            newData = self.coordinator.data
            newData["SP"] = temperature
            self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_temperature__mutmut_14(self, **kwargs):
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is None:
            return

        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, self._device_mac, temperature
            )
            newData = self.coordinator.data
            newData["sp"] = temperature
            self.coordinator.async_set_updated_data(None)

    @_mutmut_mutated(mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut)
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
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_orig(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_1(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode != HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_2(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                None, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_3(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, None, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_4(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, None
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_5(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_6(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_7(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_8(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_9(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                None, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_10(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, None, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_11(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, None
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_12(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_13(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_14(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_15(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_16(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = None
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_17(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_18(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["XXpowerXX"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_19(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["POWER"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_20(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = 2 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_21(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode != HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_22(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateǁasync_set_hvac_mode__mutmut_23(self, hvac_mode):
        """Set new HVAC mode."""

        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        newData = self.coordinator.data
        newData["power"] = 1 if hvac_mode == HVACMode.HEAT else 0
        self.coordinator.async_set_updated_data(None)

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
        return self.coordinator.last_update_success and (
            self.coordinator.data or {}
        ).get("online", True)

    @_mutmut_mutated(mutants_xǁDuuxClimateǁasync_added_to_hass__mutmut)
    async def async_added_to_hass(self):
        """When entity is added to hass."""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    async def xǁDuuxClimateǁasync_added_to_hass__mutmut_orig(self):
        """When entity is added to hass."""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    async def xǁDuuxClimateǁasync_added_to_hass__mutmut_1(self):
        """When entity is added to hass."""
        self.async_on_remove(
            None
        )

    async def xǁDuuxClimateǁasync_added_to_hass__mutmut_2(self):
        """When entity is added to hass."""
        self.async_on_remove(
            self.coordinator.async_add_listener(None)
        )

    async def async_update(self):
        """Update the entity."""
        await self.coordinator.async_request_refresh()

mutants_xǁDuuxClimateǁ__init____mutmut['_mutmut_orig'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_1'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_2'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_3'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_4'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_5'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_6'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_7'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_8'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_9'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_10'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_11'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_12'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_13'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_14'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_15'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_16'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_17'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_18'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_19'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_20'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_21'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_22'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_23'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_24'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_25'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_26'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_27'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_27 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_28'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_28 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_29'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_29 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_30'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_30 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_31'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_31 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_32'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_32 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_33'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_33 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁ__init____mutmut['xǁDuuxClimateǁ__init____mutmut_34'] = DuuxClimate.xǁDuuxClimateǁ__init____mutmut_34 # type: ignore # mutmut generated

mutants_xǁDuuxClimateǁasync_set_temperature__mutmut['_mutmut_orig'] = DuuxClimate.xǁDuuxClimateǁasync_set_temperature__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_temperature__mutmut['xǁDuuxClimateǁasync_set_temperature__mutmut_1'] = DuuxClimate.xǁDuuxClimateǁasync_set_temperature__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_temperature__mutmut['xǁDuuxClimateǁasync_set_temperature__mutmut_2'] = DuuxClimate.xǁDuuxClimateǁasync_set_temperature__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_temperature__mutmut['xǁDuuxClimateǁasync_set_temperature__mutmut_3'] = DuuxClimate.xǁDuuxClimateǁasync_set_temperature__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_temperature__mutmut['xǁDuuxClimateǁasync_set_temperature__mutmut_4'] = DuuxClimate.xǁDuuxClimateǁasync_set_temperature__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_temperature__mutmut['xǁDuuxClimateǁasync_set_temperature__mutmut_5'] = DuuxClimate.xǁDuuxClimateǁasync_set_temperature__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_temperature__mutmut['xǁDuuxClimateǁasync_set_temperature__mutmut_6'] = DuuxClimate.xǁDuuxClimateǁasync_set_temperature__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_temperature__mutmut['xǁDuuxClimateǁasync_set_temperature__mutmut_7'] = DuuxClimate.xǁDuuxClimateǁasync_set_temperature__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_temperature__mutmut['xǁDuuxClimateǁasync_set_temperature__mutmut_8'] = DuuxClimate.xǁDuuxClimateǁasync_set_temperature__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_temperature__mutmut['xǁDuuxClimateǁasync_set_temperature__mutmut_9'] = DuuxClimate.xǁDuuxClimateǁasync_set_temperature__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_temperature__mutmut['xǁDuuxClimateǁasync_set_temperature__mutmut_10'] = DuuxClimate.xǁDuuxClimateǁasync_set_temperature__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_temperature__mutmut['xǁDuuxClimateǁasync_set_temperature__mutmut_11'] = DuuxClimate.xǁDuuxClimateǁasync_set_temperature__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_temperature__mutmut['xǁDuuxClimateǁasync_set_temperature__mutmut_12'] = DuuxClimate.xǁDuuxClimateǁasync_set_temperature__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_temperature__mutmut['xǁDuuxClimateǁasync_set_temperature__mutmut_13'] = DuuxClimate.xǁDuuxClimateǁasync_set_temperature__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_temperature__mutmut['xǁDuuxClimateǁasync_set_temperature__mutmut_14'] = DuuxClimate.xǁDuuxClimateǁasync_set_temperature__mutmut_14 # type: ignore # mutmut generated

mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['_mutmut_orig'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_1'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_2'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_3'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_4'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_5'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_6'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_7'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_8'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_9'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_10'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_11'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_12'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_13'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_14'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_15'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_16'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_17'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_18'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_19'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_20'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_21'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_22'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_set_hvac_mode__mutmut['xǁDuuxClimateǁasync_set_hvac_mode__mutmut_23'] = DuuxClimate.xǁDuuxClimateǁasync_set_hvac_mode__mutmut_23 # type: ignore # mutmut generated

mutants_xǁDuuxClimateǁasync_added_to_hass__mutmut['_mutmut_orig'] = DuuxClimate.xǁDuuxClimateǁasync_added_to_hass__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_added_to_hass__mutmut['xǁDuuxClimateǁasync_added_to_hass__mutmut_1'] = DuuxClimate.xǁDuuxClimateǁasync_added_to_hass__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxClimateǁasync_added_to_hass__mutmut['xǁDuuxClimateǁasync_added_to_hass__mutmut_2'] = DuuxClimate.xǁDuuxClimateǁasync_added_to_hass__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut: MutantDict = {}  # type: ignore


class DuuxClimateAutoDiscovery(DuuxClimate):
    """Duux climate autodiscovery."""

    @_mutmut_mutated(mutants_xǁDuuxClimateAutoDiscoveryǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator, api, device)
        self._presets = self.presets_discovery()

    def xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator, api, device)
        self._presets = self.presets_discovery()

    def xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(None, api, device)
        self._presets = self.presets_discovery()

    def xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator, None, device)
        self._presets = self.presets_discovery()

    def xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator, api, None)
        self._presets = self.presets_discovery()

    def xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(api, device)
        self._presets = self.presets_discovery()

    def xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator, device)
        self._presets = self.presets_discovery()

    def xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator, api, )
        self._presets = self.presets_discovery()

    def xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the climate device."""
        super().__init__(coordinator, api, device)
        self._presets = None

    @_mutmut_mutated(mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut)
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_orig(self):
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_1(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = None
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_2(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get(None)
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_3(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data and {}).get("availableModes")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_4(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("XXavailableModesXX")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_5(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availablemodes")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_6(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("AVAILABLEMODES")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_7(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availableModes")
        if modes is not None:
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_8(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availableModes")
        if modes is None:
            modes = None

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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_9(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availableModes")
        if modes is None:
            modes = next(
                None,
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_10(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availableModes")
        if modes is None:
            modes = next(
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_11(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availableModes")
        if modes is None:
            modes = next(
                DuuxClimateAutoDiscovery._deep_find(self._device, "availableModes"),
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_12(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availableModes")
        if modes is None:
            modes = next(
                DuuxClimateAutoDiscovery._deep_find(None, "availableModes"),
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_13(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availableModes")
        if modes is None:
            modes = next(
                DuuxClimateAutoDiscovery._deep_find(self._device, None),
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_14(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availableModes")
        if modes is None:
            modes = next(
                DuuxClimateAutoDiscovery._deep_find("availableModes"),
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_15(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availableModes")
        if modes is None:
            modes = next(
                DuuxClimateAutoDiscovery._deep_find(self._device, ),
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_16(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availableModes")
        if modes is None:
            modes = next(
                DuuxClimateAutoDiscovery._deep_find(self._device, "XXavailableModesXX"),
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_17(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availableModes")
        if modes is None:
            modes = next(
                DuuxClimateAutoDiscovery._deep_find(self._device, "availablemodes"),
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_18(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availableModes")
        if modes is None:
            modes = next(
                DuuxClimateAutoDiscovery._deep_find(self._device, "AVAILABLEMODES"),
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_19(self):
        """Discover available presets."""

        # Guard against coordinator.data being None during initialization
        modes: Any = (self.coordinator.data or {}).get("availableModes")
        if modes is None:
            modes = next(
                DuuxClimateAutoDiscovery._deep_find(self._device, "availableModes"),
                None,
            )

        if isinstance(modes, list):
            modes = None

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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_20(self):
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
                None,
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_21(self):
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_22(self):
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_23(self):
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
                    if isinstance(candidate, dict) or candidate.get("settings")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_24(self):
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
                    if isinstance(candidate, dict) and candidate.get(None)
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_25(self):
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
                    if isinstance(candidate, dict) and candidate.get("XXsettingsXX")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_26(self):
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
                    if isinstance(candidate, dict) and candidate.get("SETTINGS")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_27(self):
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

        if isinstance(modes, dict):
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_28(self):
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
            _LOGGER.debug(None)
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_29(self):
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
            _LOGGER.debug("XXNo available modes foundXX")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_30(self):
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
            _LOGGER.debug("no available modes found")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_31(self):
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
            _LOGGER.debug("NO AVAILABLE MODES FOUND")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_32(self):
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

        settings = None
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_33(self):
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

        settings = modes.get(None)
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_34(self):
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

        settings = modes.get("XXsettingsXX")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_35(self):
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

        settings = modes.get("SETTINGS")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_36(self):
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
        if isinstance(settings, list):
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_37(self):
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
            _LOGGER.debug(None)
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_38(self):
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
            _LOGGER.debug("XXNo settings found in available modesXX")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_39(self):
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
            _LOGGER.debug("no settings found in available modes")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_40(self):
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
            _LOGGER.debug("NO SETTINGS FOUND IN AVAILABLE MODES")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_41(self):
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

        command_prefix = None

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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_42(self):
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
            modes.get("command_key") or modes.get("commandKey") and modes.get("key")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_43(self):
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
            modes.get("command_key") and modes.get("commandKey") or modes.get("key")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_44(self):
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
            modes.get(None) or modes.get("commandKey") or modes.get("key")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_45(self):
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
            modes.get("XXcommand_keyXX") or modes.get("commandKey") or modes.get("key")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_46(self):
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
            modes.get("COMMAND_KEY") or modes.get("commandKey") or modes.get("key")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_47(self):
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
            modes.get("command_key") or modes.get(None) or modes.get("key")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_48(self):
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
            modes.get("command_key") or modes.get("XXcommandKeyXX") or modes.get("key")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_49(self):
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
            modes.get("command_key") or modes.get("commandkey") or modes.get("key")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_50(self):
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
            modes.get("command_key") or modes.get("COMMANDKEY") or modes.get("key")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_51(self):
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
            modes.get("command_key") or modes.get("commandKey") or modes.get(None)
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_52(self):
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
            modes.get("command_key") or modes.get("commandKey") or modes.get("XXkeyXX")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_53(self):
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
            modes.get("command_key") or modes.get("commandKey") or modes.get("KEY")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_54(self):
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

        presets = None
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_55(self):
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
            if isinstance(setting, dict):
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_56(self):
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
                break

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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_57(self):
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

            name = None

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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_58(self):
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
                or setting.get("settingName") and setting.get("name")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_59(self):
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
                setting.get("setting_name") and setting.get("settingName")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_60(self):
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
                setting.get(None)
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_61(self):
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
                setting.get("XXsetting_nameXX")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_62(self):
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
                setting.get("SETTING_NAME")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_63(self):
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
                or setting.get(None)
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_64(self):
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
                or setting.get("XXsettingNameXX")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_65(self):
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
                or setting.get("settingname")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_66(self):
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
                or setting.get("SETTINGNAME")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_67(self):
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
                or setting.get(None)
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_68(self):
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
                or setting.get("XXnameXX")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_69(self):
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
                or setting.get("NAME")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_70(self):
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

            value = None

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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_71(self):
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
                or setting.get("settingValue") and setting.get("value")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_72(self):
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
                setting.get("setting_value") and setting.get("settingValue")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_73(self):
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
                setting.get(None)
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_74(self):
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
                setting.get("XXsetting_valueXX")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_75(self):
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
                setting.get("SETTING_VALUE")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_76(self):
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
                or setting.get(None)
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_77(self):
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
                or setting.get("XXsettingValueXX")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_78(self):
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
                or setting.get("settingvalue")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_79(self):
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
                or setting.get("SETTINGVALUE")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_80(self):
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
                or setting.get(None)
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_81(self):
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
                or setting.get("XXvalueXX")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_82(self):
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
                or setting.get("VALUE")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_83(self):
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

            name = None

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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_84(self):
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

            name = self._normalize_mode_name(None, value)

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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_85(self):
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

            name = self._normalize_mode_name(name, None)

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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_86(self):
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

            name = self._normalize_mode_name(value)

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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_87(self):
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

            name = self._normalize_mode_name(name, )

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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_88(self):
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

            command = None
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_89(self):
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

            command = setting.get(None)
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_90(self):
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

            command = setting.get("XXcommandXX")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_91(self):
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

            command = setting.get("COMMAND")
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_92(self):
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
            if command is None and command_prefix or value is not None:
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_93(self):
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
            if command is None or command_prefix and value is not None:
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_94(self):
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
            if command is not None and command_prefix and value is not None:
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_95(self):
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
            if command is None and command_prefix and value is None:
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_96(self):
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
                command = None
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_97(self):
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
            elif command is not None:
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_98(self):
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
                command = None

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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_99(self):
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

            if name or command is not None:
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_100(self):
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

            if name and command is None:
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_101(self):
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
                normalized_command = None
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_102(self):
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
                normalized_command = str(None)
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

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_103(self):
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
                normalized_value = None
                presets.append(
                    {
                        "name": str(name),
                        "command": normalized_command,
                        "value": normalized_value,
                    }
                )

        _LOGGER.debug("Discovered presets: %s", presets)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_104(self):
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
                normalized_value = None if value is not None else str(value)
                presets.append(
                    {
                        "name": str(name),
                        "command": normalized_command,
                        "value": normalized_value,
                    }
                )

        _LOGGER.debug("Discovered presets: %s", presets)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_105(self):
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
                normalized_value = None if value is None else str(None)
                presets.append(
                    {
                        "name": str(name),
                        "command": normalized_command,
                        "value": normalized_value,
                    }
                )

        _LOGGER.debug("Discovered presets: %s", presets)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_106(self):
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
                    None
                )

        _LOGGER.debug("Discovered presets: %s", presets)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_107(self):
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
                        "XXnameXX": str(name),
                        "command": normalized_command,
                        "value": normalized_value,
                    }
                )

        _LOGGER.debug("Discovered presets: %s", presets)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_108(self):
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
                        "NAME": str(name),
                        "command": normalized_command,
                        "value": normalized_value,
                    }
                )

        _LOGGER.debug("Discovered presets: %s", presets)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_109(self):
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
                        "name": str(None),
                        "command": normalized_command,
                        "value": normalized_value,
                    }
                )

        _LOGGER.debug("Discovered presets: %s", presets)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_110(self):
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
                        "XXcommandXX": normalized_command,
                        "value": normalized_value,
                    }
                )

        _LOGGER.debug("Discovered presets: %s", presets)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_111(self):
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
                        "COMMAND": normalized_command,
                        "value": normalized_value,
                    }
                )

        _LOGGER.debug("Discovered presets: %s", presets)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_112(self):
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
                        "XXvalueXX": normalized_value,
                    }
                )

        _LOGGER.debug("Discovered presets: %s", presets)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_113(self):
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
                        "VALUE": normalized_value,
                    }
                )

        _LOGGER.debug("Discovered presets: %s", presets)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_114(self):
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

        _LOGGER.debug(None, presets)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_115(self):
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

        _LOGGER.debug("Discovered presets: %s", None)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_116(self):
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

        _LOGGER.debug(presets)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_117(self):
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

        _LOGGER.debug("Discovered presets: %s", )

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_118(self):
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

        _LOGGER.debug("XXDiscovered presets: %sXX", presets)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_119(self):
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

        _LOGGER.debug("discovered presets: %s", presets)

        return presets

    def xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_120(self):
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

        _LOGGER.debug("DISCOVERED PRESETS: %S", presets)

        return presets

    def _normalize_mode_name(self, name, value: Any) -> Any:
        """Return normalized mode value."""
        return name

    @property
    def preset_mode(self):
        """Return current preset mode."""
        mode = (self.coordinator.data or {}).get("mode")
        for preset in self._presets:
            if preset["value"] == str(mode):
                return preset["name"]
        return None

    @property
    def preset_modes(self):
        """Return available preset modes."""
        # Base implementation - override in subclasses if needed
        return [preset["name"] for preset in self._presets]

    @_mutmut_mutated(mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut)
    async def async_set_preset_mode(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_orig(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_1(self, preset_mode):
        """Set preset mode."""
        mode_value = ""
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_2(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["XXnameXX"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_3(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["NAME"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_4(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] != preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_5(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = None
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_6(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["XXcommandXX"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_7(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["COMMAND"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_8(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = None
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_9(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["XXvalueXX"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_10(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["VALUE"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_11(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                return

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_12(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            None, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_13(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, None, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_14(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_15(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_16(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_17(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_18(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = None
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_19(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_20(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["XXmodeXX"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_21(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["MODE"] = mode_value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_22(self, preset_mode):
        """Set preset mode."""
        mode_value = None
        for preset in self._presets:
            if preset["name"] == preset_mode:
                mode_command = preset["command"]
                mode_value = preset["value"]
                break

        await self.hass.async_add_executor_job(
            self._api.send_command, self._device_mac, f"tune set {mode_command}"
        )
        newData = self.coordinator.data
        newData["mode"] = mode_value
        self.coordinator.async_set_updated_data(None)

    @staticmethod
    @_mutmut_mutated(mutants_xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut)
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

    @staticmethod
    def xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_orig(obj: Any, key: str) -> Iterator[Any]:
        """Yield every value for `key` inside a nested dict/list structure."""
        if isinstance(obj, dict):
            if key in obj:
                yield obj[key]
            for value in obj.values():
                yield from DuuxClimateAutoDiscovery._deep_find(value, key)
        elif isinstance(obj, list):
            for item in obj:
                yield from DuuxClimateAutoDiscovery._deep_find(item, key)

    @staticmethod
    def xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_1(obj: Any, key: str) -> Iterator[Any]:
        """Yield every value for `key` inside a nested dict/list structure."""
        if isinstance(obj, dict):
            if key not in obj:
                yield obj[key]
            for value in obj.values():
                yield from DuuxClimateAutoDiscovery._deep_find(value, key)
        elif isinstance(obj, list):
            for item in obj:
                yield from DuuxClimateAutoDiscovery._deep_find(item, key)

    @staticmethod
    def xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_2(obj: Any, key: str) -> Iterator[Any]:
        """Yield every value for `key` inside a nested dict/list structure."""
        if isinstance(obj, dict):
            if key in obj:
                yield obj[key]
            for value in obj.values():
                yield from DuuxClimateAutoDiscovery._deep_find(None, key)
        elif isinstance(obj, list):
            for item in obj:
                yield from DuuxClimateAutoDiscovery._deep_find(item, key)

    @staticmethod
    def xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_3(obj: Any, key: str) -> Iterator[Any]:
        """Yield every value for `key` inside a nested dict/list structure."""
        if isinstance(obj, dict):
            if key in obj:
                yield obj[key]
            for value in obj.values():
                yield from DuuxClimateAutoDiscovery._deep_find(value, None)
        elif isinstance(obj, list):
            for item in obj:
                yield from DuuxClimateAutoDiscovery._deep_find(item, key)

    @staticmethod
    def xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_4(obj: Any, key: str) -> Iterator[Any]:
        """Yield every value for `key` inside a nested dict/list structure."""
        if isinstance(obj, dict):
            if key in obj:
                yield obj[key]
            for value in obj.values():
                yield from DuuxClimateAutoDiscovery._deep_find(key)
        elif isinstance(obj, list):
            for item in obj:
                yield from DuuxClimateAutoDiscovery._deep_find(item, key)

    @staticmethod
    def xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_5(obj: Any, key: str) -> Iterator[Any]:
        """Yield every value for `key` inside a nested dict/list structure."""
        if isinstance(obj, dict):
            if key in obj:
                yield obj[key]
            for value in obj.values():
                yield from DuuxClimateAutoDiscovery._deep_find(value, )
        elif isinstance(obj, list):
            for item in obj:
                yield from DuuxClimateAutoDiscovery._deep_find(item, key)

    @staticmethod
    def xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_6(obj: Any, key: str) -> Iterator[Any]:
        """Yield every value for `key` inside a nested dict/list structure."""
        if isinstance(obj, dict):
            if key in obj:
                yield obj[key]
            for value in obj.values():
                yield from DuuxClimateAutoDiscovery._deep_find(value, key)
        elif isinstance(obj, list):
            for item in obj:
                yield from DuuxClimateAutoDiscovery._deep_find(None, key)

    @staticmethod
    def xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_7(obj: Any, key: str) -> Iterator[Any]:
        """Yield every value for `key` inside a nested dict/list structure."""
        if isinstance(obj, dict):
            if key in obj:
                yield obj[key]
            for value in obj.values():
                yield from DuuxClimateAutoDiscovery._deep_find(value, key)
        elif isinstance(obj, list):
            for item in obj:
                yield from DuuxClimateAutoDiscovery._deep_find(item, None)

    @staticmethod
    def xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_8(obj: Any, key: str) -> Iterator[Any]:
        """Yield every value for `key` inside a nested dict/list structure."""
        if isinstance(obj, dict):
            if key in obj:
                yield obj[key]
            for value in obj.values():
                yield from DuuxClimateAutoDiscovery._deep_find(value, key)
        elif isinstance(obj, list):
            for item in obj:
                yield from DuuxClimateAutoDiscovery._deep_find(key)

    @staticmethod
    def xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_9(obj: Any, key: str) -> Iterator[Any]:
        """Yield every value for `key` inside a nested dict/list structure."""
        if isinstance(obj, dict):
            if key in obj:
                yield obj[key]
            for value in obj.values():
                yield from DuuxClimateAutoDiscovery._deep_find(value, key)
        elif isinstance(obj, list):
            for item in obj:
                yield from DuuxClimateAutoDiscovery._deep_find(item, )

mutants_xǁDuuxClimateAutoDiscoveryǁ__init____mutmut['_mutmut_orig'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ__init____mutmut['xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_1'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ__init____mutmut['xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_2'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ__init____mutmut['xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_3'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ__init____mutmut['xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_4'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ__init____mutmut['xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_5'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ__init____mutmut['xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_6'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ__init____mutmut['xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_7'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ__init____mutmut_7 # type: ignore # mutmut generated

mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['_mutmut_orig'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_1'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_2'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_3'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_4'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_5'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_6'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_7'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_8'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_9'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_10'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_11'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_12'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_13'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_14'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_15'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_16'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_17'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_18'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_19'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_20'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_21'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_22'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_23'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_24'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_25'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_26'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_27'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_28'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_29'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_30'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_31'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_32'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_33'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_34'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_35'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_36'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_37'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_38'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_39'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_40'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_41'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_41 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_42'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_42 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_43'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_43 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_44'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_44 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_45'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_45 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_46'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_46 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_47'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_47 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_48'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_48 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_49'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_49 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_50'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_50 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_51'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_51 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_52'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_52 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_53'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_53 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_54'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_54 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_55'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_55 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_56'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_56 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_57'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_57 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_58'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_58 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_59'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_59 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_60'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_60 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_61'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_61 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_62'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_62 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_63'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_63 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_64'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_64 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_65'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_65 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_66'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_66 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_67'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_67 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_68'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_68 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_69'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_69 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_70'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_70 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_71'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_71 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_72'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_72 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_73'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_73 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_74'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_74 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_75'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_75 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_76'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_76 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_77'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_77 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_78'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_78 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_79'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_79 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_80'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_80 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_81'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_81 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_82'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_82 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_83'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_83 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_84'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_84 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_85'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_85 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_86'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_86 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_87'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_87 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_88'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_88 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_89'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_89 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_90'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_90 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_91'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_91 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_92'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_92 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_93'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_93 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_94'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_94 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_95'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_95 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_96'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_96 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_97'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_97 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_98'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_98 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_99'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_99 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_100'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_100 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_101'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_101 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_102'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_102 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_103'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_103 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_104'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_104 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_105'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_105 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_106'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_106 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_107'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_107 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_108'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_108 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_109'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_109 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_110'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_110 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_111'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_111 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_112'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_112 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_113'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_113 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_114'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_114 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_115'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_115 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_116'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_116 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_117'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_117 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_118'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_118 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_119'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_119 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut['xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_120'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁpresets_discovery__mutmut_120 # type: ignore # mutmut generated

mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['_mutmut_orig'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_1'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_2'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_3'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_4'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_5'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_6'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_7'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_8'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_9'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_10'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_11'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_12'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_13'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_14'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_15'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_16'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_17'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_18'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_19'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_20'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_21'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut['xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_22'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁasync_set_preset_mode__mutmut_22 # type: ignore # mutmut generated

mutants_xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut['_mutmut_orig'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut['xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_1'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut['xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_2'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut['xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_3'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut['xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_4'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut['xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_5'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut['xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_6'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut['xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_7'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut['xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_8'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut['xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_9'] = DuuxClimateAutoDiscovery.xǁDuuxClimateAutoDiscoveryǁ_deep_find__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut: MutantDict = {}  # type: ignore


class DuuxThreesixtyBase(DuuxClimateAutoDiscovery):
    """Shared base for Threesixty devices."""

    PRESET_LOW = PRESET_ECO
    PRESET_HIGH = PRESET_BOOST
    PRESET_MID = PRESET_COMFORT

    @_mutmut_mutated(mutants_xǁDuuxThreesixtyBaseǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the Threesixty climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Threesixty
        self._attr_min_temp = 18
        self._attr_max_temp = 30

    def xǁDuuxThreesixtyBaseǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the Threesixty climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Threesixty
        self._attr_min_temp = 18
        self._attr_max_temp = 30

    def xǁDuuxThreesixtyBaseǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the Threesixty climate device."""
        super().__init__(None, api, device)
        # Temperature range for Threesixty
        self._attr_min_temp = 18
        self._attr_max_temp = 30

    def xǁDuuxThreesixtyBaseǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the Threesixty climate device."""
        super().__init__(coordinator, None, device)
        # Temperature range for Threesixty
        self._attr_min_temp = 18
        self._attr_max_temp = 30

    def xǁDuuxThreesixtyBaseǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the Threesixty climate device."""
        super().__init__(coordinator, api, None)
        # Temperature range for Threesixty
        self._attr_min_temp = 18
        self._attr_max_temp = 30

    def xǁDuuxThreesixtyBaseǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the Threesixty climate device."""
        super().__init__(api, device)
        # Temperature range for Threesixty
        self._attr_min_temp = 18
        self._attr_max_temp = 30

    def xǁDuuxThreesixtyBaseǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the Threesixty climate device."""
        super().__init__(coordinator, device)
        # Temperature range for Threesixty
        self._attr_min_temp = 18
        self._attr_max_temp = 30

    def xǁDuuxThreesixtyBaseǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the Threesixty climate device."""
        super().__init__(coordinator, api, )
        # Temperature range for Threesixty
        self._attr_min_temp = 18
        self._attr_max_temp = 30

    def xǁDuuxThreesixtyBaseǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the Threesixty climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Threesixty
        self._attr_min_temp = None
        self._attr_max_temp = 30

    def xǁDuuxThreesixtyBaseǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the Threesixty climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Threesixty
        self._attr_min_temp = 19
        self._attr_max_temp = 30

    def xǁDuuxThreesixtyBaseǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the Threesixty climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Threesixty
        self._attr_min_temp = 18
        self._attr_max_temp = None

    def xǁDuuxThreesixtyBaseǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the Threesixty climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Threesixty
        self._attr_min_temp = 18
        self._attr_max_temp = 31

    @_mutmut_mutated(mutants_xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut)
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

    def xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_orig(self, name, value: Any) -> Any:
        """Change the name for the HA presets for Threesixty models."""
        if value is not None:
            if value == "2":
                return PRESET_ECO
            if value == "1":
                return PRESET_COMFORT
            if value == "0":
                return PRESET_BOOST
        return name

    def xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_1(self, name, value: Any) -> Any:
        """Change the name for the HA presets for Threesixty models."""
        if value is None:
            if value == "2":
                return PRESET_ECO
            if value == "1":
                return PRESET_COMFORT
            if value == "0":
                return PRESET_BOOST
        return name

    def xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_2(self, name, value: Any) -> Any:
        """Change the name for the HA presets for Threesixty models."""
        if value is not None:
            if value != "2":
                return PRESET_ECO
            if value == "1":
                return PRESET_COMFORT
            if value == "0":
                return PRESET_BOOST
        return name

    def xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_3(self, name, value: Any) -> Any:
        """Change the name for the HA presets for Threesixty models."""
        if value is not None:
            if value == "XX2XX":
                return PRESET_ECO
            if value == "1":
                return PRESET_COMFORT
            if value == "0":
                return PRESET_BOOST
        return name

    def xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_4(self, name, value: Any) -> Any:
        """Change the name for the HA presets for Threesixty models."""
        if value is not None:
            if value == "2":
                return PRESET_ECO
            if value != "1":
                return PRESET_COMFORT
            if value == "0":
                return PRESET_BOOST
        return name

    def xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_5(self, name, value: Any) -> Any:
        """Change the name for the HA presets for Threesixty models."""
        if value is not None:
            if value == "2":
                return PRESET_ECO
            if value == "XX1XX":
                return PRESET_COMFORT
            if value == "0":
                return PRESET_BOOST
        return name

    def xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_6(self, name, value: Any) -> Any:
        """Change the name for the HA presets for Threesixty models."""
        if value is not None:
            if value == "2":
                return PRESET_ECO
            if value == "1":
                return PRESET_COMFORT
            if value != "0":
                return PRESET_BOOST
        return name

    def xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_7(self, name, value: Any) -> Any:
        """Change the name for the HA presets for Threesixty models."""
        if value is not None:
            if value == "2":
                return PRESET_ECO
            if value == "1":
                return PRESET_COMFORT
            if value == "XX0XX":
                return PRESET_BOOST
        return name

mutants_xǁDuuxThreesixtyBaseǁ__init____mutmut['_mutmut_orig'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ__init____mutmut['xǁDuuxThreesixtyBaseǁ__init____mutmut_1'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ__init____mutmut['xǁDuuxThreesixtyBaseǁ__init____mutmut_2'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ__init____mutmut['xǁDuuxThreesixtyBaseǁ__init____mutmut_3'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ__init____mutmut['xǁDuuxThreesixtyBaseǁ__init____mutmut_4'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ__init____mutmut['xǁDuuxThreesixtyBaseǁ__init____mutmut_5'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ__init____mutmut['xǁDuuxThreesixtyBaseǁ__init____mutmut_6'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ__init____mutmut['xǁDuuxThreesixtyBaseǁ__init____mutmut_7'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ__init____mutmut['xǁDuuxThreesixtyBaseǁ__init____mutmut_8'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ__init____mutmut['xǁDuuxThreesixtyBaseǁ__init____mutmut_9'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ__init____mutmut['xǁDuuxThreesixtyBaseǁ__init____mutmut_10'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ__init____mutmut_10 # type: ignore # mutmut generated

mutants_xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut['_mutmut_orig'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut['xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_1'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut['xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_2'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut['xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_3'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut['xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_4'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut['xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_5'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut['xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_6'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut['xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_7'] = DuuxThreesixtyBase.xǁDuuxThreesixtyBaseǁ_normalize_mode_name__mutmut_7 # type: ignore # mutmut generated


class DuuxThreesixtyClimate(DuuxThreesixtyBase):
    """Duux Threesixty 2023 heater."""


class DuuxThreesixtyTwoClimate(DuuxThreesixtyBase):
    """Duux Threesixty Two 2022 heater."""
mutants_xǁDuuxEdgeTwoClimateǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut: MutantDict = {}  # type: ignore


class DuuxEdgeTwoClimate(DuuxClimate):
    """Duux Edge heater v2."""

    PRESET_LOW = PRESET_ECO
    PRESET_BOOST = PRESET_BOOST
    PRESET_HIGH = PRESET_COMFORT

    @_mutmut_mutated(mutants_xǁDuuxEdgeTwoClimateǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeTwoClimateǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeTwoClimateǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(None, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeTwoClimateǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, None, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeTwoClimateǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, None)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeTwoClimateǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeTwoClimateǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeTwoClimateǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, )
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeTwoClimateǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = None
        self._attr_max_temp = 36

    def xǁDuuxEdgeTwoClimateǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 6
        self._attr_max_temp = 36

    def xǁDuuxEdgeTwoClimateǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = None

    def xǁDuuxEdgeTwoClimateǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 37

    @property
    def preset_modes(self):
        """Return available preset modes."""
        return [self.PRESET_LOW, self.PRESET_HIGH, self.PRESET_BOOST]

    @property
    def preset_mode(self):
        """Return current preset mode."""
        mode = (self.coordinator.data or {}).get("heatin", self.PRESET_LOW)
        mode_map = {1: self.PRESET_LOW, 2: self.PRESET_HIGH, 3: self.PRESET_BOOST}
        return mode_map.get(mode)

    @_mutmut_mutated(mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut)
    async def async_set_preset_mode(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_orig(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_1(self, preset_mode):
        """Set preset mode."""
        mode_map = None

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_2(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "XX1XX", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_3(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "XX2XX", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_4(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "XX3XX"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_5(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = None

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_6(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(None, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_7(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, None)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_8(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_9(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, )

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_10(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 2)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_11(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            None, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_12(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, None, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_13(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_14(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_15(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_16(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_17(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = None
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_18(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_19(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["XXheatinXX"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_20(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["HEATIN"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_21(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(None)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_22(self, preset_mode):
        """Set preset mode."""
        mode_map = {self.PRESET_LOW: "1", self.PRESET_HIGH: "2", self.PRESET_BOOST: "3"}

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(None)

mutants_xǁDuuxEdgeTwoClimateǁ__init____mutmut['_mutmut_orig'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁ__init____mutmut['xǁDuuxEdgeTwoClimateǁ__init____mutmut_1'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁ__init____mutmut['xǁDuuxEdgeTwoClimateǁ__init____mutmut_2'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁ__init____mutmut['xǁDuuxEdgeTwoClimateǁ__init____mutmut_3'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁ__init____mutmut['xǁDuuxEdgeTwoClimateǁ__init____mutmut_4'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁ__init____mutmut['xǁDuuxEdgeTwoClimateǁ__init____mutmut_5'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁ__init____mutmut['xǁDuuxEdgeTwoClimateǁ__init____mutmut_6'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁ__init____mutmut['xǁDuuxEdgeTwoClimateǁ__init____mutmut_7'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁ__init____mutmut['xǁDuuxEdgeTwoClimateǁ__init____mutmut_8'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁ__init____mutmut['xǁDuuxEdgeTwoClimateǁ__init____mutmut_9'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁ__init____mutmut['xǁDuuxEdgeTwoClimateǁ__init____mutmut_10'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁ__init____mutmut_10 # type: ignore # mutmut generated

mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['_mutmut_orig'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_1'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_2'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_3'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_4'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_5'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_6'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_7'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_8'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_9'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_10'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_11'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_12'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_13'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_14'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_15'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_16'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_17'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_18'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_19'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_20'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_21'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_22'] = DuuxEdgeTwoClimate.xǁDuuxEdgeTwoClimateǁasync_set_preset_mode__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut: MutantDict = {}  # type: ignore


class DuuxEdgeClimate(DuuxClimate):
    """Duux Edge heater 2023 (v1)."""

    PRESET_LOW = PRESET_ECO
    PRESET_HIGH = PRESET_COMFORT

    @_mutmut_mutated(mutants_xǁDuuxEdgeClimateǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeClimateǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeClimateǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(None, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeClimateǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, None, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeClimateǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, None)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeClimateǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeClimateǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeClimateǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, )
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 36

    def xǁDuuxEdgeClimateǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = None
        self._attr_max_temp = 36

    def xǁDuuxEdgeClimateǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 6
        self._attr_max_temp = 36

    def xǁDuuxEdgeClimateǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = None

    def xǁDuuxEdgeClimateǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the Edge climate device."""
        super().__init__(coordinator, api, device)
        # Temperature range for Edge heater
        self._attr_min_temp = 5
        self._attr_max_temp = 37

    @property
    def preset_modes(self):
        """Return available preset modes."""
        return [self.PRESET_LOW, self.PRESET_HIGH]

    @property
    def preset_mode(self):
        """Return current preset mode."""
        mode = (self.coordinator.data or {}).get("heatin", self.PRESET_LOW)
        mode_map = {
            1: self.PRESET_LOW,
            2: self.PRESET_HIGH,
        }
        return mode_map.get(mode)

    @_mutmut_mutated(mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut)
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
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_orig(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_1(self, preset_mode):
        """Set preset mode."""
        mode_map = None

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_2(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "XX1XX",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_3(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "XX2XX",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_4(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = None

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_5(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(None, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_6(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, None)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_7(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_8(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, )

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_9(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 2)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_10(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            None, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_11(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, None, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_12(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_13(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_14(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_15(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_16(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = None
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_17(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_18(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["XXheatinXX"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_19(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["HEATIN"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_20(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(None)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_21(self, preset_mode):
        """Set preset mode."""
        mode_map = {
            self.PRESET_LOW: "1",
            self.PRESET_HIGH: "2",
        }

        mode = mode_map.get(preset_mode, 1)

        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["heatin"] = int(mode)
        self.coordinator.async_set_updated_data(None)

mutants_xǁDuuxEdgeClimateǁ__init____mutmut['_mutmut_orig'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁ__init____mutmut['xǁDuuxEdgeClimateǁ__init____mutmut_1'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁ__init____mutmut['xǁDuuxEdgeClimateǁ__init____mutmut_2'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁ__init____mutmut['xǁDuuxEdgeClimateǁ__init____mutmut_3'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁ__init____mutmut['xǁDuuxEdgeClimateǁ__init____mutmut_4'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁ__init____mutmut['xǁDuuxEdgeClimateǁ__init____mutmut_5'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁ__init____mutmut['xǁDuuxEdgeClimateǁ__init____mutmut_6'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁ__init____mutmut['xǁDuuxEdgeClimateǁ__init____mutmut_7'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁ__init____mutmut['xǁDuuxEdgeClimateǁ__init____mutmut_8'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁ__init____mutmut['xǁDuuxEdgeClimateǁ__init____mutmut_9'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁ__init____mutmut['xǁDuuxEdgeClimateǁ__init____mutmut_10'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁ__init____mutmut_10 # type: ignore # mutmut generated

mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['_mutmut_orig'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_1'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_2'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_3'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_4'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_5'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_6'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_7'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_8'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_9'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_10'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_11'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_12'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_13'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_14'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_15'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_16'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_17'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_18'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_19'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_20'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut['xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_21'] = DuuxEdgeClimate.xǁDuuxEdgeClimateǁasync_set_preset_mode__mutmut_21 # type: ignore # mutmut generated
