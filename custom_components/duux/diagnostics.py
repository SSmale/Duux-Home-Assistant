"""Support for Duux diagnostics."""
from __future__ import annotations

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

TO_REDACT = [
    "deviceId",
    "sensor"
]

async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for all Duux devices."""
    data = hass.data[DOMAIN][entry.entry_id]
    return async_redact_data(data["devices"], TO_REDACT)