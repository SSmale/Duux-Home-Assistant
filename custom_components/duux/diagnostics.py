"""Support for Duux diagnostics."""

from typing import Any
from homeassistant.components.diagnostics.util import async_redact_data
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import UpdateFailed

from .const import CONF_MODE_MAPPING, DEFAULT_MODE_MAPPING, DOMAIN

TO_REDACT = ["deviceId", "sensor"]


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for all Duux devices."""
    api = hass.data[DOMAIN][entry.entry_id]["api"]
    devices = hass.data[DOMAIN][entry.entry_id].get("devices", [])

    try:
        raw_data = await hass.async_add_executor_job(api.get_devices)
    except Exception as err:
        raise UpdateFailed(f"Error communicating with API: {err}")

    saved_mappings = entry.options.get(CONF_MODE_MAPPING, {})
    mode_mapping_info = {}
    for device in devices:
        device_id = device.get("deviceId")
        if device_id is None:
            continue
        custom = device_id in saved_mappings
        mode_mapping_info[device_id] = {
            "is_custom": custom,
            "mapping": saved_mappings.get(device_id) if custom else DEFAULT_MODE_MAPPING,
        }

    return {
        "devices": async_redact_data(raw_data, TO_REDACT),
        "mode_mappings": mode_mapping_info,
    }
