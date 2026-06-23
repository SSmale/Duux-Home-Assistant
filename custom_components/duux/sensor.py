"""Support for Duux sensors."""

from __future__ import annotations
import logging

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import (
    EntityCategory,
    PERCENTAGE,
    UnitOfTemperature,
    UnitOfTime,
)
from homeassistant.core import callback
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    ATTRIBUTION,
    CONF_MODE_MAPPING,
    DEFAULT_MODE_MAPPING,
    DOMAIN,
    DUUX_DTID_HEATER,
    DUUX_DTID_THERMOSTAT,
    DUUX_ERRID,
    DUUX_STID_BEAM_MINI,
    DUUX_STID_BORA_2024,
    DUUX_STID_BRIGHT_2,
)

_LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class DuuxSensorEntityDescription(SensorEntityDescription):
    """Class describing Duux sensor entities."""

    attrs: Callable[[dict[str, Any]], dict[str, Any]] = lambda data: {}


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Duux sensor entities based on a config entry."""
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]
    mode_mapping_options = config_entry.options.get(CONF_MODE_MAPPING, {})

    entities = []
    for device in devices:
        sensor_type_id = device.get("sensorTypeId")
        device_id = device["deviceId"]
        coordinator = coordinators.get(device_id)
        device_type_id = (device.get("sensorType") or {}).get("type")

        # Skip devices that have no coordinator (were filtered out in __init__)
        if coordinator is None:
            continue

        if sensor_type_id == DUUX_STID_BORA_2024:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxBora2024TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BRIGHT_2:
            entities.append(DuuxPM25Sensor(coordinator, api, device))
            entities.append(DuuxTVOCSensor(coordinator, api, device))
            entities.append(DuuxFilterLifeSensor(coordinator, api, device))
            entities.append(DuuxAirQualitySensor(coordinator, api, device))
            entities.append(DuuxBright2TimeRemainingSensor(coordinator, api, device))
        elif sensor_type_id == DUUX_STID_BEAM_MINI:
            entities.append(DuuxHumiditySensor(coordinator, api, device))
            entities.append(DuuxTempSensor(coordinator, api, device))
        elif coordinator.data.get("temp") is not None:
            entities.append(DuuxTempSensor(coordinator, api, device))

        entities.append(DuuxErrorSensor(coordinator, api, device))
        entities.append(DuuxConnectionTypeSensor(coordinator, api, device))

        if device_type_id in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
            device_mode_mapping = mode_mapping_options.get(device_id, DEFAULT_MODE_MAPPING)
            entities.append(DuuxModeMappingSensor(coordinator, api, device, device_mode_mapping))

    async_add_entities(entities)


class DuuxSensor(CoordinatorEntity, SensorEntity):
    """Define an Duux sensor."""

    _attr_attribution = ATTRIBUTION
    entity_description: DuuxSensorEntityDescription

    def __init__(self, coordinator, api, device, description):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._coordinator = coordinator
        self._device = device
        self._device_id = device["id"]
        self._device_mac = device["deviceId"]  # MAC address
        self._attr_unique_id = f"duux_{self._device_id}_{description.key}"
        self.device_name = device.get("displayName") or device.get("name")
        self._attr_has_entity_name = True

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(self._device_id))},
            manufacturer=self._device.get("manufacturer", "Duux"),
            name=self.device_name,
        )
        _init_data = coordinator.data or {}
        self._attr_native_value = _init_data.get(description.key)
        self._attr_extra_state_attributes = description.attrs(_init_data)
        self.entity_description = description

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.last_update_success and (
            self.coordinator.data or {}
        ).get("online", True)

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        data = self.coordinator.data or {}
        self._attr_native_value = data.get(self.entity_description.key)
        self._attr_extra_state_attributes = self.entity_description.attrs(data)
        self.async_write_ha_state()


class DuuxTempSensor(DuuxSensor):
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="temp",
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=UnitOfTemperature.CELSIUS,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )


class DuuxPM25Sensor(DuuxSensor):
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="ppm",
                translation_key="pm25",
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement="µg/m³",
                state_class=SensorStateClass.MEASUREMENT,
            ),
        )


class DuuxTVOCSensor(DuuxSensor):
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="tvoc",
                translation_key="tvoc",
                # TVOC is a discrete level 0-3: 0=Healthy, 1=Acceptable, 2=Polluted, 3=Harmful
            ),
        )

    _TVOC_MAP = {
        0: "healthy",
        1: "acceptable",
        2: "polluted",
        3: "harmful",
    }

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        data = self.coordinator.data or {}
        raw = data.get("tvoc")
        self._attr_native_value = (
            self._TVOC_MAP.get(raw, raw) if raw is not None else None
        )
        self._attr_extra_state_attributes = self.entity_description.attrs(data)
        self.async_write_ha_state()


class DuuxFilterLifeSensor(DuuxSensor):
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="filter",
                translation_key="filter_life",
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                icon="mdi:air-filter",
            ),
        )


class DuuxAirQualitySensor(DuuxSensor):
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="aq",
                translation_key="air_quality_index",
            ),
        )

    _AQ_MAP = {
        0: "excellent",
        1: "very_good",
        2: "good",
        3: "fair",
        4: "poor",
        5: "harmful",
    }

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        data = self.coordinator.data or {}
        raw = data.get("aq")
        # Map integer API value to translation key; fall back to raw value if unknown
        self._attr_native_value = (
            self._AQ_MAP.get(raw, raw) if raw is not None else None
        )
        self._attr_extra_state_attributes = self.entity_description.attrs(data)
        self.async_write_ha_state()


class DuuxHumiditySensor(DuuxSensor):
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="hum",
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=PERCENTAGE,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )


class DuuxTimeRemainingSensor(DuuxSensor):
    """Base time remaining sensor — subclass per device to set the correct API key."""

    def __init__(self, coordinator, api, device, key: str):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key=key,
                translation_key="time_remaining",
                device_class=SensorDeviceClass.DURATION,
                native_unit_of_measurement=UnitOfTime.MINUTES,
                state_class=SensorStateClass.MEASUREMENT,
                suggested_display_precision=1,
            ),
        )


class DuuxErrorSensor(DuuxSensor):
    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="err",
                translation_key="error_message",
            ),
        )
        self._attr_icon = "mdi:comment-alert-outline"

    @property
    def native_value(self):
        data = self.coordinator.data or {}
        key = self.entity_description.key
        errid = DUUX_ERRID(data[key]) if key in data else DUUX_ERRID.Unavailable
        return errid.name.replace("_", " ")


class DuuxConnectionTypeSensor(DuuxSensor):
    """Enum sensor reporting whether the device is connected via MQTT or TCP.

    'connectionType' lives on the device envelope returned by /smarthome/sensors
    rather than in the polled status payload, but DuuxAPI.get_device_status()
    stitches it into the coordinator data (the same way it already does for
    'online'), so this updates on every coordinator refresh rather than being
    frozen at integration setup.
    """

    def __init__(self, coordinator, api, device):
        super().__init__(
            coordinator,
            api,
            device,
            DuuxSensorEntityDescription(
                key="connectionType",
                translation_key="connection_type",
                device_class=SensorDeviceClass.ENUM,
                options=["mqtt", "tcp"],
                entity_category=EntityCategory.DIAGNOSTIC,
                icon="mdi:wan",
            ),
        )

    @property
    def native_value(self):
        """Return the connection type, normalised to match the declared options."""
        value = (self.coordinator.data or {}).get(self.entity_description.key)
        return value.lower() if isinstance(value, str) else None


class DuuxBora2024TimeRemainingSensor(DuuxTimeRemainingSensor):
    """Time remaining sensor for Duux Bora 2024 (API key: 'timrm')."""

    def __init__(self, coordinator, api, device):
        super().__init__(coordinator, api, device, key="timrm")


class DuuxBright2TimeRemainingSensor(DuuxTimeRemainingSensor):
    """Time remaining sensor for Duux Bright 2 (API key: 'timerr')."""

    def __init__(self, coordinator, api, device):
        super().__init__(coordinator, api, device, key="timerr")


class DuuxModeMappingSensor(CoordinatorEntity, SensorEntity):
    """Diagnostic enum sensor showing whether a heater uses a custom or default mode mapping.

    Shows 'custom' or 'default' as its state; exposes the full index-to-preset
    mapping as extra attributes so it is visible in Developer Tools and entity cards.
    """

    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name = True
    _attr_entity_category = EntityCategory.DIAGNOSTIC
    _attr_device_class = SensorDeviceClass.ENUM
    _attr_options = ["custom", "default"]
    _attr_translation_key = "mode_mapping_source"
    _attr_icon = "mdi:map"

    def __init__(self, coordinator, api, device, device_mode_mapping):
        super().__init__(coordinator)
        self._device_mode_mapping = device_mode_mapping
        self._device_mac = device["deviceId"]
        self._attr_unique_id = f"duux_{device['id']}_mode_mapping"

        device_name = (
            device.get("displayName")
            or (device.get("sensorType") or {}).get("name")
            or device.get("name")
        )
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, str(device["id"]))},
            manufacturer=device.get("manufacturer", "Duux"),
            name=device_name,
        )

    @property
    def available(self) -> bool:
        return self.coordinator.last_update_success and (
            self.coordinator.data or {}
        ).get("online", True)

    @property
    def native_value(self) -> str:
        return "custom" if self._device_mode_mapping is not DEFAULT_MODE_MAPPING else "default"

    @property
    def extra_state_attributes(self) -> dict:
        mapping = {int(k): v for k, v in self._device_mode_mapping.items()}
        return {"mapping": {f"mode_{k}": v for k, v in mapping.items()}}
