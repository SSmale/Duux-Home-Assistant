"""Sensor platform for Duux."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription

from .entity import DuuxEntity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import BlueprintDataUpdateCoordinator
    from .data import DuuxConfigEntry

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="heatin",
        name="Heating Mode",
        icon="mdi:speedometer-medium",
    ),
        SensorEntityDescription(
        key="sp",
        name="Target Temperature",
        icon="mdi:thermometer-check",
    ),
        SensorEntityDescription(
        key="temp",
        name="Current Temperature",
        icon="mdi:home-thermometer-outline",
    ),
        SensorEntityDescription(
        key="timer",
        name="Timer",
        icon="mdi:timer-outline",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: DuuxConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities(
        DuuxSensor(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class DuuxSensor(DuuxEntity, SensorEntity):
    """Duux Sensor class."""

    def __init__(
        self,
        coordinator: BlueprintDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def native_value(self) -> str | None:
        """Return the native value of the sensor."""
        return self.coordinator.data.get("body")