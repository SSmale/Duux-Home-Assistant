"""Support for Duux switches."""

import logging

from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from custom_components.duux.const import (
    DOMAIN,
    DUUX_STID_BORA_2024,
    DUUX_STID_BRIGHT_2,
    DUUX_STID_EDGEHEATER_2000,
    DUUX_STID_EDGEHEATER_2023_V1,
    DUUX_STID_EDGEHEATER_V2,
    DUUX_STID_WHISPER_FLEX_2,
    DUUX_STID_WHISPER_FLEX_ELIVATE,
    DUUX_STID_NEO,
)

_LOGGER = logging.getLogger(__name__)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_async_setup_entry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_async_setup_entry__mutmut)
async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_orig(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_1(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = None
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_2(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = None
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_3(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["XXapiXX"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_4(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["API"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_5(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = None
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_6(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["XXcoordinatorsXX"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_7(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["COORDINATORS"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_8(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = None

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_9(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["XXdevicesXX"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_10(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["DEVICES"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_11(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = None
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_12(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = None
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_13(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get(None)
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_14(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("XXsensorTypeIdXX")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_15(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensortypeid")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_16(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("SENSORTYPEID")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_17(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = None
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_18(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["XXdeviceIdXX"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_19(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceid"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_20(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["DEVICEID"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_21(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = None

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_22(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(None)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_23(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is not None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_24(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            break

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_25(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id not in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_26(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(None)
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_27(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(None, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_28(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, None, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_29(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, None))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_30(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_31(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_32(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, ))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_33(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(None)
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_34(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(None, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_35(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, None, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_36(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, None))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_37(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_38(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_39(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, ))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_40(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_41(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(None)
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_42(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(None, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_43(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, None, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_44(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, None))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_45(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_46(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_47(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, ))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_48(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(None)

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_49(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(None, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_50(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, None, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_51(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, None))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_52(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_53(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_54(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, ))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_55(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id != DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_56(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(None)
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_57(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(None, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_58(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, None, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_59(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, None))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_60(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_61(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_62(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, ))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_63(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(None)
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_64(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(None, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_65(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, None, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_66(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, None))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_67(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_68(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_69(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, ))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_70(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(None)
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_71(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(None, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_72(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, None, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_73(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, None))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_74(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_75(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_76(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, ))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_77(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(None)
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_78(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(None, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_79(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, None, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_80(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, None))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_81(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_82(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_83(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, ))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_84(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id != DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_85(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(None)

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_86(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(None, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_87(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, None, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_88(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, None))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_89(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_90(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_91(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, ))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_92(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id != DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_93(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(None)
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_94(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(None, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_95(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, None, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_96(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, None))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_97(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_98(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_99(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, ))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_100(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(None)

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_101(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(None, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_102(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, None, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_103(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, None))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_104(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_105(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_106(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, ))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_107(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id != DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_108(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(None)
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_109(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(None, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_110(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, None, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_111(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, None))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_112(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_113(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_114(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, ))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_115(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(None)

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_116(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(None, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_117(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, None, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_118(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, None))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_119(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_120(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_121(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, ))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_122(hass, config_entry, async_add_entities):
    """Set up Duux switch entities from a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        # Only Edge heaters have night mode
        if sensor_type_id in [
            DUUX_STID_EDGEHEATER_2023_V1,
            DUUX_STID_EDGEHEATER_V2,
            DUUX_STID_EDGEHEATER_2000,
            DUUX_STID_WHISPER_FLEX_2,
        ]:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
        if sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE,
        ]:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        # Bora has sleep (similar to night), cleaning, laundry & child lock..
        elif sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxChildLockSwitch(coordinator, api, device))
            entities.append(DuuxSleepModeSwitch(coordinator, api, device))
            entities.append(DuuxCleaningModeSwitch(coordinator, api, device))
            entities.append(DuuxLaundryModeSwitch(coordinator, api, device))
        # Neo humidifier
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxNightModeSwitch(coordinator, api, device))
            entities.append(DuuxIonizerSwitch(coordinator, api, device))

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
mutants_xǁDuuxSwitchǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxSwitch(CoordinatorEntity, SwitchEntity):
    """Base class for Duux switches."""

    @_mutmut_mutated(mutants_xǁDuuxSwitchǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(None)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = None
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = None
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = None
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["XXidXX"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["ID"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = None  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["XXdeviceIdXX"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceid"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["DEVICEID"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_11(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = None
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_12(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = None
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_13(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") and device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_14(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get(None) or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_15(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("XXdisplayNameXX") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_16(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayname") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_17(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("DISPLAYNAME") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_18(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get(None)
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_19(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("XXnameXX")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_20(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("NAME")
        self._attr_has_entity_name = True

    def xǁDuuxSwitchǁ__init____mutmut_21(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = None

    def xǁDuuxSwitchǁ__init____mutmut_22(self, coordinator, api, device):
        """Initialize the switch."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = False

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self.coordinator.last_update_success and (
            self.coordinator.data or {}
        ).get("online", True)

    @property
    def device_info(self):
        """Return device information."""
        return {
            "identifiers": {(DOMAIN, str(self._device_id))},
            "name": self.device_name,
            "manufacturer": self._device.get("manufacturer", "Duux"),
            "model": self._device.get("sensorType", {}).get("name", "Unknown"),
        }

mutants_xǁDuuxSwitchǁ__init____mutmut['_mutmut_orig'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_1'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_2'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_3'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_4'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_5'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_6'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_7'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_8'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_9'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_10'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_11'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_12'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_13'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_14'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_15'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_16'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_17'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_18'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_19'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_20'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_21'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxSwitchǁ__init____mutmut['xǁDuuxSwitchǁ__init____mutmut_22'] = DuuxSwitch.xǁDuuxSwitchǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut: MutantDict = {}  # type: ignore


class DuuxChildLockSwitch(DuuxSwitch):
    """Representation of a Duux child lock switch."""

    @_mutmut_mutated(mutants_xǁDuuxChildLockSwitchǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_translation_key = "child_lock"
        self._attr_icon = "mdi:lock"

    def xǁDuuxChildLockSwitchǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_translation_key = "child_lock"
        self._attr_icon = "mdi:lock"

    def xǁDuuxChildLockSwitchǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(None, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_translation_key = "child_lock"
        self._attr_icon = "mdi:lock"

    def xǁDuuxChildLockSwitchǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, None, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_translation_key = "child_lock"
        self._attr_icon = "mdi:lock"

    def xǁDuuxChildLockSwitchǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, api, None)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_translation_key = "child_lock"
        self._attr_icon = "mdi:lock"

    def xǁDuuxChildLockSwitchǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(api, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_translation_key = "child_lock"
        self._attr_icon = "mdi:lock"

    def xǁDuuxChildLockSwitchǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_translation_key = "child_lock"
        self._attr_icon = "mdi:lock"

    def xǁDuuxChildLockSwitchǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, api, )
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_translation_key = "child_lock"
        self._attr_icon = "mdi:lock"

    def xǁDuuxChildLockSwitchǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = None
        self._attr_translation_key = "child_lock"
        self._attr_icon = "mdi:lock"

    def xǁDuuxChildLockSwitchǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_translation_key = None
        self._attr_icon = "mdi:lock"

    def xǁDuuxChildLockSwitchǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_translation_key = "XXchild_lockXX"
        self._attr_icon = "mdi:lock"

    def xǁDuuxChildLockSwitchǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_translation_key = "CHILD_LOCK"
        self._attr_icon = "mdi:lock"

    def xǁDuuxChildLockSwitchǁ__init____mutmut_11(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_translation_key = "child_lock"
        self._attr_icon = None

    def xǁDuuxChildLockSwitchǁ__init____mutmut_12(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_translation_key = "child_lock"
        self._attr_icon = "XXmdi:lockXX"

    def xǁDuuxChildLockSwitchǁ__init____mutmut_13(self, coordinator, api, device):
        """Initialize the child lock switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_child_lock"
        self._attr_translation_key = "child_lock"
        self._attr_icon = "MDI:LOCK"

    @property
    def is_on(self):
        """Return true if child lock is on."""
        return (self.coordinator.data or {}).get("lock") == 1

    @_mutmut_mutated(mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut)
    async def async_turn_on(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["lock"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_orig(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["lock"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_1(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            None, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["lock"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_2(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, None, True
        )
        newData = self.coordinator.data
        newData["lock"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_3(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["lock"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_4(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._device_mac, True
        )
        newData = self.coordinator.data
        newData["lock"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_5(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, True
        )
        newData = self.coordinator.data
        newData["lock"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_6(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, )
        newData = self.coordinator.data
        newData["lock"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_7(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["lock"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_8(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, True
        )
        newData = None
        newData["lock"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_9(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["lock"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_10(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["XXlockXX"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_11(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["LOCK"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_12(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["lock"] = 2
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_13(self, **kwargs):
        """Turn on child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["lock"] = 1
        self.coordinator.async_set_updated_data(None)

    @_mutmut_mutated(mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut)
    async def async_turn_off(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["lock"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_orig(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["lock"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_1(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            None, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["lock"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_2(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, None, False
        )
        newData = self.coordinator.data
        newData["lock"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_3(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["lock"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_4(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            self._device_mac, False
        )
        newData = self.coordinator.data
        newData["lock"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_5(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, False
        )
        newData = self.coordinator.data
        newData["lock"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_6(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, )
        newData = self.coordinator.data
        newData["lock"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_7(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["lock"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_8(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, False
        )
        newData = None
        newData["lock"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_9(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["lock"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_10(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["XXlockXX"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_11(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["LOCK"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_12(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["lock"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_13(self, **kwargs):
        """Turn off child lock."""
        await self.hass.async_add_executor_job(
            self._api.set_lock, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["lock"] = 0
        self.coordinator.async_set_updated_data(None)

mutants_xǁDuuxChildLockSwitchǁ__init____mutmut['_mutmut_orig'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁ__init____mutmut['xǁDuuxChildLockSwitchǁ__init____mutmut_1'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁ__init____mutmut['xǁDuuxChildLockSwitchǁ__init____mutmut_2'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁ__init____mutmut['xǁDuuxChildLockSwitchǁ__init____mutmut_3'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁ__init____mutmut['xǁDuuxChildLockSwitchǁ__init____mutmut_4'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁ__init____mutmut['xǁDuuxChildLockSwitchǁ__init____mutmut_5'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁ__init____mutmut['xǁDuuxChildLockSwitchǁ__init____mutmut_6'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁ__init____mutmut['xǁDuuxChildLockSwitchǁ__init____mutmut_7'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁ__init____mutmut['xǁDuuxChildLockSwitchǁ__init____mutmut_8'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁ__init____mutmut['xǁDuuxChildLockSwitchǁ__init____mutmut_9'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁ__init____mutmut['xǁDuuxChildLockSwitchǁ__init____mutmut_10'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁ__init____mutmut['xǁDuuxChildLockSwitchǁ__init____mutmut_11'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁ__init____mutmut['xǁDuuxChildLockSwitchǁ__init____mutmut_12'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁ__init____mutmut['xǁDuuxChildLockSwitchǁ__init____mutmut_13'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁ__init____mutmut_13 # type: ignore # mutmut generated

mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut['_mutmut_orig'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut['xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_1'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut['xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_2'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut['xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_3'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut['xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_4'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut['xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_5'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut['xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_6'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut['xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_7'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut['xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_8'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut['xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_9'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut['xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_10'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut['xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_11'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut['xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_12'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_on__mutmut['xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_13'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_on__mutmut_13 # type: ignore # mutmut generated

mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut['_mutmut_orig'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut['xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_1'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut['xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_2'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut['xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_3'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut['xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_4'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut['xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_5'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut['xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_6'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut['xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_7'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut['xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_8'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut['xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_9'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut['xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_10'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut['xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_11'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut['xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_12'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxChildLockSwitchǁasync_turn_off__mutmut['xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_13'] = DuuxChildLockSwitch.xǁDuuxChildLockSwitchǁasync_turn_off__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut: MutantDict = {}  # type: ignore


class DuuxNightModeSwitch(DuuxSwitch):
    """Representation of a Duux night mode switch."""

    @_mutmut_mutated(mutants_xǁDuuxNightModeSwitchǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_translation_key = "night_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxNightModeSwitchǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_translation_key = "night_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxNightModeSwitchǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(None, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_translation_key = "night_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxNightModeSwitchǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(coordinator, None, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_translation_key = "night_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxNightModeSwitchǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(coordinator, api, None)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_translation_key = "night_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxNightModeSwitchǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(api, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_translation_key = "night_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxNightModeSwitchǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(coordinator, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_translation_key = "night_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxNightModeSwitchǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(coordinator, api, )
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_translation_key = "night_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxNightModeSwitchǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = None
        self._attr_translation_key = "night_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxNightModeSwitchǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_translation_key = None
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxNightModeSwitchǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_translation_key = "XXnight_modeXX"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxNightModeSwitchǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_translation_key = "NIGHT_MODE"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxNightModeSwitchǁ__init____mutmut_11(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_translation_key = "night_mode"
        self._attr_icon = None

    def xǁDuuxNightModeSwitchǁ__init____mutmut_12(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_translation_key = "night_mode"
        self._attr_icon = "XXmdi:weather-nightXX"

    def xǁDuuxNightModeSwitchǁ__init____mutmut_13(self, coordinator, api, device):
        """Initialize the night mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_night_mode"
        self._attr_translation_key = "night_mode"
        self._attr_icon = "MDI:WEATHER-NIGHT"

    @property
    def is_on(self):
        """Return true if night mode is on."""
        return (self.coordinator.data or {}).get("night") == 1

    @_mutmut_mutated(mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut)
    async def async_turn_on(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["night"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_orig(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["night"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_1(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            None, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["night"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_2(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, None, True
        )
        newData = self.coordinator.data
        newData["night"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_3(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["night"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_4(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._device_mac, True
        )
        newData = self.coordinator.data
        newData["night"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_5(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, True
        )
        newData = self.coordinator.data
        newData["night"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_6(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, )
        newData = self.coordinator.data
        newData["night"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_7(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["night"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_8(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, True
        )
        newData = None
        newData["night"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_9(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["night"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_10(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["XXnightXX"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_11(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["NIGHT"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_12(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["night"] = 2
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_13(self, **kwargs):
        """Turn on night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["night"] = 1
        self.coordinator.async_set_updated_data(None)

    @_mutmut_mutated(mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut)
    async def async_turn_off(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["night"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_orig(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["night"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_1(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            None, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["night"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_2(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, None, False
        )
        newData = self.coordinator.data
        newData["night"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_3(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["night"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_4(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            self._device_mac, False
        )
        newData = self.coordinator.data
        newData["night"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_5(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, False
        )
        newData = self.coordinator.data
        newData["night"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_6(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, )
        newData = self.coordinator.data
        newData["night"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_7(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["night"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_8(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, False
        )
        newData = None
        newData["night"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_9(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["night"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_10(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["XXnightXX"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_11(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["NIGHT"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_12(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["night"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_13(self, **kwargs):
        """Turn off night mode."""
        await self.hass.async_add_executor_job(
            self._api.set_night_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["night"] = 0
        self.coordinator.async_set_updated_data(None)

mutants_xǁDuuxNightModeSwitchǁ__init____mutmut['_mutmut_orig'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁ__init____mutmut['xǁDuuxNightModeSwitchǁ__init____mutmut_1'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁ__init____mutmut['xǁDuuxNightModeSwitchǁ__init____mutmut_2'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁ__init____mutmut['xǁDuuxNightModeSwitchǁ__init____mutmut_3'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁ__init____mutmut['xǁDuuxNightModeSwitchǁ__init____mutmut_4'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁ__init____mutmut['xǁDuuxNightModeSwitchǁ__init____mutmut_5'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁ__init____mutmut['xǁDuuxNightModeSwitchǁ__init____mutmut_6'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁ__init____mutmut['xǁDuuxNightModeSwitchǁ__init____mutmut_7'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁ__init____mutmut['xǁDuuxNightModeSwitchǁ__init____mutmut_8'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁ__init____mutmut['xǁDuuxNightModeSwitchǁ__init____mutmut_9'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁ__init____mutmut['xǁDuuxNightModeSwitchǁ__init____mutmut_10'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁ__init____mutmut['xǁDuuxNightModeSwitchǁ__init____mutmut_11'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁ__init____mutmut['xǁDuuxNightModeSwitchǁ__init____mutmut_12'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁ__init____mutmut['xǁDuuxNightModeSwitchǁ__init____mutmut_13'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁ__init____mutmut_13 # type: ignore # mutmut generated

mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut['_mutmut_orig'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut['xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_1'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut['xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_2'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut['xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_3'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut['xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_4'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut['xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_5'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut['xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_6'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut['xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_7'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut['xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_8'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut['xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_9'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut['xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_10'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut['xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_11'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut['xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_12'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_on__mutmut['xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_13'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_on__mutmut_13 # type: ignore # mutmut generated

mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut['_mutmut_orig'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut['xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_1'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut['xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_2'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut['xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_3'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut['xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_4'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut['xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_5'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut['xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_6'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut['xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_7'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut['xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_8'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut['xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_9'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut['xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_10'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut['xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_11'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut['xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_12'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxNightModeSwitchǁasync_turn_off__mutmut['xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_13'] = DuuxNightModeSwitch.xǁDuuxNightModeSwitchǁasync_turn_off__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut: MutantDict = {}  # type: ignore


class DuuxSleepModeSwitch(DuuxSwitch):
    """Representation of a Duux sleep mode switch."""

    @_mutmut_mutated(mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_translation_key = "sleep_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxSleepModeSwitchǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_translation_key = "sleep_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxSleepModeSwitchǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(None, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_translation_key = "sleep_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxSleepModeSwitchǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(coordinator, None, device)
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_translation_key = "sleep_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxSleepModeSwitchǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(coordinator, api, None)
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_translation_key = "sleep_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxSleepModeSwitchǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(api, device)
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_translation_key = "sleep_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxSleepModeSwitchǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(coordinator, device)
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_translation_key = "sleep_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxSleepModeSwitchǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(coordinator, api, )
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_translation_key = "sleep_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxSleepModeSwitchǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = None
        self._attr_translation_key = "sleep_mode"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxSleepModeSwitchǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_translation_key = None
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxSleepModeSwitchǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_translation_key = "XXsleep_modeXX"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxSleepModeSwitchǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_translation_key = "SLEEP_MODE"
        self._attr_icon = "mdi:weather-night"

    def xǁDuuxSleepModeSwitchǁ__init____mutmut_11(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_translation_key = "sleep_mode"
        self._attr_icon = None

    def xǁDuuxSleepModeSwitchǁ__init____mutmut_12(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_translation_key = "sleep_mode"
        self._attr_icon = "XXmdi:weather-nightXX"

    def xǁDuuxSleepModeSwitchǁ__init____mutmut_13(self, coordinator, api, device):
        """Initialize the sleep mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_sleep_mode"
        self._attr_translation_key = "sleep_mode"
        self._attr_icon = "MDI:WEATHER-NIGHT"

    @property
    def is_on(self):
        """Return true if night mode is on."""
        return (self.coordinator.data or {}).get("sleep") == 1

    @_mutmut_mutated(mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut)
    async def async_turn_on(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["sleep"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_orig(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["sleep"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_1(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            None, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["sleep"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_2(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, None, True
        )
        newData = self.coordinator.data
        newData["sleep"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_3(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["sleep"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_4(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._device_mac, True
        )
        newData = self.coordinator.data
        newData["sleep"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_5(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, True
        )
        newData = self.coordinator.data
        newData["sleep"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_6(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, )
        newData = self.coordinator.data
        newData["sleep"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_7(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["sleep"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_8(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, True
        )
        newData = None
        newData["sleep"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_9(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["sleep"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_10(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["XXsleepXX"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_11(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["SLEEP"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_12(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["sleep"] = 2
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_13(self, **kwargs):
        """Turn on sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["sleep"] = 1
        self.coordinator.async_set_updated_data(None)

    @_mutmut_mutated(mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut)
    async def async_turn_off(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["sleep"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_orig(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["sleep"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_1(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            None, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["sleep"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_2(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, None, False
        )
        newData = self.coordinator.data
        newData["sleep"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_3(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["sleep"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_4(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            self._device_mac, False
        )
        newData = self.coordinator.data
        newData["sleep"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_5(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, False
        )
        newData = self.coordinator.data
        newData["sleep"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_6(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, )
        newData = self.coordinator.data
        newData["sleep"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_7(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["sleep"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_8(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, False
        )
        newData = None
        newData["sleep"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_9(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["sleep"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_10(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["XXsleepXX"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_11(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["SLEEP"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_12(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["sleep"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_13(self, **kwargs):
        """Turn off sleep mode."""
        await self.hass.async_add_executor_job(
            self._api.set_sleep_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["sleep"] = 0
        self.coordinator.async_set_updated_data(None)

mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut['_mutmut_orig'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut['xǁDuuxSleepModeSwitchǁ__init____mutmut_1'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut['xǁDuuxSleepModeSwitchǁ__init____mutmut_2'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut['xǁDuuxSleepModeSwitchǁ__init____mutmut_3'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut['xǁDuuxSleepModeSwitchǁ__init____mutmut_4'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut['xǁDuuxSleepModeSwitchǁ__init____mutmut_5'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut['xǁDuuxSleepModeSwitchǁ__init____mutmut_6'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut['xǁDuuxSleepModeSwitchǁ__init____mutmut_7'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut['xǁDuuxSleepModeSwitchǁ__init____mutmut_8'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut['xǁDuuxSleepModeSwitchǁ__init____mutmut_9'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut['xǁDuuxSleepModeSwitchǁ__init____mutmut_10'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut['xǁDuuxSleepModeSwitchǁ__init____mutmut_11'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut['xǁDuuxSleepModeSwitchǁ__init____mutmut_12'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁ__init____mutmut['xǁDuuxSleepModeSwitchǁ__init____mutmut_13'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁ__init____mutmut_13 # type: ignore # mutmut generated

mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut['_mutmut_orig'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_1'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_2'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_3'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_4'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_5'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_6'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_7'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_8'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_9'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_10'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_11'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_12'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_13'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_on__mutmut_13 # type: ignore # mutmut generated

mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut['_mutmut_orig'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_1'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_2'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_3'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_4'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_5'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_6'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_7'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_8'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_9'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_10'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_11'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_12'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut['xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_13'] = DuuxSleepModeSwitch.xǁDuuxSleepModeSwitchǁasync_turn_off__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut: MutantDict = {}  # type: ignore


class DuuxCleaningModeSwitch(DuuxSwitch):
    """Representation of a Duux self-cleaning mode switch."""

    @_mutmut_mutated(mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_translation_key = "cleaning_mode"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxCleaningModeSwitchǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_translation_key = "cleaning_mode"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxCleaningModeSwitchǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(None, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_translation_key = "cleaning_mode"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxCleaningModeSwitchǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(coordinator, None, device)
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_translation_key = "cleaning_mode"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxCleaningModeSwitchǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(coordinator, api, None)
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_translation_key = "cleaning_mode"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxCleaningModeSwitchǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(api, device)
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_translation_key = "cleaning_mode"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxCleaningModeSwitchǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(coordinator, device)
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_translation_key = "cleaning_mode"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxCleaningModeSwitchǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(coordinator, api, )
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_translation_key = "cleaning_mode"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxCleaningModeSwitchǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = None
        self._attr_translation_key = "cleaning_mode"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxCleaningModeSwitchǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_translation_key = None
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxCleaningModeSwitchǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_translation_key = "XXcleaning_modeXX"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxCleaningModeSwitchǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_translation_key = "CLEANING_MODE"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxCleaningModeSwitchǁ__init____mutmut_11(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_translation_key = "cleaning_mode"
        self._attr_icon = None

    def xǁDuuxCleaningModeSwitchǁ__init____mutmut_12(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_translation_key = "cleaning_mode"
        self._attr_icon = "XXmdi:air-filterXX"

    def xǁDuuxCleaningModeSwitchǁ__init____mutmut_13(self, coordinator, api, device):
        """Initialize the self-cleaning mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_cleaning_mode"
        self._attr_translation_key = "cleaning_mode"
        self._attr_icon = "MDI:AIR-FILTER"

    @property
    def is_on(self):
        """Return true if self-cleaning mode is on."""
        return (self.coordinator.data or {}).get("dry") == 1

    @_mutmut_mutated(mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut)
    async def async_turn_on(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["dry"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_orig(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["dry"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_1(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            None, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["dry"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_2(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, None, True
        )
        newData = self.coordinator.data
        newData["dry"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_3(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["dry"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_4(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._device_mac, True
        )
        newData = self.coordinator.data
        newData["dry"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_5(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, True
        )
        newData = self.coordinator.data
        newData["dry"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_6(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, )
        newData = self.coordinator.data
        newData["dry"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_7(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["dry"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_8(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, True
        )
        newData = None
        newData["dry"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_9(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["dry"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_10(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["XXdryXX"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_11(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["DRY"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_12(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["dry"] = 2
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_13(self, **kwargs):
        """Turn on cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["dry"] = 1
        self.coordinator.async_set_updated_data(None)

    @_mutmut_mutated(mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut)
    async def async_turn_off(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["dry"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_orig(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["dry"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_1(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            None, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["dry"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_2(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, None, False
        )
        newData = self.coordinator.data
        newData["dry"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_3(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["dry"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_4(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            self._device_mac, False
        )
        newData = self.coordinator.data
        newData["dry"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_5(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, False
        )
        newData = self.coordinator.data
        newData["dry"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_6(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, )
        newData = self.coordinator.data
        newData["dry"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_7(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["dry"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_8(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, False
        )
        newData = None
        newData["dry"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_9(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["dry"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_10(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["XXdryXX"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_11(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["DRY"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_12(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["dry"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_13(self, **kwargs):
        """Turn off cleaning mode."""
        await self.hass.async_add_executor_job(
            self._api.set_cleaning_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["dry"] = 0
        self.coordinator.async_set_updated_data(None)

mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut['_mutmut_orig'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut['xǁDuuxCleaningModeSwitchǁ__init____mutmut_1'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut['xǁDuuxCleaningModeSwitchǁ__init____mutmut_2'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut['xǁDuuxCleaningModeSwitchǁ__init____mutmut_3'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut['xǁDuuxCleaningModeSwitchǁ__init____mutmut_4'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut['xǁDuuxCleaningModeSwitchǁ__init____mutmut_5'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut['xǁDuuxCleaningModeSwitchǁ__init____mutmut_6'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut['xǁDuuxCleaningModeSwitchǁ__init____mutmut_7'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut['xǁDuuxCleaningModeSwitchǁ__init____mutmut_8'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut['xǁDuuxCleaningModeSwitchǁ__init____mutmut_9'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut['xǁDuuxCleaningModeSwitchǁ__init____mutmut_10'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut['xǁDuuxCleaningModeSwitchǁ__init____mutmut_11'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut['xǁDuuxCleaningModeSwitchǁ__init____mutmut_12'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁ__init____mutmut['xǁDuuxCleaningModeSwitchǁ__init____mutmut_13'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁ__init____mutmut_13 # type: ignore # mutmut generated

mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut['_mutmut_orig'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_1'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_2'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_3'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_4'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_5'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_6'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_7'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_8'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_9'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_10'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_11'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_12'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_13'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_on__mutmut_13 # type: ignore # mutmut generated

mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut['_mutmut_orig'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_1'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_2'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_3'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_4'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_5'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_6'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_7'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_8'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_9'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_10'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_11'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_12'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut['xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_13'] = DuuxCleaningModeSwitch.xǁDuuxCleaningModeSwitchǁasync_turn_off__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut: MutantDict = {}  # type: ignore


class DuuxLaundryModeSwitch(DuuxSwitch):
    """Representation of a Duux laundry mode switch."""

    @_mutmut_mutated(mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_translation_key = "laundry_mode"
        self._attr_icon = "mdi:tshirt-crew"

    def xǁDuuxLaundryModeSwitchǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_translation_key = "laundry_mode"
        self._attr_icon = "mdi:tshirt-crew"

    def xǁDuuxLaundryModeSwitchǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(None, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_translation_key = "laundry_mode"
        self._attr_icon = "mdi:tshirt-crew"

    def xǁDuuxLaundryModeSwitchǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(coordinator, None, device)
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_translation_key = "laundry_mode"
        self._attr_icon = "mdi:tshirt-crew"

    def xǁDuuxLaundryModeSwitchǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(coordinator, api, None)
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_translation_key = "laundry_mode"
        self._attr_icon = "mdi:tshirt-crew"

    def xǁDuuxLaundryModeSwitchǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(api, device)
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_translation_key = "laundry_mode"
        self._attr_icon = "mdi:tshirt-crew"

    def xǁDuuxLaundryModeSwitchǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(coordinator, device)
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_translation_key = "laundry_mode"
        self._attr_icon = "mdi:tshirt-crew"

    def xǁDuuxLaundryModeSwitchǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(coordinator, api, )
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_translation_key = "laundry_mode"
        self._attr_icon = "mdi:tshirt-crew"

    def xǁDuuxLaundryModeSwitchǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = None
        self._attr_translation_key = "laundry_mode"
        self._attr_icon = "mdi:tshirt-crew"

    def xǁDuuxLaundryModeSwitchǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_translation_key = None
        self._attr_icon = "mdi:tshirt-crew"

    def xǁDuuxLaundryModeSwitchǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_translation_key = "XXlaundry_modeXX"
        self._attr_icon = "mdi:tshirt-crew"

    def xǁDuuxLaundryModeSwitchǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_translation_key = "LAUNDRY_MODE"
        self._attr_icon = "mdi:tshirt-crew"

    def xǁDuuxLaundryModeSwitchǁ__init____mutmut_11(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_translation_key = "laundry_mode"
        self._attr_icon = None

    def xǁDuuxLaundryModeSwitchǁ__init____mutmut_12(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_translation_key = "laundry_mode"
        self._attr_icon = "XXmdi:tshirt-crewXX"

    def xǁDuuxLaundryModeSwitchǁ__init____mutmut_13(self, coordinator, api, device):
        """Initialize the laundry mode switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_laundry_mode"
        self._attr_translation_key = "laundry_mode"
        self._attr_icon = "MDI:TSHIRT-CREW"

    @property
    def is_on(self):
        """Return true if laundry mode is on."""
        return (self.coordinator.data or {}).get("laundr") == 1

    @_mutmut_mutated(mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut)
    async def async_turn_on(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["laundr"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_orig(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["laundr"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_1(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            None, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["laundr"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_2(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, None, True
        )
        newData = self.coordinator.data
        newData["laundr"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_3(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["laundr"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_4(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._device_mac, True
        )
        newData = self.coordinator.data
        newData["laundr"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_5(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, True
        )
        newData = self.coordinator.data
        newData["laundr"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_6(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, )
        newData = self.coordinator.data
        newData["laundr"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_7(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["laundr"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_8(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, True
        )
        newData = None
        newData["laundr"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_9(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["laundr"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_10(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["XXlaundrXX"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_11(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["LAUNDR"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_12(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["laundr"] = 2
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_13(self, **kwargs):
        """Turn on laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["laundr"] = 1
        self.coordinator.async_set_updated_data(None)

    @_mutmut_mutated(mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut)
    async def async_turn_off(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["laundr"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_orig(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["laundr"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_1(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            None, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["laundr"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_2(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, None, False
        )
        newData = self.coordinator.data
        newData["laundr"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_3(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["laundr"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_4(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            self._device_mac, False
        )
        newData = self.coordinator.data
        newData["laundr"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_5(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, False
        )
        newData = self.coordinator.data
        newData["laundr"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_6(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, )
        newData = self.coordinator.data
        newData["laundr"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_7(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["laundr"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_8(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, False
        )
        newData = None
        newData["laundr"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_9(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["laundr"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_10(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["XXlaundrXX"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_11(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["LAUNDR"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_12(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["laundr"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_13(self, **kwargs):
        """Turn off Laundry mode."""
        await self.hass.async_add_executor_job(
            self._api.set_laundry_mode, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["laundr"] = 0
        self.coordinator.async_set_updated_data(None)

mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut['_mutmut_orig'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut['xǁDuuxLaundryModeSwitchǁ__init____mutmut_1'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut['xǁDuuxLaundryModeSwitchǁ__init____mutmut_2'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut['xǁDuuxLaundryModeSwitchǁ__init____mutmut_3'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut['xǁDuuxLaundryModeSwitchǁ__init____mutmut_4'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut['xǁDuuxLaundryModeSwitchǁ__init____mutmut_5'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut['xǁDuuxLaundryModeSwitchǁ__init____mutmut_6'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut['xǁDuuxLaundryModeSwitchǁ__init____mutmut_7'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut['xǁDuuxLaundryModeSwitchǁ__init____mutmut_8'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut['xǁDuuxLaundryModeSwitchǁ__init____mutmut_9'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut['xǁDuuxLaundryModeSwitchǁ__init____mutmut_10'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut['xǁDuuxLaundryModeSwitchǁ__init____mutmut_11'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut['xǁDuuxLaundryModeSwitchǁ__init____mutmut_12'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁ__init____mutmut['xǁDuuxLaundryModeSwitchǁ__init____mutmut_13'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁ__init____mutmut_13 # type: ignore # mutmut generated

mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut['_mutmut_orig'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_1'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_2'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_3'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_4'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_5'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_6'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_7'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_8'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_9'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_10'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_11'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_12'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_13'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_on__mutmut_13 # type: ignore # mutmut generated

mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut['_mutmut_orig'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_1'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_2'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_3'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_4'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_5'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_6'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_7'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_8'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_9'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_10'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_11'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_12'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut['xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_13'] = DuuxLaundryModeSwitch.xǁDuuxLaundryModeSwitchǁasync_turn_off__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut: MutantDict = {}  # type: ignore


class DuuxIonizerSwitch(DuuxSwitch):
    """Representation of a Duux ionizer switch."""

    @_mutmut_mutated(mutants_xǁDuuxIonizerSwitchǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_ionizer"
        self._attr_translation_key = "ionizer"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxIonizerSwitchǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_ionizer"
        self._attr_translation_key = "ionizer"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxIonizerSwitchǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(None, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_ionizer"
        self._attr_translation_key = "ionizer"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxIonizerSwitchǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(coordinator, None, device)
        self._attr_unique_id = f"duux_{self._device_id}_ionizer"
        self._attr_translation_key = "ionizer"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxIonizerSwitchǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(coordinator, api, None)
        self._attr_unique_id = f"duux_{self._device_id}_ionizer"
        self._attr_translation_key = "ionizer"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxIonizerSwitchǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(api, device)
        self._attr_unique_id = f"duux_{self._device_id}_ionizer"
        self._attr_translation_key = "ionizer"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxIonizerSwitchǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(coordinator, device)
        self._attr_unique_id = f"duux_{self._device_id}_ionizer"
        self._attr_translation_key = "ionizer"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxIonizerSwitchǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(coordinator, api, )
        self._attr_unique_id = f"duux_{self._device_id}_ionizer"
        self._attr_translation_key = "ionizer"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxIonizerSwitchǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = None
        self._attr_translation_key = "ionizer"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxIonizerSwitchǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_ionizer"
        self._attr_translation_key = None
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxIonizerSwitchǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_ionizer"
        self._attr_translation_key = "XXionizerXX"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxIonizerSwitchǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_ionizer"
        self._attr_translation_key = "IONIZER"
        self._attr_icon = "mdi:air-filter"

    def xǁDuuxIonizerSwitchǁ__init____mutmut_11(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_ionizer"
        self._attr_translation_key = "ionizer"
        self._attr_icon = None

    def xǁDuuxIonizerSwitchǁ__init____mutmut_12(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_ionizer"
        self._attr_translation_key = "ionizer"
        self._attr_icon = "XXmdi:air-filterXX"

    def xǁDuuxIonizerSwitchǁ__init____mutmut_13(self, coordinator, api, device):
        """Initialize the ionizer switch."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_ionizer"
        self._attr_translation_key = "ionizer"
        self._attr_icon = "MDI:AIR-FILTER"

    @property
    def is_on(self):
        """Return true if ionizer is on."""
        return (self.coordinator.data or {}).get("ion") == 1

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        if not super().available:
            return False

        # Constraint for Bright 2: Ionizer unavailable if speed is 1 (manual mode)
        # Note: In Auto mode (speed 0), it should be available.
        data = self.coordinator.data or {}
        speed = data.get("speed")
        sensor_type_id = self._device.get("sensorTypeId")

        if sensor_type_id == DUUX_STID_BRIGHT_2 and speed == 1:
            return False

        return True

    @_mutmut_mutated(mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut)
    async def async_turn_on(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_orig(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_1(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get(None) == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_2(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data and {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_3(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("XXspeedXX") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_4(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("SPEED") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_5(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") != 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_6(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 2:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_7(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                None
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_8(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "XXIonizer cannot be turned on when fan speed is at lowest (1)XX"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_9(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_10(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "IONIZER CANNOT BE TURNED ON WHEN FAN SPEED IS AT LOWEST (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_11(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            None, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_12(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, None, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_13(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_14(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_15(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_16(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_17(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_18(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = None
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_19(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_20(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["XXionXX"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_21(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ION"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_22(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 2
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_23(self, **kwargs):
        """Turn on ionizer."""
        # Constraint: Ionizer cannot be turned on if speed is at lowest (1)
        if (self.coordinator.data or {}).get("speed") == 1:
            _LOGGER.warning(
                "Ionizer cannot be turned on when fan speed is at lowest (1)"
            )
            return

        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(None)

    @_mutmut_mutated(mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut)
    async def async_turn_off(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["ion"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_orig(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["ion"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_1(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            None, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["ion"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_2(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            self._api.set_ionizer, None, False
        )
        newData = self.coordinator.data
        newData["ion"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_3(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["ion"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_4(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            self._device_mac, False
        )
        newData = self.coordinator.data
        newData["ion"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_5(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            self._api.set_ionizer, False
        )
        newData = self.coordinator.data
        newData["ion"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_6(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, )
        newData = self.coordinator.data
        newData["ion"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_7(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, True
        )
        newData = self.coordinator.data
        newData["ion"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_8(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, False
        )
        newData = None
        newData["ion"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_9(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["ion"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_10(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["XXionXX"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_11(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["ION"] = 0
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_12(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["ion"] = 1
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_13(self, **kwargs):
        """Turn off ionizer."""
        await self.hass.async_add_executor_job(
            self._api.set_ionizer, self._device_mac, False
        )
        newData = self.coordinator.data
        newData["ion"] = 0
        self.coordinator.async_set_updated_data(None)

mutants_xǁDuuxIonizerSwitchǁ__init____mutmut['_mutmut_orig'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁ__init____mutmut['xǁDuuxIonizerSwitchǁ__init____mutmut_1'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁ__init____mutmut['xǁDuuxIonizerSwitchǁ__init____mutmut_2'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁ__init____mutmut['xǁDuuxIonizerSwitchǁ__init____mutmut_3'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁ__init____mutmut['xǁDuuxIonizerSwitchǁ__init____mutmut_4'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁ__init____mutmut['xǁDuuxIonizerSwitchǁ__init____mutmut_5'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁ__init____mutmut['xǁDuuxIonizerSwitchǁ__init____mutmut_6'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁ__init____mutmut['xǁDuuxIonizerSwitchǁ__init____mutmut_7'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁ__init____mutmut['xǁDuuxIonizerSwitchǁ__init____mutmut_8'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁ__init____mutmut['xǁDuuxIonizerSwitchǁ__init____mutmut_9'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁ__init____mutmut['xǁDuuxIonizerSwitchǁ__init____mutmut_10'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁ__init____mutmut['xǁDuuxIonizerSwitchǁ__init____mutmut_11'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁ__init____mutmut['xǁDuuxIonizerSwitchǁ__init____mutmut_12'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁ__init____mutmut['xǁDuuxIonizerSwitchǁ__init____mutmut_13'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁ__init____mutmut_13 # type: ignore # mutmut generated

mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['_mutmut_orig'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_1'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_2'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_3'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_4'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_5'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_6'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_7'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_8'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_9'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_10'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_11'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_12'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_13'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_14'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_15'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_16'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_17'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_18'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_19'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_20'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_21'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_22'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_on__mutmut['xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_23'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_on__mutmut_23 # type: ignore # mutmut generated

mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut['_mutmut_orig'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut['xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_1'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut['xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_2'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut['xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_3'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut['xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_4'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut['xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_5'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut['xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_6'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut['xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_7'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut['xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_8'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut['xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_9'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut['xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_10'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut['xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_11'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut['xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_12'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxIonizerSwitchǁasync_turn_off__mutmut['xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_13'] = DuuxIonizerSwitch.xǁDuuxIonizerSwitchǁasync_turn_off__mutmut_13 # type: ignore # mutmut generated
