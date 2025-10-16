"""Custom types for integration_blueprint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import DuuxApiClient
    from .coordinator import BlueprintDataUpdateCoordinator


type DuuxConfigEntry = ConfigEntry[DuuxData]


@dataclass
class DuuxData:
    """Data for the Duux integration."""

    client: DuuxApiClient
    coordinator: BlueprintDataUpdateCoordinator
    integration: Integration