"""Support for Duux selectors."""

import logging

from homeassistant.components.select import SelectEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from homeassistant.const import (
    EntityCategory,
    UnitOfTime,
)

from .const import (
    DOMAIN,
    DUUX_STID_BORA_2024,
    DUUX_STID_BEAM_MINI,
    DUUX_STID_BRIGHT_2,
    DUUX_STID_EDGEHEATER_V2,
    DUUX_STID_NEO,
    DUUX_STID_WHISPER_FLEX_ELIVATE,
)

_LOGGER = logging.getLogger(__name__)

SWING_OFF = "Off"

# Horizontal swing button cycles through 3 stripe icons on the device.
# Levels are symmetric about centre (e.g. level 2 = 60 deg total = 30 deg
# each side). Raw values are inferred to be sequential indices, matching
# the pattern every other trait in this integration uses (mode/night/lock
# are all small sequential ints) — NOT confirmed against a trait schema,
# since horosc has no trait definition in the diagnostics sample.
HORIZONTAL_SWING_OPTIONS: dict[str, int] = {
    SWING_OFF: 0,
    "30°": 1,
    "60°": 2,
    "90°": 3,
}

# Vertical swing button cycles through 2 stripe icons on the device.
# Arc is NOT symmetric about horizontal (level 1 = 10 deg below to 35 deg
# above; level 2 = 10 deg below to 90 deg above). Same caveat as above —
# raw values are inferred, not confirmed.
VERTICAL_SWING_OPTIONS: dict[str, int] = {
    SWING_OFF: 0,
    "45°": 1,
    "100°": 2,
}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_async_setup_entry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_async_setup_entry__mutmut)
async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_orig(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_1(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_2(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_3(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_4(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_5(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_6(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_7(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_8(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_9(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_10(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_11(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_12(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_13(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_14(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_15(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_16(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_17(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_18(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_19(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_20(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_21(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_22(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_23(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_24(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_25(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id != DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_26(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(None)
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_27(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(None, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_28(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, None, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_29(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, None))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_30(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_31(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_32(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, ))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_33(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(None)
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_34(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(None, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_35(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, None, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_36(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, None))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_37(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_38(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_39(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, ))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_40(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id != DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_41(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(None)
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_42(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(None, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_43(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, None, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_44(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, None))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_45(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_46(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_47(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, ))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_48(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(None)
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_49(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(None, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_50(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, None, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_51(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, None))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_52(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_53(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_54(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, ))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_55(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id != DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_56(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(None)
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_57(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(None, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_58(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, None, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_59(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, None))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_60(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_61(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_62(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, ))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_63(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id not in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_64(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(None)

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_65(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(None, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_66(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, None, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_67(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, None))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_68(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_69(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_70(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, ))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_71(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None or sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_72(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get(None) is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_73(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("XXhoroscXX") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_74(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("HOROSC") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_75(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_76(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_77(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(None)

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_78(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(None, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_79(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, None, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_80(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, None))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_81(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_82(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_83(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, ))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_84(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get(None) is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_85(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("XXveroscXX") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_86(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("VEROSC") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_87(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_88(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(None)

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_89(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(None, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_90(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, None, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_91(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, None))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_92(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_93(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_94(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, ))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_95(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get(None) is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_96(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("XXswingXX") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_97(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("SWING") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_98(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_99(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(None)

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_100(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(None, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_101(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, None, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_102(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, None))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_103(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_104(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_105(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, ))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_106(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get(None) is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_107(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("XXtiltXX") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_108(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("TILT") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_109(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_110(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(None)
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_111(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(None, api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_112(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, None, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_113(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, None))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_114(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(api, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_115(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, device))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_116(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, ))
    async_add_entities(entities)


async def x_async_setup_entry__mutmut_117(hass, config_entry, async_add_entities):
    """Set up Duux selector entities from a config entry."""
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

        # Bora has two fan speeds..
        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxFanSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Route the Neo to its selectors
        elif sensor_type_id == DUUX_STID_NEO:
            entities.append(DuuxNeoSpeedSelector(coordinator, api, device))
            entities.append(DuuxTimerSelector(coordinator, api, device))
        # Added Duux Bright 2 for timer selector
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxBright2TimerSelector(coordinator, api, device))
        elif sensor_type_id in [DUUX_STID_BEAM_MINI, DUUX_STID_EDGEHEATER_V2]:
            entities.append(DuuxTimerSelector(coordinator, api, device))

        if coordinator.data.get("horosc") is not None and sensor_type_id not in [
            DUUX_STID_WHISPER_FLEX_ELIVATE
        ]:
            entities.append(DuuxHorizontalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("verosc") is not None:
            entities.append(DuuxVerticalOscillationSelect(coordinator, api, device))

        if coordinator.data.get("swing") is not None:
            entities.append(DuuxHorizontalSwingSelect(coordinator, api, device))

        if coordinator.data.get("tilt") is not None:
            entities.append(DuuxVerticalTiltSelect(coordinator, api, device))
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
mutants_xǁDuuxSwingSelectǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut: MutantDict = {}  # type: ignore


class DuuxSwingSelect(CoordinatorEntity, SelectEntity):
    """Base class for a DUUX swing-level select entity.

    Subclasses only need to set `_options_map` and `_data_key`, override
    `_set_value` to call the matching duux_api method, and set a
    name/icon — everything else (device linkage, availability, refresh)
    lives here. To attach a swing select to another fan model,
    instantiate the relevant subclass with that device's
    (coordinator, api, device), the same way entities are added in
    fan.py.
    """

    _options_map: dict[str, int] = {}
    _data_key: str = ""

    def _set_value(self, device_mac: str, value: int):
        """Call the duux_api method for this axis. Override in subclasses."""
        raise NotImplementedError

    @_mutmut_mutated(mutants_xǁDuuxSwingSelectǁ__init____mutmut)
    def __init__(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(self._options_map.keys())

    def xǁDuuxSwingSelectǁ__init____mutmut_orig(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(self._options_map.keys())

    def xǁDuuxSwingSelectǁ__init____mutmut_1(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(None)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(self._options_map.keys())

    def xǁDuuxSwingSelectǁ__init____mutmut_2(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = None
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(self._options_map.keys())

    def xǁDuuxSwingSelectǁ__init____mutmut_3(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = None
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(self._options_map.keys())

    def xǁDuuxSwingSelectǁ__init____mutmut_4(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = None
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(self._options_map.keys())

    def xǁDuuxSwingSelectǁ__init____mutmut_5(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["XXidXX"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(self._options_map.keys())

    def xǁDuuxSwingSelectǁ__init____mutmut_6(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["ID"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(self._options_map.keys())

    def xǁDuuxSwingSelectǁ__init____mutmut_7(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = None  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(self._options_map.keys())

    def xǁDuuxSwingSelectǁ__init____mutmut_8(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["XXdeviceIdXX"]  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(self._options_map.keys())

    def xǁDuuxSwingSelectǁ__init____mutmut_9(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceid"]  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(self._options_map.keys())

    def xǁDuuxSwingSelectǁ__init____mutmut_10(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["DEVICEID"]  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(self._options_map.keys())

    def xǁDuuxSwingSelectǁ__init____mutmut_11(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_has_entity_name = None
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(self._options_map.keys())

    def xǁDuuxSwingSelectǁ__init____mutmut_12(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_has_entity_name = False
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(self._options_map.keys())

    def xǁDuuxSwingSelectǁ__init____mutmut_13(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = None
        self._attr_options = list(self._options_map.keys())

    def xǁDuuxSwingSelectǁ__init____mutmut_14(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = None

    def xǁDuuxSwingSelectǁ__init____mutmut_15(self, coordinator, api, device) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_has_entity_name = True
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_options = list(None)

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self.coordinator.last_update_success and (
            self.coordinator.data or {}
        ).get("online", True)

    @property
    def device_info(self):
        """Return device information, linking this select to its fan device."""
        return {
            "identifiers": {(DOMAIN, str(self._device_id))},
            "name": self._device.get("displayName") or self._device.get("name"),
            "manufacturer": self._device.get("manufacturer", "Duux"),
            "model": self._device.get("sensorType", {}).get("name", "Unknown"),
        }

    @property
    def current_option(self) -> str | None:
        """Return the currently selected swing level."""
        raw_value = (self.coordinator.data or {}).get(self._data_key)
        if raw_value is None:
            return None

        for label, value in self._options_map.items():
            if value == raw_value:
                return label

        _LOGGER.debug(
            "%s: raw value %s for '%s' doesn't match any known option",
            getattr(self, "_attr_name", None),
            raw_value,
            self._data_key,
        )
        return None

    @_mutmut_mutated(mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut)
    async def async_select_option(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_orig(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_1(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_2(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                None,
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_3(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                None,
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_4(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                None,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_5(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_6(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_7(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_8(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "XX%s: unknown swing option '%s'XX",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_9(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%S: UNKNOWN SWING OPTION '%S'",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_10(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(None, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_11(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, None, None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_12(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr("_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_13(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_14(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", ),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_15(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "XX_attr_nameXX", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_16(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_ATTR_NAME", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_17(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = None

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_18(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(None, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_19(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, None, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_20(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, None)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_21(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_22(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_23(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, )
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_24(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = None
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_25(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxSwingSelectǁasync_select_option__mutmut_26(self, option: str) -> None:
        """Set the swing level, or turn swing off if 'Off' is selected."""
        if option not in self._options_map:
            _LOGGER.warning(
                "%s: unknown swing option '%s'",
                getattr(self, "_attr_name", None),
                option,
            )
            return

        value = self._options_map[option]

        await self.hass.async_add_executor_job(self._set_value, self._device_mac, value)
        newData = self.coordinator.data
        newData[self._data_key] = value
        self.coordinator.async_set_updated_data(None)

mutants_xǁDuuxSwingSelectǁ__init____mutmut['_mutmut_orig'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁ__init____mutmut['xǁDuuxSwingSelectǁ__init____mutmut_1'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁ__init____mutmut['xǁDuuxSwingSelectǁ__init____mutmut_2'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁ__init____mutmut['xǁDuuxSwingSelectǁ__init____mutmut_3'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁ__init____mutmut['xǁDuuxSwingSelectǁ__init____mutmut_4'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁ__init____mutmut['xǁDuuxSwingSelectǁ__init____mutmut_5'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁ__init____mutmut['xǁDuuxSwingSelectǁ__init____mutmut_6'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁ__init____mutmut['xǁDuuxSwingSelectǁ__init____mutmut_7'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁ__init____mutmut['xǁDuuxSwingSelectǁ__init____mutmut_8'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁ__init____mutmut['xǁDuuxSwingSelectǁ__init____mutmut_9'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁ__init____mutmut['xǁDuuxSwingSelectǁ__init____mutmut_10'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁ__init____mutmut['xǁDuuxSwingSelectǁ__init____mutmut_11'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁ__init____mutmut['xǁDuuxSwingSelectǁ__init____mutmut_12'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁ__init____mutmut['xǁDuuxSwingSelectǁ__init____mutmut_13'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁ__init____mutmut['xǁDuuxSwingSelectǁ__init____mutmut_14'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁ__init____mutmut['xǁDuuxSwingSelectǁ__init____mutmut_15'] = DuuxSwingSelect.xǁDuuxSwingSelectǁ__init____mutmut_15 # type: ignore # mutmut generated

mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['_mutmut_orig'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_1'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_2'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_3'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_4'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_5'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_6'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_7'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_8'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_9'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_10'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_11'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_12'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_13'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_14'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_15'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_16'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_17'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_18'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_19'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_20'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_21'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_22'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_23'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_24'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_25'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuuxSwingSelectǁasync_select_option__mutmut['xǁDuuxSwingSelectǁasync_select_option__mutmut_26'] = DuuxSwingSelect.xǁDuuxSwingSelectǁasync_select_option__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxHorizontalOscillationSelect(DuuxSwingSelect):
    """Select entity controlling horizontal oscillation level."""

    _options_map = HORIZONTAL_SWING_OPTIONS
    _data_key = "horosc"

    @_mutmut_mutated(mutants_xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut)
    def _set_value(self, device_mac: str, value: int):
        return self._api.set_horosc(device_mac, value)

    def xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut_orig(self, device_mac: str, value: int):
        return self._api.set_horosc(device_mac, value)

    def xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut_1(self, device_mac: str, value: int):
        return self._api.set_horosc(None, value)

    def xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut_2(self, device_mac: str, value: int):
        return self._api.set_horosc(device_mac, None)

    def xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut_3(self, device_mac: str, value: int):
        return self._api.set_horosc(value)

    def xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut_4(self, device_mac: str, value: int):
        return self._api.set_horosc(device_mac, )

    @_mutmut_mutated(mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut)
    def __init__(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_orig(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_1(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(None, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_2(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, None, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_3(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, None)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_4(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_5(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_6(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, )
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_7(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = None
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_8(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = None
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_9(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "XXhorizontal_swingXX"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_10(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "HORIZONTAL_SWING"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_11(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = None

    def xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_12(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "XXmdi:arrow-left-rightXX"

    def xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_13(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "MDI:ARROW-LEFT-RIGHT"

mutants_xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut['_mutmut_orig'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut['xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut_1'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut['xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut_2'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut['xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut_3'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut['xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut_4'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ_set_value__mutmut_4 # type: ignore # mutmut generated

mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut['_mutmut_orig'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut['xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_1'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut['xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_2'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut['xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_3'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut['xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_4'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut['xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_5'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut['xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_6'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut['xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_7'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut['xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_8'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut['xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_9'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut['xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_10'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut['xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_11'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut['xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_12'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalOscillationSelectǁ__init____mutmut['xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_13'] = DuuxHorizontalOscillationSelect.xǁDuuxHorizontalOscillationSelectǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxVerticalOscillationSelect(DuuxSwingSelect):
    """Select entity controlling vertical swing level."""

    _options_map = VERTICAL_SWING_OPTIONS
    _data_key = "verosc"

    @_mutmut_mutated(mutants_xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut)
    def _set_value(self, device_mac: str, value: int):
        return self._api.set_verosc(device_mac, value)

    def xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut_orig(self, device_mac: str, value: int):
        return self._api.set_verosc(device_mac, value)

    def xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut_1(self, device_mac: str, value: int):
        return self._api.set_verosc(None, value)

    def xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut_2(self, device_mac: str, value: int):
        return self._api.set_verosc(device_mac, None)

    def xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut_3(self, device_mac: str, value: int):
        return self._api.set_verosc(value)

    def xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut_4(self, device_mac: str, value: int):
        return self._api.set_verosc(device_mac, )

    @_mutmut_mutated(mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut)
    def __init__(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalOscillationSelectǁ__init____mutmut_orig(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalOscillationSelectǁ__init____mutmut_1(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(None, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalOscillationSelectǁ__init____mutmut_2(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(coordinator, None, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalOscillationSelectǁ__init____mutmut_3(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(coordinator, api, None)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalOscillationSelectǁ__init____mutmut_4(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalOscillationSelectǁ__init____mutmut_5(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(coordinator, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalOscillationSelectǁ__init____mutmut_6(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(coordinator, api, )
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalOscillationSelectǁ__init____mutmut_7(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = None
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalOscillationSelectǁ__init____mutmut_8(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = None
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalOscillationSelectǁ__init____mutmut_9(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "XXvertical_swingXX"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalOscillationSelectǁ__init____mutmut_10(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "VERTICAL_SWING"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalOscillationSelectǁ__init____mutmut_11(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = None

    def xǁDuuxVerticalOscillationSelectǁ__init____mutmut_12(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "XXmdi:arrow-up-downXX"

    def xǁDuuxVerticalOscillationSelectǁ__init____mutmut_13(self, coordinator, api, device) -> None:
        """Initialize the vertical swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "MDI:ARROW-UP-DOWN"

mutants_xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut['_mutmut_orig'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut['xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut_1'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut['xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut_2'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut['xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut_3'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut['xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut_4'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ_set_value__mutmut_4 # type: ignore # mutmut generated

mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut['_mutmut_orig'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut['xǁDuuxVerticalOscillationSelectǁ__init____mutmut_1'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut['xǁDuuxVerticalOscillationSelectǁ__init____mutmut_2'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut['xǁDuuxVerticalOscillationSelectǁ__init____mutmut_3'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut['xǁDuuxVerticalOscillationSelectǁ__init____mutmut_4'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut['xǁDuuxVerticalOscillationSelectǁ__init____mutmut_5'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut['xǁDuuxVerticalOscillationSelectǁ__init____mutmut_6'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut['xǁDuuxVerticalOscillationSelectǁ__init____mutmut_7'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut['xǁDuuxVerticalOscillationSelectǁ__init____mutmut_8'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut['xǁDuuxVerticalOscillationSelectǁ__init____mutmut_9'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut['xǁDuuxVerticalOscillationSelectǁ__init____mutmut_10'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut['xǁDuuxVerticalOscillationSelectǁ__init____mutmut_11'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut['xǁDuuxVerticalOscillationSelectǁ__init____mutmut_12'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalOscillationSelectǁ__init____mutmut['xǁDuuxVerticalOscillationSelectǁ__init____mutmut_13'] = DuuxVerticalOscillationSelect.xǁDuuxVerticalOscillationSelectǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxHorizontalSwingSelect(DuuxSwingSelect):
    """Select entity controlling horizontal swing level."""

    _options_map = HORIZONTAL_SWING_OPTIONS
    _data_key = "swing"

    @_mutmut_mutated(mutants_xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut)
    def _set_value(self, device_mac: str, value: int):
        return self._api.set_swing(device_mac, value)

    def xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut_orig(self, device_mac: str, value: int):
        return self._api.set_swing(device_mac, value)

    def xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut_1(self, device_mac: str, value: int):
        return self._api.set_swing(None, value)

    def xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut_2(self, device_mac: str, value: int):
        return self._api.set_swing(device_mac, None)

    def xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut_3(self, device_mac: str, value: int):
        return self._api.set_swing(value)

    def xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut_4(self, device_mac: str, value: int):
        return self._api.set_swing(device_mac, )

    @_mutmut_mutated(mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut)
    def __init__(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalSwingSelectǁ__init____mutmut_orig(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalSwingSelectǁ__init____mutmut_1(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(None, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalSwingSelectǁ__init____mutmut_2(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, None, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalSwingSelectǁ__init____mutmut_3(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, None)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalSwingSelectǁ__init____mutmut_4(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalSwingSelectǁ__init____mutmut_5(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalSwingSelectǁ__init____mutmut_6(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, )
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalSwingSelectǁ__init____mutmut_7(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = None
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalSwingSelectǁ__init____mutmut_8(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = None
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalSwingSelectǁ__init____mutmut_9(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "XXhorizontal_swingXX"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalSwingSelectǁ__init____mutmut_10(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "HORIZONTAL_SWING"
        self._attr_icon = "mdi:arrow-left-right"

    def xǁDuuxHorizontalSwingSelectǁ__init____mutmut_11(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = None

    def xǁDuuxHorizontalSwingSelectǁ__init____mutmut_12(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "XXmdi:arrow-left-rightXX"

    def xǁDuuxHorizontalSwingSelectǁ__init____mutmut_13(self, coordinator, api, device) -> None:
        """Initialize the horizontal swing select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_horizontal_swing"
        self._attr_translation_key = "horizontal_swing"
        self._attr_icon = "MDI:ARROW-LEFT-RIGHT"

mutants_xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut['_mutmut_orig'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut['xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut_1'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut['xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut_2'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut['xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut_3'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut['xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut_4'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ_set_value__mutmut_4 # type: ignore # mutmut generated

mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut['_mutmut_orig'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut['xǁDuuxHorizontalSwingSelectǁ__init____mutmut_1'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut['xǁDuuxHorizontalSwingSelectǁ__init____mutmut_2'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut['xǁDuuxHorizontalSwingSelectǁ__init____mutmut_3'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut['xǁDuuxHorizontalSwingSelectǁ__init____mutmut_4'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut['xǁDuuxHorizontalSwingSelectǁ__init____mutmut_5'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut['xǁDuuxHorizontalSwingSelectǁ__init____mutmut_6'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut['xǁDuuxHorizontalSwingSelectǁ__init____mutmut_7'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut['xǁDuuxHorizontalSwingSelectǁ__init____mutmut_8'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut['xǁDuuxHorizontalSwingSelectǁ__init____mutmut_9'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut['xǁDuuxHorizontalSwingSelectǁ__init____mutmut_10'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut['xǁDuuxHorizontalSwingSelectǁ__init____mutmut_11'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut['xǁDuuxHorizontalSwingSelectǁ__init____mutmut_12'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxHorizontalSwingSelectǁ__init____mutmut['xǁDuuxHorizontalSwingSelectǁ__init____mutmut_13'] = DuuxHorizontalSwingSelect.xǁDuuxHorizontalSwingSelectǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ_set_value__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxVerticalTiltSelect(DuuxSwingSelect):
    """Select entity controlling vertical tilt level."""

    _options_map = VERTICAL_SWING_OPTIONS
    _data_key = "tilt"

    @_mutmut_mutated(mutants_xǁDuuxVerticalTiltSelectǁ_set_value__mutmut)
    def _set_value(self, device_mac: str, value: int):
        return self._api.set_tilt(device_mac, value)

    def xǁDuuxVerticalTiltSelectǁ_set_value__mutmut_orig(self, device_mac: str, value: int):
        return self._api.set_tilt(device_mac, value)

    def xǁDuuxVerticalTiltSelectǁ_set_value__mutmut_1(self, device_mac: str, value: int):
        return self._api.set_tilt(None, value)

    def xǁDuuxVerticalTiltSelectǁ_set_value__mutmut_2(self, device_mac: str, value: int):
        return self._api.set_tilt(device_mac, None)

    def xǁDuuxVerticalTiltSelectǁ_set_value__mutmut_3(self, device_mac: str, value: int):
        return self._api.set_tilt(value)

    def xǁDuuxVerticalTiltSelectǁ_set_value__mutmut_4(self, device_mac: str, value: int):
        return self._api.set_tilt(device_mac, )

    @_mutmut_mutated(mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut)
    def __init__(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalTiltSelectǁ__init____mutmut_orig(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalTiltSelectǁ__init____mutmut_1(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(None, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalTiltSelectǁ__init____mutmut_2(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(coordinator, None, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalTiltSelectǁ__init____mutmut_3(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(coordinator, api, None)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalTiltSelectǁ__init____mutmut_4(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalTiltSelectǁ__init____mutmut_5(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(coordinator, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalTiltSelectǁ__init____mutmut_6(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(coordinator, api, )
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalTiltSelectǁ__init____mutmut_7(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = None
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalTiltSelectǁ__init____mutmut_8(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = None
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalTiltSelectǁ__init____mutmut_9(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "XXvertical_swingXX"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalTiltSelectǁ__init____mutmut_10(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "VERTICAL_SWING"
        self._attr_icon = "mdi:arrow-up-down"

    def xǁDuuxVerticalTiltSelectǁ__init____mutmut_11(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = None

    def xǁDuuxVerticalTiltSelectǁ__init____mutmut_12(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "XXmdi:arrow-up-downXX"

    def xǁDuuxVerticalTiltSelectǁ__init____mutmut_13(self, coordinator, api, device) -> None:
        """Initialize the vertical tilt select."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_vertical_swing"
        self._attr_translation_key = "vertical_swing"
        self._attr_icon = "MDI:ARROW-UP-DOWN"

mutants_xǁDuuxVerticalTiltSelectǁ_set_value__mutmut['_mutmut_orig'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ_set_value__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ_set_value__mutmut['xǁDuuxVerticalTiltSelectǁ_set_value__mutmut_1'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ_set_value__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ_set_value__mutmut['xǁDuuxVerticalTiltSelectǁ_set_value__mutmut_2'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ_set_value__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ_set_value__mutmut['xǁDuuxVerticalTiltSelectǁ_set_value__mutmut_3'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ_set_value__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ_set_value__mutmut['xǁDuuxVerticalTiltSelectǁ_set_value__mutmut_4'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ_set_value__mutmut_4 # type: ignore # mutmut generated

mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut['_mutmut_orig'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut['xǁDuuxVerticalTiltSelectǁ__init____mutmut_1'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut['xǁDuuxVerticalTiltSelectǁ__init____mutmut_2'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut['xǁDuuxVerticalTiltSelectǁ__init____mutmut_3'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut['xǁDuuxVerticalTiltSelectǁ__init____mutmut_4'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut['xǁDuuxVerticalTiltSelectǁ__init____mutmut_5'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut['xǁDuuxVerticalTiltSelectǁ__init____mutmut_6'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut['xǁDuuxVerticalTiltSelectǁ__init____mutmut_7'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut['xǁDuuxVerticalTiltSelectǁ__init____mutmut_8'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut['xǁDuuxVerticalTiltSelectǁ__init____mutmut_9'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut['xǁDuuxVerticalTiltSelectǁ__init____mutmut_10'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut['xǁDuuxVerticalTiltSelectǁ__init____mutmut_11'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut['xǁDuuxVerticalTiltSelectǁ__init____mutmut_12'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxVerticalTiltSelectǁ__init____mutmut['xǁDuuxVerticalTiltSelectǁ__init____mutmut_13'] = DuuxVerticalTiltSelect.xǁDuuxVerticalTiltSelectǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxSelector(CoordinatorEntity, SelectEntity):
    """Base class for Duux selectors."""

    @_mutmut_mutated(mutants_xǁDuuxSelectorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(None)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = None
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = None
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = None
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["XXidXX"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["ID"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = None  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["XXdeviceIdXX"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceid"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["DEVICEID"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_11(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = None
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_12(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = None
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_13(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") and device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_14(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get(None) or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_15(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("XXdisplayNameXX") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_16(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayname") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_17(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("DISPLAYNAME") or device.get("name")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_18(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get(None)
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_19(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("XXnameXX")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_20(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("NAME")
        self._attr_has_entity_name = True

    def xǁDuuxSelectorǁ__init____mutmut_21(self, coordinator, api, device):
        """Initialize the selector."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = None

    def xǁDuuxSelectorǁ__init____mutmut_22(self, coordinator, api, device):
        """Initialize the selector."""
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

mutants_xǁDuuxSelectorǁ__init____mutmut['_mutmut_orig'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_1'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_2'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_3'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_4'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_5'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_6'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_7'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_8'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_9'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_10'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_11'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_12'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_13'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_14'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_15'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_16'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_17'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_18'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_19'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_20'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_21'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxSelectorǁ__init____mutmut['xǁDuuxSelectorǁ__init____mutmut_22'] = DuuxSelector.xǁDuuxSelectorǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut: MutantDict = {}  # type: ignore


class DuuxFanSpeedSelector(DuuxSelector):
    """Representation of a Duux fan speed selector."""

    FAN_HIGH = "high"
    FAN_LOW = "low"

    @_mutmut_mutated(mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_translation_key = "fan_speed"
        self._attr_icon = "mdi:fan"

    def xǁDuuxFanSpeedSelectorǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_translation_key = "fan_speed"
        self._attr_icon = "mdi:fan"

    def xǁDuuxFanSpeedSelectorǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(None, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_translation_key = "fan_speed"
        self._attr_icon = "mdi:fan"

    def xǁDuuxFanSpeedSelectorǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(coordinator, None, device)
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_translation_key = "fan_speed"
        self._attr_icon = "mdi:fan"

    def xǁDuuxFanSpeedSelectorǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(coordinator, api, None)
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_translation_key = "fan_speed"
        self._attr_icon = "mdi:fan"

    def xǁDuuxFanSpeedSelectorǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(api, device)
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_translation_key = "fan_speed"
        self._attr_icon = "mdi:fan"

    def xǁDuuxFanSpeedSelectorǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(coordinator, device)
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_translation_key = "fan_speed"
        self._attr_icon = "mdi:fan"

    def xǁDuuxFanSpeedSelectorǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(coordinator, api, )
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_translation_key = "fan_speed"
        self._attr_icon = "mdi:fan"

    def xǁDuuxFanSpeedSelectorǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = None
        self._attr_translation_key = "fan_speed"
        self._attr_icon = "mdi:fan"

    def xǁDuuxFanSpeedSelectorǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_translation_key = None
        self._attr_icon = "mdi:fan"

    def xǁDuuxFanSpeedSelectorǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_translation_key = "XXfan_speedXX"
        self._attr_icon = "mdi:fan"

    def xǁDuuxFanSpeedSelectorǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_translation_key = "FAN_SPEED"
        self._attr_icon = "mdi:fan"

    def xǁDuuxFanSpeedSelectorǁ__init____mutmut_11(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_translation_key = "fan_speed"
        self._attr_icon = None

    def xǁDuuxFanSpeedSelectorǁ__init____mutmut_12(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_translation_key = "fan_speed"
        self._attr_icon = "XXmdi:fanXX"

    def xǁDuuxFanSpeedSelectorǁ__init____mutmut_13(self, coordinator, api, device):
        """Initialize the fan speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_fan_speed"
        self._attr_translation_key = "fan_speed"
        self._attr_icon = "MDI:FAN"

    @property
    def options(self):
        """Return available fan modes."""
        return [self.FAN_LOW, self.FAN_HIGH]

    @property
    def current_option(self):
        """Return current fan mode."""
        mode = (self.coordinator.data or {}).get("fan")
        mode_map = {
            1: self.FAN_LOW,
            0: self.FAN_HIGH,
        }
        return mode_map.get(int(mode) if mode is not None else 1, self.FAN_LOW)

    @_mutmut_mutated(mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut)
    async def async_select_option(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_orig(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_1(self, option):
        """Set fan speed mode."""
        mode_map = None

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_2(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "XX0XX",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_3(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "XX1XX",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_4(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = None

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_5(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(None, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_6(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, None)

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_7(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get("1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_8(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, )

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_9(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "XX1XX")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_10(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            None, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_11(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, None, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_12(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_13(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_14(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_15(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_16(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = None
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_17(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_18(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["XXfanXX"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_19(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["FAN"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_20(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(None)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_21(self, option):
        """Set fan speed mode."""
        mode_map = {
            self.FAN_HIGH: "0",
            self.FAN_LOW: "1",
        }

        mode = mode_map.get(option, "1")

        await self.hass.async_add_executor_job(
            self._api.set_fan, self._device_mac, mode
        )
        newData = self.coordinator.data
        newData["fan"] = int(mode)
        self.coordinator.async_set_updated_data(None)

mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut['_mutmut_orig'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut['xǁDuuxFanSpeedSelectorǁ__init____mutmut_1'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut['xǁDuuxFanSpeedSelectorǁ__init____mutmut_2'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut['xǁDuuxFanSpeedSelectorǁ__init____mutmut_3'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut['xǁDuuxFanSpeedSelectorǁ__init____mutmut_4'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut['xǁDuuxFanSpeedSelectorǁ__init____mutmut_5'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut['xǁDuuxFanSpeedSelectorǁ__init____mutmut_6'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut['xǁDuuxFanSpeedSelectorǁ__init____mutmut_7'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut['xǁDuuxFanSpeedSelectorǁ__init____mutmut_8'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut['xǁDuuxFanSpeedSelectorǁ__init____mutmut_9'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut['xǁDuuxFanSpeedSelectorǁ__init____mutmut_10'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut['xǁDuuxFanSpeedSelectorǁ__init____mutmut_11'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut['xǁDuuxFanSpeedSelectorǁ__init____mutmut_12'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁ__init____mutmut['xǁDuuxFanSpeedSelectorǁ__init____mutmut_13'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁ__init____mutmut_13 # type: ignore # mutmut generated

mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['_mutmut_orig'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_1'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_2'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_3'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_4'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_5'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_6'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_7'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_8'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_9'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_10'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_11'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_12'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_13'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_14'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_15'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_16'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_17'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_18'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_19'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_20'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut['xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_21'] = DuuxFanSpeedSelector.xǁDuuxFanSpeedSelectorǁasync_select_option__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut: MutantDict = {}  # type: ignore


class DuuxTimerSelector(DuuxSelector):
    """Representation of a Duux timer selector."""

    @_mutmut_mutated(mutants_xǁDuuxTimerSelectorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(None, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, None, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, None)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, )
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = None
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = None
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "XXtimerXX"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "TIMER"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_11(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = None
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_12(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "XXmdi:timerXX"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_13(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "MDI:TIMER"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_14(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = None
        self._attr_options = list(map(str, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_15(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = None

    def xǁDuuxTimerSelectorǁ__init____mutmut_16(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(None)

    def xǁDuuxTimerSelectorǁ__init____mutmut_17(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(None, range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_18(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, None))

    def xǁDuuxTimerSelectorǁ__init____mutmut_19(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(range(0, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_20(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, ))

    def xǁDuuxTimerSelectorǁ__init____mutmut_21(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(None, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_22(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, None)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_23(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_24(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, )))

    def xǁDuuxTimerSelectorǁ__init____mutmut_25(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(1, 24 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_26(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 - 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_27(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 25 + 1)))

    def xǁDuuxTimerSelectorǁ__init____mutmut_28(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_timer"
        self._attr_translation_key = "timer"
        self._attr_icon = "mdi:timer"
        self._attr_unit_of_measurement = UnitOfTime.HOURS
        self._attr_options = list(map(str, range(0, 24 + 2)))

    @property
    def current_option(self):
        """Return current timer."""
        timer = (self.coordinator.data or {}).get("timer")
        return str(timer) if timer is not None else None

    @_mutmut_mutated(mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut)
    async def async_select_option(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_orig(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_1(self, option):
        """Set timer amount."""
        try:
            amount = None
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_2(self, option):
        """Set timer amount."""
        try:
            amount = max(None, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_3(self, option):
        """Set timer amount."""
        try:
            amount = max(0, None)
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_4(self, option):
        """Set timer amount."""
        try:
            amount = max(min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_5(self, option):
        """Set timer amount."""
        try:
            amount = max(0, )
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_6(self, option):
        """Set timer amount."""
        try:
            amount = max(1, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_7(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(None, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_8(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, None))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_9(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_10(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, ))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_11(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(25, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_12(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(None)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_13(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = None

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_14(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 1

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_15(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            None, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_16(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, None, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_17(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, None
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_18(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_19(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_20(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_21(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(None)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_22(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = None
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_23(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_24(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["XXtimerXX"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_25(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["TIMER"] = amount
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxTimerSelectorǁasync_select_option__mutmut_26(self, option):
        """Set timer amount."""
        try:
            amount = max(0, min(24, int(option)))
        except (ValueError, TypeError):
            amount = 0

        await self.hass.async_add_executor_job(
            self._api.set_timer, self._device_mac, str(amount)
        )
        newData = self.coordinator.data
        newData["timer"] = amount
        self.coordinator.async_set_updated_data(None)

mutants_xǁDuuxTimerSelectorǁ__init____mutmut['_mutmut_orig'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_1'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_2'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_3'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_4'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_5'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_6'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_7'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_8'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_9'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_10'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_11'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_12'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_13'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_14'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_15'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_16'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_17'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_18'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_19'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_20'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_21'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_22'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_23'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_24'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_25'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_26'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_27'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_27 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁ__init____mutmut['xǁDuuxTimerSelectorǁ__init____mutmut_28'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁ__init____mutmut_28 # type: ignore # mutmut generated

mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['_mutmut_orig'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_1'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_2'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_3'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_4'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_5'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_6'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_7'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_8'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_9'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_10'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_11'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_12'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_13'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_14'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_15'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_16'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_17'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_18'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_19'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_20'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_21'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_22'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_23'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_24'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_25'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuuxTimerSelectorǁasync_select_option__mutmut['xǁDuuxTimerSelectorǁasync_select_option__mutmut_26'] = DuuxTimerSelector.xǁDuuxTimerSelectorǁasync_select_option__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimerSelectorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxBright2TimerSelector(DuuxTimerSelector):
    """Representation of a Duux Bright 2 timer selector."""

    @_mutmut_mutated(mutants_xǁDuuxBright2TimerSelectorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        # Bright 2 supports specific timer presets only (hours): 0=off, 1, 2, 4, 8
        self._attr_options = ["0", "1", "2", "4", "8"]

    def xǁDuuxBright2TimerSelectorǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        # Bright 2 supports specific timer presets only (hours): 0=off, 1, 2, 4, 8
        self._attr_options = ["0", "1", "2", "4", "8"]

    def xǁDuuxBright2TimerSelectorǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(None, api, device)
        # Bright 2 supports specific timer presets only (hours): 0=off, 1, 2, 4, 8
        self._attr_options = ["0", "1", "2", "4", "8"]

    def xǁDuuxBright2TimerSelectorǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, None, device)
        # Bright 2 supports specific timer presets only (hours): 0=off, 1, 2, 4, 8
        self._attr_options = ["0", "1", "2", "4", "8"]

    def xǁDuuxBright2TimerSelectorǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, None)
        # Bright 2 supports specific timer presets only (hours): 0=off, 1, 2, 4, 8
        self._attr_options = ["0", "1", "2", "4", "8"]

    def xǁDuuxBright2TimerSelectorǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(api, device)
        # Bright 2 supports specific timer presets only (hours): 0=off, 1, 2, 4, 8
        self._attr_options = ["0", "1", "2", "4", "8"]

    def xǁDuuxBright2TimerSelectorǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, device)
        # Bright 2 supports specific timer presets only (hours): 0=off, 1, 2, 4, 8
        self._attr_options = ["0", "1", "2", "4", "8"]

    def xǁDuuxBright2TimerSelectorǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, )
        # Bright 2 supports specific timer presets only (hours): 0=off, 1, 2, 4, 8
        self._attr_options = ["0", "1", "2", "4", "8"]

    def xǁDuuxBright2TimerSelectorǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        # Bright 2 supports specific timer presets only (hours): 0=off, 1, 2, 4, 8
        self._attr_options = None

    def xǁDuuxBright2TimerSelectorǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        # Bright 2 supports specific timer presets only (hours): 0=off, 1, 2, 4, 8
        self._attr_options = ["XX0XX", "1", "2", "4", "8"]

    def xǁDuuxBright2TimerSelectorǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        # Bright 2 supports specific timer presets only (hours): 0=off, 1, 2, 4, 8
        self._attr_options = ["0", "XX1XX", "2", "4", "8"]

    def xǁDuuxBright2TimerSelectorǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        # Bright 2 supports specific timer presets only (hours): 0=off, 1, 2, 4, 8
        self._attr_options = ["0", "1", "XX2XX", "4", "8"]

    def xǁDuuxBright2TimerSelectorǁ__init____mutmut_11(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        # Bright 2 supports specific timer presets only (hours): 0=off, 1, 2, 4, 8
        self._attr_options = ["0", "1", "2", "XX4XX", "8"]

    def xǁDuuxBright2TimerSelectorǁ__init____mutmut_12(self, coordinator, api, device):
        """Initialize the timer selector."""
        super().__init__(coordinator, api, device)
        # Bright 2 supports specific timer presets only (hours): 0=off, 1, 2, 4, 8
        self._attr_options = ["0", "1", "2", "4", "XX8XX"]

mutants_xǁDuuxBright2TimerSelectorǁ__init____mutmut['_mutmut_orig'] = DuuxBright2TimerSelector.xǁDuuxBright2TimerSelectorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimerSelectorǁ__init____mutmut['xǁDuuxBright2TimerSelectorǁ__init____mutmut_1'] = DuuxBright2TimerSelector.xǁDuuxBright2TimerSelectorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimerSelectorǁ__init____mutmut['xǁDuuxBright2TimerSelectorǁ__init____mutmut_2'] = DuuxBright2TimerSelector.xǁDuuxBright2TimerSelectorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimerSelectorǁ__init____mutmut['xǁDuuxBright2TimerSelectorǁ__init____mutmut_3'] = DuuxBright2TimerSelector.xǁDuuxBright2TimerSelectorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimerSelectorǁ__init____mutmut['xǁDuuxBright2TimerSelectorǁ__init____mutmut_4'] = DuuxBright2TimerSelector.xǁDuuxBright2TimerSelectorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimerSelectorǁ__init____mutmut['xǁDuuxBright2TimerSelectorǁ__init____mutmut_5'] = DuuxBright2TimerSelector.xǁDuuxBright2TimerSelectorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimerSelectorǁ__init____mutmut['xǁDuuxBright2TimerSelectorǁ__init____mutmut_6'] = DuuxBright2TimerSelector.xǁDuuxBright2TimerSelectorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimerSelectorǁ__init____mutmut['xǁDuuxBright2TimerSelectorǁ__init____mutmut_7'] = DuuxBright2TimerSelector.xǁDuuxBright2TimerSelectorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimerSelectorǁ__init____mutmut['xǁDuuxBright2TimerSelectorǁ__init____mutmut_8'] = DuuxBright2TimerSelector.xǁDuuxBright2TimerSelectorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimerSelectorǁ__init____mutmut['xǁDuuxBright2TimerSelectorǁ__init____mutmut_9'] = DuuxBright2TimerSelector.xǁDuuxBright2TimerSelectorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimerSelectorǁ__init____mutmut['xǁDuuxBright2TimerSelectorǁ__init____mutmut_10'] = DuuxBright2TimerSelector.xǁDuuxBright2TimerSelectorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimerSelectorǁ__init____mutmut['xǁDuuxBright2TimerSelectorǁ__init____mutmut_11'] = DuuxBright2TimerSelector.xǁDuuxBright2TimerSelectorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxBright2TimerSelectorǁ__init____mutmut['xǁDuuxBright2TimerSelectorǁ__init____mutmut_12'] = DuuxBright2TimerSelector.xǁDuuxBright2TimerSelectorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut: MutantDict = {}  # type: ignore


class DuuxNeoSpeedSelector(DuuxSelector):
    """Representation of a Duux Neo spray speed selector."""

    SPEED_LOW = "Low"
    SPEED_MID = "Mid"
    SPEED_HIGH = "High"

    @_mutmut_mutated(mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = "spray_volume"
        self._attr_icon = "mdi:weather-partly-rainy"
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    def xǁDuuxNeoSpeedSelectorǁ__init____mutmut_orig(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = "spray_volume"
        self._attr_icon = "mdi:weather-partly-rainy"
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    def xǁDuuxNeoSpeedSelectorǁ__init____mutmut_1(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(None, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = "spray_volume"
        self._attr_icon = "mdi:weather-partly-rainy"
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    def xǁDuuxNeoSpeedSelectorǁ__init____mutmut_2(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(coordinator, None, device)
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = "spray_volume"
        self._attr_icon = "mdi:weather-partly-rainy"
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    def xǁDuuxNeoSpeedSelectorǁ__init____mutmut_3(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(coordinator, api, None)
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = "spray_volume"
        self._attr_icon = "mdi:weather-partly-rainy"
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    def xǁDuuxNeoSpeedSelectorǁ__init____mutmut_4(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(api, device)
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = "spray_volume"
        self._attr_icon = "mdi:weather-partly-rainy"
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    def xǁDuuxNeoSpeedSelectorǁ__init____mutmut_5(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(coordinator, device)
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = "spray_volume"
        self._attr_icon = "mdi:weather-partly-rainy"
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    def xǁDuuxNeoSpeedSelectorǁ__init____mutmut_6(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(coordinator, api, )
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = "spray_volume"
        self._attr_icon = "mdi:weather-partly-rainy"
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    def xǁDuuxNeoSpeedSelectorǁ__init____mutmut_7(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = None
        self._attr_translation_key = "spray_volume"
        self._attr_icon = "mdi:weather-partly-rainy"
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    def xǁDuuxNeoSpeedSelectorǁ__init____mutmut_8(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = None
        self._attr_icon = "mdi:weather-partly-rainy"
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    def xǁDuuxNeoSpeedSelectorǁ__init____mutmut_9(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = "XXspray_volumeXX"
        self._attr_icon = "mdi:weather-partly-rainy"
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    def xǁDuuxNeoSpeedSelectorǁ__init____mutmut_10(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = "SPRAY_VOLUME"
        self._attr_icon = "mdi:weather-partly-rainy"
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    def xǁDuuxNeoSpeedSelectorǁ__init____mutmut_11(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = "spray_volume"
        self._attr_icon = None
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    def xǁDuuxNeoSpeedSelectorǁ__init____mutmut_12(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = "spray_volume"
        self._attr_icon = "XXmdi:weather-partly-rainyXX"
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    def xǁDuuxNeoSpeedSelectorǁ__init____mutmut_13(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = "spray_volume"
        self._attr_icon = "MDI:WEATHER-PARTLY-RAINY"
        self._attr_options = [self.SPEED_LOW, self.SPEED_MID, self.SPEED_HIGH]

    def xǁDuuxNeoSpeedSelectorǁ__init____mutmut_14(self, coordinator, api, device):
        """Initialize the speed selector."""
        super().__init__(coordinator, api, device)
        self._attr_unique_id = f"duux_{self._device_id}_speed"
        self._attr_translation_key = "spray_volume"
        self._attr_icon = "mdi:weather-partly-rainy"
        self._attr_options = None

    @property
    def current_option(self):
        """Return current speed."""
        mode = self.coordinator.data.get("speed", self.SPEED_LOW)
        mode_map = {
            0: self.SPEED_LOW,
            1: self.SPEED_MID,
            2: self.SPEED_HIGH,
        }
        return mode_map.get(mode, self.SPEED_LOW)

    @_mutmut_mutated(mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut)
    async def async_select_option(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_orig(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_1(self, option):
        """Set spray speed mode."""
        mode_map = None
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_2(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "XX0XX",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_3(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "XX1XX",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_4(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "XX2XX",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_5(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = None

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_6(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(None, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_7(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, None)

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_8(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get("0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_9(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, )

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_10(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "XX0XX")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_11(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            None, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_12(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, None, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_13(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, None, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_14(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, None, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_15(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, None
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_16(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_17(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_18(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_19(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_20(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_21(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 1, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_22(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 3
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_23(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = None
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_24(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = None
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_25(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["XXspeedXX"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_26(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["SPEED"] = int(mode)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_27(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(None)
        self.coordinator.async_set_updated_data(newData)

    async def xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_28(self, option):
        """Set spray speed mode."""
        mode_map = {
            self.SPEED_LOW: "0",
            self.SPEED_MID: "1",
            self.SPEED_HIGH: "2",
        }
        mode = mode_map.get(option, "0")

        await self.hass.async_add_executor_job(
            self._api.set_speed, self._device_mac, mode, 0, 2
        )
        newData = self.coordinator.data
        newData["speed"] = int(mode)
        self.coordinator.async_set_updated_data(None)

mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut['_mutmut_orig'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut['xǁDuuxNeoSpeedSelectorǁ__init____mutmut_1'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut['xǁDuuxNeoSpeedSelectorǁ__init____mutmut_2'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut['xǁDuuxNeoSpeedSelectorǁ__init____mutmut_3'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut['xǁDuuxNeoSpeedSelectorǁ__init____mutmut_4'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut['xǁDuuxNeoSpeedSelectorǁ__init____mutmut_5'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut['xǁDuuxNeoSpeedSelectorǁ__init____mutmut_6'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut['xǁDuuxNeoSpeedSelectorǁ__init____mutmut_7'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut['xǁDuuxNeoSpeedSelectorǁ__init____mutmut_8'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut['xǁDuuxNeoSpeedSelectorǁ__init____mutmut_9'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut['xǁDuuxNeoSpeedSelectorǁ__init____mutmut_10'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut['xǁDuuxNeoSpeedSelectorǁ__init____mutmut_11'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut['xǁDuuxNeoSpeedSelectorǁ__init____mutmut_12'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut['xǁDuuxNeoSpeedSelectorǁ__init____mutmut_13'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁ__init____mutmut['xǁDuuxNeoSpeedSelectorǁ__init____mutmut_14'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁ__init____mutmut_14 # type: ignore # mutmut generated

mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['_mutmut_orig'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_1'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_2'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_3'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_4'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_5'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_6'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_7'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_8'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_9'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_10'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_11'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_12'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_13'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_14'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_15'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_16'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_17'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_18'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_19'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_20'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_21'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_22'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_23'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_24'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_25'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_26'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_27'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut['xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_28'] = DuuxNeoSpeedSelector.xǁDuuxNeoSpeedSelectorǁasync_select_option__mutmut_28 # type: ignore # mutmut generated
