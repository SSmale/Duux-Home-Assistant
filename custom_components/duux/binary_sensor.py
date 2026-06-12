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


@dataclass(frozen=True)
class DuuxBinarySensorEntityDescription(BinarySensorEntityDescription):
    """Class describing Duux binary sensor entities."""

    attrs: Callable[[dict[str, Any]], dict[str, Any]] = lambda data: {}


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


class DuuxBinarySensor(CoordinatorEntity, BinarySensorEntity):
    """Define a Duux binary sensor."""

    _attr_attribution = ATTRIBUTION
    entity_description: DuuxBinarySensorEntityDescription

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

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_extra_state_attributes = self.entity_description.attrs(
            self.coordinator.data
        )
        self.async_write_ha_state()


class DuuxErrorSensor(DuuxBinarySensor):
    """Binary sensor that fires when the device reports an error code."""

    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="err",
                name="Problem",
                device_class=BinarySensorDeviceClass.PROBLEM,
                attrs=lambda data: {
                    "error_code": (data or {}).get("err"),
                },
            ),
        )

    @property
    def is_on(self) -> bool:
        """True when the device reports a non-OK error code."""
        data = self.coordinator.data or {}
        err = data.get(self.entity_description.key)
        if err is None:
            return False
        return DUUX_ERRID(err) != DUUX_ERRID.OK


class DuuxConnectivitySensor(DuuxBinarySensor):
    """Binary sensor that reflects whether the device is online."""

    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxBinarySensorEntityDescription(
                key="connectivity",
                name="Connected",
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
                attrs=lambda data: {
                    "last_seen": device.get("connectionUpdateDate"),
                    "connection_type": device.get("connectionType"),
                },
            ),
        )

    @property
    def is_on(self):
        return (
            DUUX_ERRID(self.coordinator.data.get(self.entity_description.key))
            != DUUX_ERRID.OK
        )
