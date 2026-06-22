"""Support for Duux sensors."""

from __future__ import annotations
import logging
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.core import callback
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, ATTRIBUTION, DUUX_ERRID

_LOGGER = logging.getLogger(__name__)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class DuuxBinarySensorEntityDescription(BinarySensorEntityDescription):
    """Class describing Duux binary sensor entities."""

    attrs: Callable[[dict[str, Any]], dict[str, Any]] = lambda data: {}
mutants_x_async_setup_entry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_async_setup_entry__mutmut)
async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_orig(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_1(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = None
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_2(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = None
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_3(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["XXapiXX"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_4(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["API"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_5(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = None
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_6(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["XXcoordinatorsXX"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_7(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["COORDINATORS"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_8(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = None

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_9(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["XXdevicesXX"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_10(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["DEVICES"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_11(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = None
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_12(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = None
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_13(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["XXdeviceIdXX"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_14(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceid"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_15(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["DEVICEID"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_16(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = None

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_17(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(None)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_18(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is not None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_19(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            break

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_20(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(None)
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_21(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(None, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_22(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, None, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_23(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, None))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_24(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_25(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_26(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, ))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_27(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(None)

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_28(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(None, api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_29(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, None, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_30(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, None))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_31(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(api, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_32(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, device))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_33(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, ))

    async_add_entities(entities)


async def x_async_setup_entry__mutmut_34(hass, config_entry, async_add_entities):
    """Set up Duux binary sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]

    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinator = coordinators.get(device_id)

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectivitySensor(coordinator, api, device))

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
mutants_xǁDuuxBinarySensorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxBinarySensor(CoordinatorEntity, BinarySensorEntity):
    """Define a Duux binary sensor."""

    _attr_attribution = ATTRIBUTION
    entity_description: DuuxBinarySensorEntityDescription

    @_mutmut_mutated(mutants_xǁDuuxBinarySensorǁ__init____mutmut)
    def __init__(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_orig(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_1(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(None)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_2(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = None
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_3(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = None
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_4(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = None
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_5(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = None
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_6(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["XXidXX"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_7(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["ID"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_8(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = None
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_9(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["XXdeviceIdXX"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_10(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceid"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_11(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["DEVICEID"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_12(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = None
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_13(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = None
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_14(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") and device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_15(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get(None) or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_16(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("XXdisplayNameXX") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_17(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayname") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_18(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("DISPLAYNAME") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_19(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get(None)
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_20(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("XXnameXX")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_21(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("NAME")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_22(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = None

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_23(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = False

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_24(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = None
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_25(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers=None,
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_26(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=None,
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_27(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=None,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_28(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_29(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_30(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_31(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(None))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_32(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get(None, "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_33(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", None),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_34(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_35(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", ),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_36(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("XXmanufacturerXX", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_37(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("MANUFACTURER", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_38(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "XXDuuxXX"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_39(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_40(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "DUUX"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_41(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = None
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_42(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(None)
        self.entity_description = description

    def xǁDuuxBinarySensorǁ__init____mutmut_43(self, coordinator, api, device, description):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        self._attr_extra_state_attributes = description.attrs(coordinator.data)
        self.entity_description = None

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_extra_state_attributes = self.entity_description.attrs(
            self.coordinator.data
        )
        self.async_write_ha_state()

mutants_xǁDuuxBinarySensorǁ__init____mutmut['_mutmut_orig'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_1'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_2'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_3'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_4'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_5'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_6'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_7'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_8'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_9'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_10'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_11'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_12'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_13'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_14'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_15'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_16'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_17'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_18'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_19'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_20'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_21'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_22'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_23'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_24'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_25'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_26'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_27'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_27 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_28'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_28 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_29'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_29 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_30'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_30 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_31'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_31 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_32'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_32 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_33'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_33 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_34'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_34 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_35'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_35 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_36'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_36 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_37'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_37 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_38'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_38 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_39'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_39 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_40'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_40 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_41'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_41 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_42'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_42 # type: ignore # mutmut generated
mutants_xǁDuuxBinarySensorǁ__init____mutmut['xǁDuuxBinarySensorǁ__init____mutmut_43'] = DuuxBinarySensor.xǁDuuxBinarySensorǁ__init____mutmut_43 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxErrorSensor(DuuxBinarySensor):
    """Binary sensor that fires when the device reports an error code."""

    @_mutmut_mutated(mutants_xǁDuuxErrorSensorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_orig(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_1(self, coordinator, api, device):
        super().__init__(
            None,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_2(self, coordinator, api, device):
        super().__init__(
            coordinator,
            None,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_3(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            None,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_4(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            None,
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_5(self, coordinator, api, device):
        super().__init__(
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_6(self, coordinator, api, device):
        super().__init__(
            coordinator,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_7(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_8(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            )

    def xǁDuuxErrorSensorǁ__init____mutmut_9(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key=None,
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_10(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key=None,
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_11(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=None,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_12(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=None,
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_13(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_14(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_15(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_16(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_17(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="XXerrXX",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_18(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="ERR",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_19(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="XXproblemXX",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_20(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="PROBLEM",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_21(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: None,
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_22(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "XXerror_codeXX": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_23(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "ERROR_CODE": (data or {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_24(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get(None),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_25(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data and {}).get("err"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_26(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("XXerrXX"),
                },
            ),
        )

    def xǁDuuxErrorSensorǁ__init____mutmut_27(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                translation_key="problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("ERR"),
                },
            ),
        )

    @property
    def is_on(self) -> bool:
        """True when the device reports a non-OK error code."""
        data = self.coordinator.data or {}
        key = self.entity_description.key
        errid = DUUX_ERRID(data[key]) if key in data else DUUX_ERRID.Unavailable
        return errid not in (DUUX_ERRID.OK, DUUX_ERRID.Unavailable)

mutants_xǁDuuxErrorSensorǁ__init____mutmut['_mutmut_orig'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_1'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_2'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_3'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_4'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_5'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_6'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_7'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_8'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_9'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_10'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_11'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_12'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_13'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_14'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_15'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_16'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_17'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_18'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_19'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_20'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_21'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_22'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_23'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_24'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_25'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_26'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuuxErrorSensorǁ__init____mutmut['xǁDuuxErrorSensorǁ__init____mutmut_27'] = DuuxErrorSensor.xǁDuuxErrorSensorǁ__init____mutmut_27 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut: MutantDict = {}  # type: ignore


class DuuxConnectivitySensor(DuuxBinarySensor):
    """Binary sensor that reflects whether the device is online."""

    @_mutmut_mutated(mutants_xǁDuuxConnectivitySensorǁ__init____mutmut)
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_orig(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_1(self, coordinator, api, device):
        super().__init__(
            None,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_2(self, coordinator, api, device):
        super().__init__(
            coordinator,
            None,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_3(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            None,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_4(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            None,
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_5(self, coordinator, api, device):
        super().__init__(
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_6(self, coordinator, api, device):
        super().__init__(
            coordinator,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_7(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_8(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_9(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key=None,
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_10(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key=None,
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_11(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=None,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_12(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=None,
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_13(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_14(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_15(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_16(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_17(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="XXconnectivityXX",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_18(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="CONNECTIVITY",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_19(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="XXconnectedXX",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_20(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="CONNECTED",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_21(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: None,
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_22(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "XXlast_seenXX": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_23(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "LAST_SEEN": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_24(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get(None),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_25(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("XXconnectionUpdateDateXX"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_26(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionupdatedate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_27(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("CONNECTIONUPDATEDATE"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_28(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "XXconnection_typeXX": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_29(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "CONNECTION_TYPE": device.get("connectionType"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_30(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get(None),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_31(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("XXconnectionTypeXX"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_32(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectiontype"),
                },
            ),
        )

    def xǁDuuxConnectivitySensorǁ__init____mutmut_33(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                translation_key="connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("CONNECTIONTYPE"),
                },
            ),
        )

    @property
    def is_on(self) -> bool:
        """True when the device is online.

        CONNECTIVITY device class: True = Connected, False = Disconnected.
        The 'online' flag lives on the device envelope, not the polled
        status payload, so we read from self._device rather than
        coordinator.data.
        """
        return bool(self._device.get("online", False))

mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['_mutmut_orig'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_1'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_2'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_3'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_4'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_5'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_6'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_7'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_8'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_9'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_10'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_11'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_12'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_13'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_14'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_15'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_16'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_17'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_18'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_19'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_20'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_21'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_22'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_23'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_24'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_25'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_26'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_27'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_27 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_28'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_28 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_29'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_29 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_30'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_30 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_31'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_31 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_32'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_32 # type: ignore # mutmut generated
mutants_xǁDuuxConnectivitySensorǁ__init____mutmut['xǁDuuxConnectivitySensorǁ__init____mutmut_33'] = DuuxConnectivitySensor.xǁDuuxConnectivitySensorǁ__init____mutmut_33 # type: ignore # mutmut generated
