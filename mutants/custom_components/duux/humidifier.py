"""Support for Duux de/humidifier devices."""

import logging

from homeassistant.components.humidifier import HumidifierDeviceClass, HumidifierEntity
from homeassistant.components.humidifier.const import (
    MODE_NORMAL,
    HumidifierEntityFeature,
    HumidifierAction,
    MODE_AUTO,
    MODE_BOOST,
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
    DUUX_STID_NEO,
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_orig(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_1(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux de/humidifier entities."""
    data = None
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_2(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux de/humidifier entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = None
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_type_id = device.get("sensorType").get("type")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_3(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux de/humidifier entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["XXapiXX"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_type_id = device.get("sensorType").get("type")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_4(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux de/humidifier entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["API"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_type_id = device.get("sensorType").get("type")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_5(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux de/humidifier entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = None
    devices = data["devices"]

    entities = []
    for device in devices:
        device_type_id = device.get("sensorType").get("type")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_6(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux de/humidifier entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["XXcoordinatorsXX"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_type_id = device.get("sensorType").get("type")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_7(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux de/humidifier entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["COORDINATORS"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_type_id = device.get("sensorType").get("type")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_8(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux de/humidifier entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = None

    entities = []
    for device in devices:
        device_type_id = device.get("sensorType").get("type")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_9(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux de/humidifier entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["XXdevicesXX"]

    entities = []
    for device in devices:
        device_type_id = device.get("sensorType").get("type")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_10(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux de/humidifier entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["DEVICES"]

    entities = []
    for device in devices:
        device_type_id = device.get("sensorType").get("type")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_11(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux de/humidifier entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = None
    for device in devices:
        device_type_id = device.get("sensorType").get("type")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_12(
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
        device_type_id = None
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_13(
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
        device_type_id = device.get("sensorType").get(None)
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_14(
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
        device_type_id = device.get(None).get("type")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_15(
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
        device_type_id = device.get("XXsensorTypeXX").get("type")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_16(
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
        device_type_id = device.get("sensortype").get("type")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_17(
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
        device_type_id = device.get("SENSORTYPE").get("type")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_18(
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
        device_type_id = device.get("sensorType").get("XXtypeXX")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_19(
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
        device_type_id = device.get("sensorType").get("TYPE")
        if device_type_id not in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_20(
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
        if device_type_id in DUUX_DTID_HUMIDIFIER:
            continue

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_21(
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
            break

        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_22(
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

        sensor_type_id = None
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_23(
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

        sensor_type_id = device.get(None)
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_24(
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

        sensor_type_id = device.get("XXsensorTypeIdXX")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_25(
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

        sensor_type_id = device.get("sensortypeid")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_26(
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

        sensor_type_id = device.get("SENSORTYPEID")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_27(
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
        device_id = None
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_28(
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
        device_id = device["XXdeviceIdXX"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_29(
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
        device_id = device["deviceid"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_30(
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
        device_id = device["DEVICEID"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_31(
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
        coordinator = coordinator = None

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_32(
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
        coordinator = coordinator = coordinators.get(None)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_33(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is not None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_34(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            break

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_35(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id != DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_36(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(None)
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_37(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(None, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_38(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, None, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_39(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, None))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_40(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_41(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_42(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, ))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_43(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id != DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_44(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(None)
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_45(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(None, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_46(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, None, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_47(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, None))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_48(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_49(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_50(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, ))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_51(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id != DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_52(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(None)
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_53(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(None, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_54(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, None, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_55(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, None))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_56(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_57(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_58(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, ))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_59(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(None)

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_60(
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
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Create the appropriate de/humidifier entity based on sensor_type_id
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxBoraDehumidifier(coordinator, api, device))
        # Add the Neo to the setup loop
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoHumidifier(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxBeamMiniDehumidifier(coordinator, api, device))
        else:
            _LOGGER.warning(f"Unknown de/humidifier type {sensor_type_id}, skipping.")

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
mutants_xǁDuuxBaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxBaseǁasync_turn_on__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxBaseǁasync_turn_off__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxBaseǁasync_set_humidity__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxBaseǁasync_added_to_hass__mutmut: MutantDict = {}  # type: ignore


class DuuxBase(CoordinatorEntity, HumidifierEntity):
    """Representation of a Duux de/humidifier device."""

    @_mutmut_mutated(mutants_xǁDuuxBaseǁ__init____mutmut)
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

    def xǁDuuxBaseǁ__init____mutmut_orig(self, coordinator, api, device):
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

    def xǁDuuxBaseǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(None)
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

    def xǁDuuxBaseǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = None
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

    def xǁDuuxBaseǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = None
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

    def xǁDuuxBaseǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = None
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["XXidXX"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["ID"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = None  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["XXdeviceIdXX"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceid"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["DEVICEID"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_11(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = None
        self._attr_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_12(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = None
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_13(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") and device.get("name")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_14(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get(None) or device.get("name")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_15(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("XXdisplayNameXX") or device.get("name")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_16(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayname") or device.get("name")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_17(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("DISPLAYNAME") or device.get("name")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_18(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get(None)
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_19(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("XXnameXX")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_20(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("NAME")
        self._attr_has_entity_name = True

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_21(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = None

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_22(self, coordinator, api, device):
        """Initialize the de/humidifier device."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = False

        # Default humidity range (can be overridden by subclasses)
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_23(self, coordinator, api, device):
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
        self._attr_min_humidity = None
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_24(self, coordinator, api, device):
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
        self._attr_min_humidity = 31
        self._attr_max_humidity = 80

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_25(self, coordinator, api, device):
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
        self._attr_max_humidity = None

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_26(self, coordinator, api, device):
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
        self._attr_max_humidity = 81

        # Enable preset 'modes'..
        self._attr_supported_features = HumidifierEntityFeature.MODES

    def xǁDuuxBaseǁ__init____mutmut_27(self, coordinator, api, device):
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
        self._attr_supported_features = None

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

    @_mutmut_mutated(mutants_xǁDuuxBaseǁasync_turn_on__mutmut)
    async def async_turn_on(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["power"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_on__mutmut_orig(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["power"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_on__mutmut_1(self, **kwargs):
        await self.hass.async_add_executor_job(
            None, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["power"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_on__mutmut_2(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, None, True
        )
        newData = self.coordinator.data
        newData["power"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_on__mutmut_3(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["power"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_on__mutmut_4(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._device_mac, True
        )
        newData = self.coordinator.data
        newData["power"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_on__mutmut_5(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, True
        )
        newData = self.coordinator.data
        newData["power"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_on__mutmut_6(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, )
        newData = self.coordinator.data
        newData["power"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_on__mutmut_7(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["power"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_on__mutmut_8(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, True
        )
        newData = None
        newData["power"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_on__mutmut_9(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["power"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_on__mutmut_10(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["XXpowerXX"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_on__mutmut_11(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["POWER"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_on__mutmut_12(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["power"] = 2
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_on__mutmut_13(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["power"] = 1
        self.coordinator.async_set_updated_data(None)

    @_mutmut_mutated(mutants_xǁDuuxBaseǁasync_turn_off__mutmut)
    async def async_turn_off(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["power"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_off__mutmut_orig(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["power"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_off__mutmut_1(self, **kwargs):
        await self.hass.async_add_executor_job(
            None, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["power"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_off__mutmut_2(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, None, False
        )
        newData = self.coordinator.data
        newData["power"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_off__mutmut_3(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["power"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_off__mutmut_4(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._device_mac, False
        )
        newData = self.coordinator.data
        newData["power"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_off__mutmut_5(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, False
        )
        newData = self.coordinator.data
        newData["power"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_off__mutmut_6(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, )
        newData = self.coordinator.data
        newData["power"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_off__mutmut_7(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["power"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_off__mutmut_8(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, False
        )
        newData = None
        newData["power"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_off__mutmut_9(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["power"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_off__mutmut_10(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["XXpowerXX"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_off__mutmut_11(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["POWER"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_off__mutmut_12(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["power"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_turn_off__mutmut_13(self, **kwargs):
        await self.hass.async_add_executor_job(
            self._api.set_power, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["power"] = 0
        self.coordinator.async_set_updated_data(None)

    @property
    def is_on(self):
        power = (self.coordinator.data or {}).get("power", 0)
        return power == 1

    @property
    def action(self):
        """Return current action."""
        # Base implementation - override in subclasses
        pass

    @property
    def current_humidity(self):
        """Return the current humidity."""
        return (self.coordinator.data or {}).get("hum")

    @property
    def target_humidity(self):
        """Return the humidity we try to reach."""
        return (self.coordinator.data or {}).get("sp")

    @_mutmut_mutated(mutants_xǁDuuxBaseǁasync_set_humidity__mutmut)
    async def async_set_humidity(self, humidity: int):
        """Set new target humidity."""
        await self.hass.async_add_executor_job(
            self._api.set_humidity, self._device_mac, humidity
        )
        newData = self.coordinator.data
        newData["sp"] = humidity
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_set_humidity__mutmut_orig(self, humidity: int):
        """Set new target humidity."""
        await self.hass.async_add_executor_job(
            self._api.set_humidity, self._device_mac, humidity
        )
        newData = self.coordinator.data
        newData["sp"] = humidity
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_set_humidity__mutmut_1(self, humidity: int):
        """Set new target humidity."""
        await self.hass.async_add_executor_job(
            None, self._device_mac, humidity
        )
        newData = self.coordinator.data
        newData["sp"] = humidity
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_set_humidity__mutmut_2(self, humidity: int):
        """Set new target humidity."""
        await self.hass.async_add_executor_job(
            self._api.set_humidity, None, humidity
        )
        newData = self.coordinator.data
        newData["sp"] = humidity
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_set_humidity__mutmut_3(self, humidity: int):
        """Set new target humidity."""
        await self.hass.async_add_executor_job(
            self._api.set_humidity, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["sp"] = humidity
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_set_humidity__mutmut_4(self, humidity: int):
        """Set new target humidity."""
        await self.hass.async_add_executor_job(
            self._device_mac, humidity
        )
        newData = self.coordinator.data
        newData["sp"] = humidity
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_set_humidity__mutmut_5(self, humidity: int):
        """Set new target humidity."""
        await self.hass.async_add_executor_job(
            self._api.set_humidity, humidity
        )
        newData = self.coordinator.data
        newData["sp"] = humidity
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_set_humidity__mutmut_6(self, humidity: int):
        """Set new target humidity."""
        await self.hass.async_add_executor_job(
            self._api.set_humidity, self._device_mac, )
        newData = self.coordinator.data
        newData["sp"] = humidity
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_set_humidity__mutmut_7(self, humidity: int):
        """Set new target humidity."""
        await self.hass.async_add_executor_job(
            self._api.set_humidity, self._device_mac, humidity
        )
        newData = None
        newData["sp"] = humidity
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_set_humidity__mutmut_8(self, humidity: int):
        """Set new target humidity."""
        await self.hass.async_add_executor_job(
            self._api.set_humidity, self._device_mac, humidity
        )
        newData = self.coordinator.data
        newData["sp"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_set_humidity__mutmut_9(self, humidity: int):
        """Set new target humidity."""
        await self.hass.async_add_executor_job(
            self._api.set_humidity, self._device_mac, humidity
        )
        newData = self.coordinator.data
        newData["XXspXX"] = humidity
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_set_humidity__mutmut_10(self, humidity: int):
        """Set new target humidity."""
        await self.hass.async_add_executor_job(
            self._api.set_humidity, self._device_mac, humidity
        )
        newData = self.coordinator.data
        newData["SP"] = humidity
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBaseǁasync_set_humidity__mutmut_11(self, humidity: int):
        """Set new target humidity."""
        await self.hass.async_add_executor_job(
            self._api.set_humidity, self._device_mac, humidity
        )
        newData = self.coordinator.data
        newData["sp"] = humidity
        self.coordinator.async_set_updated_data(None)

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

    @_mutmut_mutated(mutants_xǁDuuxBaseǁasync_added_to_hass__mutmut)
    async def async_added_to_hass(self):
        """When entity is added to hass."""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    async def xǁDuuxBaseǁasync_added_to_hass__mutmut_orig(self):
        """When entity is added to hass."""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    async def xǁDuuxBaseǁasync_added_to_hass__mutmut_1(self):
        """When entity is added to hass."""
        self.async_on_remove(
            None
        )

    async def xǁDuuxBaseǁasync_added_to_hass__mutmut_2(self):
        """When entity is added to hass."""
        self.async_on_remove(
            self.coordinator.async_add_listener(None)
        )

    async def async_update(self):
        """Update the entity."""
        await self.coordinator.async_request_refresh()

mutants_xǁDuuxBaseǁ__init____mutmut['_mutmut_orig'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_1'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_2'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_3'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_4'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_5'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_6'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_7'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_8'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_9'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_10'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_11'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_12'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_13'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_14'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_15'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_16'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_17'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_18'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_19'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_20'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_21'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_22'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_23'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_24'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_25'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_26'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁ__init____mutmut['xǁDuuxBaseǁ__init____mutmut_27'] = DuuxBase.xǁDuuxBaseǁ__init____mutmut_27 # type: ignore # mutmut generated

mutants_xǁDuuxBaseǁasync_turn_on__mutmut['_mutmut_orig'] = DuuxBase.xǁDuuxBaseǁasync_turn_on__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_on__mutmut['xǁDuuxBaseǁasync_turn_on__mutmut_1'] = DuuxBase.xǁDuuxBaseǁasync_turn_on__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_on__mutmut['xǁDuuxBaseǁasync_turn_on__mutmut_2'] = DuuxBase.xǁDuuxBaseǁasync_turn_on__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_on__mutmut['xǁDuuxBaseǁasync_turn_on__mutmut_3'] = DuuxBase.xǁDuuxBaseǁasync_turn_on__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_on__mutmut['xǁDuuxBaseǁasync_turn_on__mutmut_4'] = DuuxBase.xǁDuuxBaseǁasync_turn_on__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_on__mutmut['xǁDuuxBaseǁasync_turn_on__mutmut_5'] = DuuxBase.xǁDuuxBaseǁasync_turn_on__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_on__mutmut['xǁDuuxBaseǁasync_turn_on__mutmut_6'] = DuuxBase.xǁDuuxBaseǁasync_turn_on__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_on__mutmut['xǁDuuxBaseǁasync_turn_on__mutmut_7'] = DuuxBase.xǁDuuxBaseǁasync_turn_on__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_on__mutmut['xǁDuuxBaseǁasync_turn_on__mutmut_8'] = DuuxBase.xǁDuuxBaseǁasync_turn_on__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_on__mutmut['xǁDuuxBaseǁasync_turn_on__mutmut_9'] = DuuxBase.xǁDuuxBaseǁasync_turn_on__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_on__mutmut['xǁDuuxBaseǁasync_turn_on__mutmut_10'] = DuuxBase.xǁDuuxBaseǁasync_turn_on__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_on__mutmut['xǁDuuxBaseǁasync_turn_on__mutmut_11'] = DuuxBase.xǁDuuxBaseǁasync_turn_on__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_on__mutmut['xǁDuuxBaseǁasync_turn_on__mutmut_12'] = DuuxBase.xǁDuuxBaseǁasync_turn_on__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_on__mutmut['xǁDuuxBaseǁasync_turn_on__mutmut_13'] = DuuxBase.xǁDuuxBaseǁasync_turn_on__mutmut_13 # type: ignore # mutmut generated

mutants_xǁDuuxBaseǁasync_turn_off__mutmut['_mutmut_orig'] = DuuxBase.xǁDuuxBaseǁasync_turn_off__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_off__mutmut['xǁDuuxBaseǁasync_turn_off__mutmut_1'] = DuuxBase.xǁDuuxBaseǁasync_turn_off__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_off__mutmut['xǁDuuxBaseǁasync_turn_off__mutmut_2'] = DuuxBase.xǁDuuxBaseǁasync_turn_off__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_off__mutmut['xǁDuuxBaseǁasync_turn_off__mutmut_3'] = DuuxBase.xǁDuuxBaseǁasync_turn_off__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_off__mutmut['xǁDuuxBaseǁasync_turn_off__mutmut_4'] = DuuxBase.xǁDuuxBaseǁasync_turn_off__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_off__mutmut['xǁDuuxBaseǁasync_turn_off__mutmut_5'] = DuuxBase.xǁDuuxBaseǁasync_turn_off__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_off__mutmut['xǁDuuxBaseǁasync_turn_off__mutmut_6'] = DuuxBase.xǁDuuxBaseǁasync_turn_off__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_off__mutmut['xǁDuuxBaseǁasync_turn_off__mutmut_7'] = DuuxBase.xǁDuuxBaseǁasync_turn_off__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_off__mutmut['xǁDuuxBaseǁasync_turn_off__mutmut_8'] = DuuxBase.xǁDuuxBaseǁasync_turn_off__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_off__mutmut['xǁDuuxBaseǁasync_turn_off__mutmut_9'] = DuuxBase.xǁDuuxBaseǁasync_turn_off__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_off__mutmut['xǁDuuxBaseǁasync_turn_off__mutmut_10'] = DuuxBase.xǁDuuxBaseǁasync_turn_off__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_off__mutmut['xǁDuuxBaseǁasync_turn_off__mutmut_11'] = DuuxBase.xǁDuuxBaseǁasync_turn_off__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_off__mutmut['xǁDuuxBaseǁasync_turn_off__mutmut_12'] = DuuxBase.xǁDuuxBaseǁasync_turn_off__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_turn_off__mutmut['xǁDuuxBaseǁasync_turn_off__mutmut_13'] = DuuxBase.xǁDuuxBaseǁasync_turn_off__mutmut_13 # type: ignore # mutmut generated

mutants_xǁDuuxBaseǁasync_set_humidity__mutmut['_mutmut_orig'] = DuuxBase.xǁDuuxBaseǁasync_set_humidity__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_set_humidity__mutmut['xǁDuuxBaseǁasync_set_humidity__mutmut_1'] = DuuxBase.xǁDuuxBaseǁasync_set_humidity__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_set_humidity__mutmut['xǁDuuxBaseǁasync_set_humidity__mutmut_2'] = DuuxBase.xǁDuuxBaseǁasync_set_humidity__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_set_humidity__mutmut['xǁDuuxBaseǁasync_set_humidity__mutmut_3'] = DuuxBase.xǁDuuxBaseǁasync_set_humidity__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_set_humidity__mutmut['xǁDuuxBaseǁasync_set_humidity__mutmut_4'] = DuuxBase.xǁDuuxBaseǁasync_set_humidity__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_set_humidity__mutmut['xǁDuuxBaseǁasync_set_humidity__mutmut_5'] = DuuxBase.xǁDuuxBaseǁasync_set_humidity__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_set_humidity__mutmut['xǁDuuxBaseǁasync_set_humidity__mutmut_6'] = DuuxBase.xǁDuuxBaseǁasync_set_humidity__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_set_humidity__mutmut['xǁDuuxBaseǁasync_set_humidity__mutmut_7'] = DuuxBase.xǁDuuxBaseǁasync_set_humidity__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_set_humidity__mutmut['xǁDuuxBaseǁasync_set_humidity__mutmut_8'] = DuuxBase.xǁDuuxBaseǁasync_set_humidity__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_set_humidity__mutmut['xǁDuuxBaseǁasync_set_humidity__mutmut_9'] = DuuxBase.xǁDuuxBaseǁasync_set_humidity__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_set_humidity__mutmut['xǁDuuxBaseǁasync_set_humidity__mutmut_10'] = DuuxBase.xǁDuuxBaseǁasync_set_humidity__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_set_humidity__mutmut['xǁDuuxBaseǁasync_set_humidity__mutmut_11'] = DuuxBase.xǁDuuxBaseǁasync_set_humidity__mutmut_11 # type: ignore # mutmut generated

mutants_xǁDuuxBaseǁasync_added_to_hass__mutmut['_mutmut_orig'] = DuuxBase.xǁDuuxBaseǁasync_added_to_hass__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_added_to_hass__mutmut['xǁDuuxBaseǁasync_added_to_hass__mutmut_1'] = DuuxBase.xǁDuuxBaseǁasync_added_to_hass__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxBaseǁasync_added_to_hass__mutmut['xǁDuuxBaseǁasync_added_to_hass__mutmut_2'] = DuuxBase.xǁDuuxBaseǁasync_added_to_hass__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxDehumidifierǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxDehumidifier(DuuxBase):
    """Representation of a Duux dehumidifier device."""

    @_mutmut_mutated(mutants_xǁDuuxDehumidifierǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the dehumidifier device."""
        super().__init__(coordinator, api, device)

        self._attr_device_class = HumidifierDeviceClass.DEHUMIDIFIER

    def xǁDuuxDehumidifierǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the dehumidifier device."""
        super().__init__(coordinator, api, device)

        self._attr_device_class = HumidifierDeviceClass.DEHUMIDIFIER

    def xǁDuuxDehumidifierǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the dehumidifier device."""
        super().__init__(None, api, device)

        self._attr_device_class = HumidifierDeviceClass.DEHUMIDIFIER

    def xǁDuuxDehumidifierǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the dehumidifier device."""
        super().__init__(coordinator, None, device)

        self._attr_device_class = HumidifierDeviceClass.DEHUMIDIFIER

    def xǁDuuxDehumidifierǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the dehumidifier device."""
        super().__init__(coordinator, api, None)

        self._attr_device_class = HumidifierDeviceClass.DEHUMIDIFIER

    def xǁDuuxDehumidifierǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the dehumidifier device."""
        super().__init__(api, device)

        self._attr_device_class = HumidifierDeviceClass.DEHUMIDIFIER

    def xǁDuuxDehumidifierǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the dehumidifier device."""
        super().__init__(coordinator, device)

        self._attr_device_class = HumidifierDeviceClass.DEHUMIDIFIER

    def xǁDuuxDehumidifierǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the dehumidifier device."""
        super().__init__(coordinator, api, )

        self._attr_device_class = HumidifierDeviceClass.DEHUMIDIFIER

    def xǁDuuxDehumidifierǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the dehumidifier device."""
        super().__init__(coordinator, api, device)

        self._attr_device_class = None

    @property
    def action(self):
        """Return current action."""
        power = self.coordinator.data.get("power", 0)
        return HumidifierAction.DRYING if power == 1 else HumidifierAction.OFF

mutants_xǁDuuxDehumidifierǁ__init____mutmut['_mutmut_orig'] = DuuxDehumidifier.xǁDuuxDehumidifierǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxDehumidifierǁ__init____mutmut['xǁDuuxDehumidifierǁ__init____mutmut_1'] = DuuxDehumidifier.xǁDuuxDehumidifierǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxDehumidifierǁ__init____mutmut['xǁDuuxDehumidifierǁ__init____mutmut_2'] = DuuxDehumidifier.xǁDuuxDehumidifierǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxDehumidifierǁ__init____mutmut['xǁDuuxDehumidifierǁ__init____mutmut_3'] = DuuxDehumidifier.xǁDuuxDehumidifierǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxDehumidifierǁ__init____mutmut['xǁDuuxDehumidifierǁ__init____mutmut_4'] = DuuxDehumidifier.xǁDuuxDehumidifierǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxDehumidifierǁ__init____mutmut['xǁDuuxDehumidifierǁ__init____mutmut_5'] = DuuxDehumidifier.xǁDuuxDehumidifierǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxDehumidifierǁ__init____mutmut['xǁDuuxDehumidifierǁ__init____mutmut_6'] = DuuxDehumidifier.xǁDuuxDehumidifierǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxDehumidifierǁ__init____mutmut['xǁDuuxDehumidifierǁ__init____mutmut_7'] = DuuxDehumidifier.xǁDuuxDehumidifierǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxHumidifierǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxHumidifier(DuuxBase):
    """Representation of a Duux humidifier device."""

    @_mutmut_mutated(mutants_xǁDuuxHumidifierǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the humidifier device."""
        super().__init__(coordinator, api, device)

        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

    def xǁDuuxHumidifierǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the humidifier device."""
        super().__init__(coordinator, api, device)

        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

    def xǁDuuxHumidifierǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the humidifier device."""
        super().__init__(None, api, device)

        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

    def xǁDuuxHumidifierǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the humidifier device."""
        super().__init__(coordinator, None, device)

        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

    def xǁDuuxHumidifierǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the humidifier device."""
        super().__init__(coordinator, api, None)

        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

    def xǁDuuxHumidifierǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the humidifier device."""
        super().__init__(api, device)

        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

    def xǁDuuxHumidifierǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the humidifier device."""
        super().__init__(coordinator, device)

        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

    def xǁDuuxHumidifierǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the humidifier device."""
        super().__init__(coordinator, api, )

        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

    def xǁDuuxHumidifierǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the humidifier device."""
        super().__init__(coordinator, api, device)

        self._attr_device_class = None

    @property
    def action(self):
        """Return current action."""
        power = self.coordinator.data.get("power", 0)
        return HumidifierAction.HUMIDIFYING if power == 1 else HumidifierAction.OFF

mutants_xǁDuuxHumidifierǁ__init____mutmut['_mutmut_orig'] = DuuxHumidifier.xǁDuuxHumidifierǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxHumidifierǁ__init____mutmut['xǁDuuxHumidifierǁ__init____mutmut_1'] = DuuxHumidifier.xǁDuuxHumidifierǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxHumidifierǁ__init____mutmut['xǁDuuxHumidifierǁ__init____mutmut_2'] = DuuxHumidifier.xǁDuuxHumidifierǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxHumidifierǁ__init____mutmut['xǁDuuxHumidifierǁ__init____mutmut_3'] = DuuxHumidifier.xǁDuuxHumidifierǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxHumidifierǁ__init____mutmut['xǁDuuxHumidifierǁ__init____mutmut_4'] = DuuxHumidifier.xǁDuuxHumidifierǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxHumidifierǁ__init____mutmut['xǁDuuxHumidifierǁ__init____mutmut_5'] = DuuxHumidifier.xǁDuuxHumidifierǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxHumidifierǁ__init____mutmut['xǁDuuxHumidifierǁ__init____mutmut_6'] = DuuxHumidifier.xǁDuuxHumidifierǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxHumidifierǁ__init____mutmut['xǁDuuxHumidifierǁ__init____mutmut_7'] = DuuxHumidifier.xǁDuuxHumidifierǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut: MutantDict = {}  # type: ignore


class DuuxBoraDehumidifier(DuuxDehumidifier):
    """Duux Bora Dehumidifier."""

    PRESET_AUTO = MODE_AUTO
    PRESET_CONTINUOUS = MODE_BOOST

    @_mutmut_mutated(mutants_xǁDuuxBoraDehumidifierǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the Bora dehumidifier device."""
        super().__init__(coordinator, api, device)

        # min/max humidity settings for Bora.
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxBoraDehumidifierǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the Bora dehumidifier device."""
        super().__init__(coordinator, api, device)

        # min/max humidity settings for Bora.
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxBoraDehumidifierǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the Bora dehumidifier device."""
        super().__init__(None, api, device)

        # min/max humidity settings for Bora.
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxBoraDehumidifierǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the Bora dehumidifier device."""
        super().__init__(coordinator, None, device)

        # min/max humidity settings for Bora.
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxBoraDehumidifierǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the Bora dehumidifier device."""
        super().__init__(coordinator, api, None)

        # min/max humidity settings for Bora.
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxBoraDehumidifierǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the Bora dehumidifier device."""
        super().__init__(api, device)

        # min/max humidity settings for Bora.
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxBoraDehumidifierǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the Bora dehumidifier device."""
        super().__init__(coordinator, device)

        # min/max humidity settings for Bora.
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxBoraDehumidifierǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the Bora dehumidifier device."""
        super().__init__(coordinator, api, )

        # min/max humidity settings for Bora.
        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxBoraDehumidifierǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the Bora dehumidifier device."""
        super().__init__(coordinator, api, device)

        # min/max humidity settings for Bora.
        self._attr_min_humidity = None
        self._attr_max_humidity = 80

    def xǁDuuxBoraDehumidifierǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the Bora dehumidifier device."""
        super().__init__(coordinator, api, device)

        # min/max humidity settings for Bora.
        self._attr_min_humidity = 31
        self._attr_max_humidity = 80

    def xǁDuuxBoraDehumidifierǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the Bora dehumidifier device."""
        super().__init__(coordinator, api, device)

        # min/max humidity settings for Bora.
        self._attr_min_humidity = 30
        self._attr_max_humidity = None

    def xǁDuuxBoraDehumidifierǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the Bora dehumidifier device."""
        super().__init__(coordinator, api, device)

        # min/max humidity settings for Bora.
        self._attr_min_humidity = 30
        self._attr_max_humidity = 81

    @property
    def available_modes(self):
        """Return available preset modes."""
        return [self.PRESET_AUTO, self.PRESET_CONTINUOUS]

    @property
    def mode(self):
        """Return current preset mode."""
        mode = (self.coordinator.data or {}).get("mode", self.PRESET_AUTO)
        mode_map = {
            0: self.PRESET_AUTO,
            1: self.PRESET_CONTINUOUS,
        }
        return mode_map.get(mode, self.PRESET_AUTO)

    @_mutmut_mutated(mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut)
    async def async_set_mode(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_orig(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_1(self, mode):
        """Set preset mode."""
        mode_map = None

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_2(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "XX0XX", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_3(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "XX1XX"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_4(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = None

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_5(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(None, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_6(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, None)

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_7(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get("0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_8(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, )

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_9(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "XX0XX")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_10(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            None, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_11(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, None, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_12(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_13(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_14(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_15(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_16(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = None
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_17(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_18(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["XXmodeXX"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_19(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["MODE"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_20(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(None)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_21(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_CONTINUOUS: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(None)

mutants_xǁDuuxBoraDehumidifierǁ__init____mutmut['_mutmut_orig'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁ__init____mutmut['xǁDuuxBoraDehumidifierǁ__init____mutmut_1'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁ__init____mutmut['xǁDuuxBoraDehumidifierǁ__init____mutmut_2'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁ__init____mutmut['xǁDuuxBoraDehumidifierǁ__init____mutmut_3'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁ__init____mutmut['xǁDuuxBoraDehumidifierǁ__init____mutmut_4'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁ__init____mutmut['xǁDuuxBoraDehumidifierǁ__init____mutmut_5'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁ__init____mutmut['xǁDuuxBoraDehumidifierǁ__init____mutmut_6'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁ__init____mutmut['xǁDuuxBoraDehumidifierǁ__init____mutmut_7'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁ__init____mutmut['xǁDuuxBoraDehumidifierǁ__init____mutmut_8'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁ__init____mutmut['xǁDuuxBoraDehumidifierǁ__init____mutmut_9'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁ__init____mutmut['xǁDuuxBoraDehumidifierǁ__init____mutmut_10'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁ__init____mutmut_10 # type: ignore # mutmut generated

mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['_mutmut_orig'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_1'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_2'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_3'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_4'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_5'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_6'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_7'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_8'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_9'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_10'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_11'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_12'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_13'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_14'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_15'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_16'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_17'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_18'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_19'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_20'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut['xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_21'] = DuuxBoraDehumidifier.xǁDuuxBoraDehumidifierǁasync_set_mode__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut: MutantDict = {}  # type: ignore


class DuuxBeamMiniDehumidifier(DuuxHumidifier):
    """Duux Beam Mini Humidifier."""

    PRESET_AUTO = MODE_AUTO
    PRESET_MANUAL = MODE_NORMAL

    @_mutmut_mutated(mutants_xǁDuuxBeamMiniDehumidifierǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the Beam Mini humidifier device."""
        super().__init__(coordinator, api, device)

        # min/max humidity settings for Beam Mini.
        self._attr_min_humidity = 20
        self._attr_max_humidity = 80

    def xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the Beam Mini humidifier device."""
        super().__init__(coordinator, api, device)

        # min/max humidity settings for Beam Mini.
        self._attr_min_humidity = 20
        self._attr_max_humidity = 80

    def xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the Beam Mini humidifier device."""
        super().__init__(None, api, device)

        # min/max humidity settings for Beam Mini.
        self._attr_min_humidity = 20
        self._attr_max_humidity = 80

    def xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the Beam Mini humidifier device."""
        super().__init__(coordinator, None, device)

        # min/max humidity settings for Beam Mini.
        self._attr_min_humidity = 20
        self._attr_max_humidity = 80

    def xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the Beam Mini humidifier device."""
        super().__init__(coordinator, api, None)

        # min/max humidity settings for Beam Mini.
        self._attr_min_humidity = 20
        self._attr_max_humidity = 80

    def xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the Beam Mini humidifier device."""
        super().__init__(api, device)

        # min/max humidity settings for Beam Mini.
        self._attr_min_humidity = 20
        self._attr_max_humidity = 80

    def xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the Beam Mini humidifier device."""
        super().__init__(coordinator, device)

        # min/max humidity settings for Beam Mini.
        self._attr_min_humidity = 20
        self._attr_max_humidity = 80

    def xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the Beam Mini humidifier device."""
        super().__init__(coordinator, api, )

        # min/max humidity settings for Beam Mini.
        self._attr_min_humidity = 20
        self._attr_max_humidity = 80

    def xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the Beam Mini humidifier device."""
        super().__init__(coordinator, api, device)

        # min/max humidity settings for Beam Mini.
        self._attr_min_humidity = None
        self._attr_max_humidity = 80

    def xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the Beam Mini humidifier device."""
        super().__init__(coordinator, api, device)

        # min/max humidity settings for Beam Mini.
        self._attr_min_humidity = 21
        self._attr_max_humidity = 80

    def xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the Beam Mini humidifier device."""
        super().__init__(coordinator, api, device)

        # min/max humidity settings for Beam Mini.
        self._attr_min_humidity = 20
        self._attr_max_humidity = None

    def xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the Beam Mini humidifier device."""
        super().__init__(coordinator, api, device)

        # min/max humidity settings for Beam Mini.
        self._attr_min_humidity = 20
        self._attr_max_humidity = 81

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

    @_mutmut_mutated(mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut)
    async def async_set_mode(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_orig(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_1(self, mode):
        """Set preset mode."""
        mode_map = None

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_2(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "XX0XX", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_3(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "XX1XX"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_4(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = None

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_5(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(None, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_6(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, None)

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_7(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get("0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_8(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, )

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_9(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "XX0XX")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_10(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            None, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_11(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, None, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_12(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_13(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_14(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_15(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_16(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = None
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_17(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_18(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["XXmodeXX"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_19(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["MODE"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_20(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(None)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_21(self, mode):
        """Set preset mode."""
        mode_map = {self.PRESET_AUTO: "0", self.PRESET_MANUAL: "1"}

        mode = mode_map.get(mode, "0")

        await self.hass.async_add_executor_job(
            self._api.set_dry_mode, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["mode"] = int(mode)
        self.coordinator.async_set_updated_data(None)

mutants_xǁDuuxBeamMiniDehumidifierǁ__init____mutmut['_mutmut_orig'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁ__init____mutmut['xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_1'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁ__init____mutmut['xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_2'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁ__init____mutmut['xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_3'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁ__init____mutmut['xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_4'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁ__init____mutmut['xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_5'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁ__init____mutmut['xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_6'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁ__init____mutmut['xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_7'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁ__init____mutmut['xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_8'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁ__init____mutmut['xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_9'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁ__init____mutmut['xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_10'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁ__init____mutmut_10 # type: ignore # mutmut generated

mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['_mutmut_orig'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_1'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_2'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_3'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_4'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_5'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_6'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_7'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_8'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_9'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_10'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_11'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_12'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_13'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_14'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_15'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_16'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_17'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_18'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_19'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_20'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut['xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_21'] = DuuxBeamMiniDehumidifier.xǁDuuxBeamMiniDehumidifierǁasync_set_mode__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut: MutantDict = {}  # type: ignore


class DuuxNeoHumidifier(DuuxDehumidifier):
    """Duux Neo Humidifier."""

    PRESET_NORMAL = MODE_NORMAL
    PRESET_AUTO = MODE_AUTO

    @_mutmut_mutated(mutants_xǁDuuxNeoHumidifierǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the Neo humidifier device."""
        super().__init__(coordinator, api, device)
        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

        # Explicitly tell Home Assistant this device supports modes
        self._attr_supported_features = HumidifierEntityFeature.MODES

        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxNeoHumidifierǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the Neo humidifier device."""
        super().__init__(coordinator, api, device)
        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

        # Explicitly tell Home Assistant this device supports modes
        self._attr_supported_features = HumidifierEntityFeature.MODES

        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxNeoHumidifierǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the Neo humidifier device."""
        super().__init__(None, api, device)
        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

        # Explicitly tell Home Assistant this device supports modes
        self._attr_supported_features = HumidifierEntityFeature.MODES

        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxNeoHumidifierǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the Neo humidifier device."""
        super().__init__(coordinator, None, device)
        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

        # Explicitly tell Home Assistant this device supports modes
        self._attr_supported_features = HumidifierEntityFeature.MODES

        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxNeoHumidifierǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the Neo humidifier device."""
        super().__init__(coordinator, api, None)
        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

        # Explicitly tell Home Assistant this device supports modes
        self._attr_supported_features = HumidifierEntityFeature.MODES

        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxNeoHumidifierǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the Neo humidifier device."""
        super().__init__(api, device)
        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

        # Explicitly tell Home Assistant this device supports modes
        self._attr_supported_features = HumidifierEntityFeature.MODES

        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxNeoHumidifierǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the Neo humidifier device."""
        super().__init__(coordinator, device)
        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

        # Explicitly tell Home Assistant this device supports modes
        self._attr_supported_features = HumidifierEntityFeature.MODES

        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxNeoHumidifierǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the Neo humidifier device."""
        super().__init__(coordinator, api, )
        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

        # Explicitly tell Home Assistant this device supports modes
        self._attr_supported_features = HumidifierEntityFeature.MODES

        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxNeoHumidifierǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the Neo humidifier device."""
        super().__init__(coordinator, api, device)
        self._attr_device_class = None

        # Explicitly tell Home Assistant this device supports modes
        self._attr_supported_features = HumidifierEntityFeature.MODES

        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxNeoHumidifierǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the Neo humidifier device."""
        super().__init__(coordinator, api, device)
        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

        # Explicitly tell Home Assistant this device supports modes
        self._attr_supported_features = None

        self._attr_min_humidity = 30
        self._attr_max_humidity = 80

    def xǁDuuxNeoHumidifierǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the Neo humidifier device."""
        super().__init__(coordinator, api, device)
        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

        # Explicitly tell Home Assistant this device supports modes
        self._attr_supported_features = HumidifierEntityFeature.MODES

        self._attr_min_humidity = None
        self._attr_max_humidity = 80

    def xǁDuuxNeoHumidifierǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the Neo humidifier device."""
        super().__init__(coordinator, api, device)
        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

        # Explicitly tell Home Assistant this device supports modes
        self._attr_supported_features = HumidifierEntityFeature.MODES

        self._attr_min_humidity = 31
        self._attr_max_humidity = 80

    def xǁDuuxNeoHumidifierǁ__init____mutmut_11(self, coordinator, api, device):
        """Initialize the Neo humidifier device."""
        super().__init__(coordinator, api, device)
        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

        # Explicitly tell Home Assistant this device supports modes
        self._attr_supported_features = HumidifierEntityFeature.MODES

        self._attr_min_humidity = 30
        self._attr_max_humidity = None

    def xǁDuuxNeoHumidifierǁ__init____mutmut_12(self, coordinator, api, device):
        """Initialize the Neo humidifier device."""
        super().__init__(coordinator, api, device)
        self._attr_device_class = HumidifierDeviceClass.HUMIDIFIER

        # Explicitly tell Home Assistant this device supports modes
        self._attr_supported_features = HumidifierEntityFeature.MODES

        self._attr_min_humidity = 30
        self._attr_max_humidity = 81

    @property
    def action(self):
        """Return the current action of the humidifier."""
        is_on = bool(self.coordinator.data.get("power"))
        if not is_on:
            return HumidifierAction.OFF

        current_hum = self.coordinator.data.get("hum")
        target_hum = self.coordinator.data.get("sp")

        if (
            current_hum is not None
            and target_hum is not None
            and current_hum < target_hum
        ):
            return HumidifierAction.HUMIDIFYING

        return HumidifierAction.IDLE

    @property
    def available_modes(self):
        """Return available preset modes."""
        return [self.PRESET_NORMAL, self.PRESET_AUTO]

    @property
    def mode(self):
        """Return current preset mode."""
        mode = self.coordinator.data.get("mode")

        # Safely convert to string to handle both int(1) and str("1") from the API
        if str(mode) == "1":
            return self.PRESET_AUTO
        return self.PRESET_NORMAL

    @_mutmut_mutated(mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut)
    async def async_set_mode(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "1" if mode == self.PRESET_AUTO else "0"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._api.set_humidifier_mode,
            self._device_mac,
            api_mode,
        )
        newData = self.coordinator.data
        newData["mode"] = api_mode
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_orig(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "1" if mode == self.PRESET_AUTO else "0"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._api.set_humidifier_mode,
            self._device_mac,
            api_mode,
        )
        newData = self.coordinator.data
        newData["mode"] = api_mode
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_1(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = None

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._api.set_humidifier_mode,
            self._device_mac,
            api_mode,
        )
        newData = self.coordinator.data
        newData["mode"] = api_mode
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_2(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "XX1XX" if mode == self.PRESET_AUTO else "0"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._api.set_humidifier_mode,
            self._device_mac,
            api_mode,
        )
        newData = self.coordinator.data
        newData["mode"] = api_mode
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_3(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "1" if mode != self.PRESET_AUTO else "0"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._api.set_humidifier_mode,
            self._device_mac,
            api_mode,
        )
        newData = self.coordinator.data
        newData["mode"] = api_mode
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_4(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "1" if mode == self.PRESET_AUTO else "XX0XX"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._api.set_humidifier_mode,
            self._device_mac,
            api_mode,
        )
        newData = self.coordinator.data
        newData["mode"] = api_mode
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_5(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "1" if mode == self.PRESET_AUTO else "0"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            None,
            self._device_mac,
            api_mode,
        )
        newData = self.coordinator.data
        newData["mode"] = api_mode
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_6(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "1" if mode == self.PRESET_AUTO else "0"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._api.set_humidifier_mode,
            None,
            api_mode,
        )
        newData = self.coordinator.data
        newData["mode"] = api_mode
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_7(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "1" if mode == self.PRESET_AUTO else "0"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._api.set_humidifier_mode,
            self._device_mac,
            None,
        )
        newData = self.coordinator.data
        newData["mode"] = api_mode
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_8(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "1" if mode == self.PRESET_AUTO else "0"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._device_mac,
            api_mode,
        )
        newData = self.coordinator.data
        newData["mode"] = api_mode
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_9(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "1" if mode == self.PRESET_AUTO else "0"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._api.set_humidifier_mode,
            api_mode,
        )
        newData = self.coordinator.data
        newData["mode"] = api_mode
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_10(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "1" if mode == self.PRESET_AUTO else "0"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._api.set_humidifier_mode,
            self._device_mac,
            )
        newData = self.coordinator.data
        newData["mode"] = api_mode
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_11(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "1" if mode == self.PRESET_AUTO else "0"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._api.set_humidifier_mode,
            self._device_mac,
            api_mode,
        )
        newData = None
        newData["mode"] = api_mode
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_12(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "1" if mode == self.PRESET_AUTO else "0"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._api.set_humidifier_mode,
            self._device_mac,
            api_mode,
        )
        newData = self.coordinator.data
        newData["mode"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_13(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "1" if mode == self.PRESET_AUTO else "0"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._api.set_humidifier_mode,
            self._device_mac,
            api_mode,
        )
        newData = self.coordinator.data
        newData["XXmodeXX"] = api_mode
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_14(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "1" if mode == self.PRESET_AUTO else "0"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._api.set_humidifier_mode,
            self._device_mac,
            api_mode,
        )
        newData = self.coordinator.data
        newData["MODE"] = api_mode
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_15(self, mode):
        """Set preset mode."""
        # Convert Home Assistant mode back to the API value
        api_mode = "1" if mode == self.PRESET_AUTO else "0"

        await self.hass.async_add_executor_job(
            # Use the new API function we just created
            self._api.set_humidifier_mode,
            self._device_mac,
            api_mode,
        )
        newData = self.coordinator.data
        newData["mode"] = api_mode
        self.coordinator.async_set_updated_data(None)

    @property
    def extra_state_attributes(self):
        """Return device specific state attributes."""
        data = self.coordinator.data
        speed_val = data.get("speed")
        speed_map = {0: "Low", 1: "Mid", 2: "High"}

        attrs = {}
        if speed_val is not None:
            attrs["spray_volume"] = speed_map.get(
                int(speed_val), f"Unknown ({speed_val})"
            )

        return attrs

mutants_xǁDuuxNeoHumidifierǁ__init____mutmut['_mutmut_orig'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁ__init____mutmut['xǁDuuxNeoHumidifierǁ__init____mutmut_1'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁ__init____mutmut['xǁDuuxNeoHumidifierǁ__init____mutmut_2'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁ__init____mutmut['xǁDuuxNeoHumidifierǁ__init____mutmut_3'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁ__init____mutmut['xǁDuuxNeoHumidifierǁ__init____mutmut_4'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁ__init____mutmut['xǁDuuxNeoHumidifierǁ__init____mutmut_5'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁ__init____mutmut['xǁDuuxNeoHumidifierǁ__init____mutmut_6'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁ__init____mutmut['xǁDuuxNeoHumidifierǁ__init____mutmut_7'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁ__init____mutmut['xǁDuuxNeoHumidifierǁ__init____mutmut_8'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁ__init____mutmut['xǁDuuxNeoHumidifierǁ__init____mutmut_9'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁ__init____mutmut['xǁDuuxNeoHumidifierǁ__init____mutmut_10'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁ__init____mutmut['xǁDuuxNeoHumidifierǁ__init____mutmut_11'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁ__init____mutmut['xǁDuuxNeoHumidifierǁ__init____mutmut_12'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁ__init____mutmut_12 # type: ignore # mutmut generated

mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['_mutmut_orig'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_1'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_2'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_3'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_4'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_5'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_6'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_7'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_8'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_9'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_10'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_11'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_12'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_13'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_14'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxNeoHumidifierǁasync_set_mode__mutmut['xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_15'] = DuuxNeoHumidifier.xǁDuuxNeoHumidifierǁasync_set_mode__mutmut_15 # type: ignore # mutmut generated
