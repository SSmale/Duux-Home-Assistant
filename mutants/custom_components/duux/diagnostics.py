"""Support for Duux diagnostics."""

from typing import Any
from homeassistant.components.diagnostics.util import async_redact_data
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import UpdateFailed

from .const import DOMAIN

TO_REDACT = ["deviceId", "sensor"]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_async_get_config_entry_diagnostics__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_async_get_config_entry_diagnostics__mutmut)
async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for all Duux devices."""
    api = hass.data[DOMAIN][entry.entry_id]["api"]

    try:
        data = await hass.async_add_executor_job(api.get_devices)
        return async_redact_data(data, TO_REDACT)
    except Exception as err:
        raise UpdateFailed(f"Error communicating with API: {err}")


async def x_async_get_config_entry_diagnostics__mutmut_orig(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for all Duux devices."""
    api = hass.data[DOMAIN][entry.entry_id]["api"]

    try:
        data = await hass.async_add_executor_job(api.get_devices)
        return async_redact_data(data, TO_REDACT)
    except Exception as err:
        raise UpdateFailed(f"Error communicating with API: {err}")


async def x_async_get_config_entry_diagnostics__mutmut_1(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for all Duux devices."""
    api = None

    try:
        data = await hass.async_add_executor_job(api.get_devices)
        return async_redact_data(data, TO_REDACT)
    except Exception as err:
        raise UpdateFailed(f"Error communicating with API: {err}")


async def x_async_get_config_entry_diagnostics__mutmut_2(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for all Duux devices."""
    api = hass.data[DOMAIN][entry.entry_id]["XXapiXX"]

    try:
        data = await hass.async_add_executor_job(api.get_devices)
        return async_redact_data(data, TO_REDACT)
    except Exception as err:
        raise UpdateFailed(f"Error communicating with API: {err}")


async def x_async_get_config_entry_diagnostics__mutmut_3(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for all Duux devices."""
    api = hass.data[DOMAIN][entry.entry_id]["API"]

    try:
        data = await hass.async_add_executor_job(api.get_devices)
        return async_redact_data(data, TO_REDACT)
    except Exception as err:
        raise UpdateFailed(f"Error communicating with API: {err}")


async def x_async_get_config_entry_diagnostics__mutmut_4(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for all Duux devices."""
    api = hass.data[DOMAIN][entry.entry_id]["api"]

    try:
        data = None
        return async_redact_data(data, TO_REDACT)
    except Exception as err:
        raise UpdateFailed(f"Error communicating with API: {err}")


async def x_async_get_config_entry_diagnostics__mutmut_5(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for all Duux devices."""
    api = hass.data[DOMAIN][entry.entry_id]["api"]

    try:
        data = await hass.async_add_executor_job(None)
        return async_redact_data(data, TO_REDACT)
    except Exception as err:
        raise UpdateFailed(f"Error communicating with API: {err}")


async def x_async_get_config_entry_diagnostics__mutmut_6(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for all Duux devices."""
    api = hass.data[DOMAIN][entry.entry_id]["api"]

    try:
        data = await hass.async_add_executor_job(api.get_devices)
        return async_redact_data(None, TO_REDACT)
    except Exception as err:
        raise UpdateFailed(f"Error communicating with API: {err}")


async def x_async_get_config_entry_diagnostics__mutmut_7(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for all Duux devices."""
    api = hass.data[DOMAIN][entry.entry_id]["api"]

    try:
        data = await hass.async_add_executor_job(api.get_devices)
        return async_redact_data(data, None)
    except Exception as err:
        raise UpdateFailed(f"Error communicating with API: {err}")


async def x_async_get_config_entry_diagnostics__mutmut_8(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for all Duux devices."""
    api = hass.data[DOMAIN][entry.entry_id]["api"]

    try:
        data = await hass.async_add_executor_job(api.get_devices)
        return async_redact_data(TO_REDACT)
    except Exception as err:
        raise UpdateFailed(f"Error communicating with API: {err}")


async def x_async_get_config_entry_diagnostics__mutmut_9(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for all Duux devices."""
    api = hass.data[DOMAIN][entry.entry_id]["api"]

    try:
        data = await hass.async_add_executor_job(api.get_devices)
        return async_redact_data(data, )
    except Exception as err:
        raise UpdateFailed(f"Error communicating with API: {err}")


async def x_async_get_config_entry_diagnostics__mutmut_10(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for all Duux devices."""
    api = hass.data[DOMAIN][entry.entry_id]["api"]

    try:
        data = await hass.async_add_executor_job(api.get_devices)
        return async_redact_data(data, TO_REDACT)
    except Exception as err:
        raise UpdateFailed(None)

mutants_x_async_get_config_entry_diagnostics__mutmut['_mutmut_orig'] = x_async_get_config_entry_diagnostics__mutmut_orig # type: ignore # mutmut generated
mutants_x_async_get_config_entry_diagnostics__mutmut['x_async_get_config_entry_diagnostics__mutmut_1'] = x_async_get_config_entry_diagnostics__mutmut_1 # type: ignore # mutmut generated
mutants_x_async_get_config_entry_diagnostics__mutmut['x_async_get_config_entry_diagnostics__mutmut_2'] = x_async_get_config_entry_diagnostics__mutmut_2 # type: ignore # mutmut generated
mutants_x_async_get_config_entry_diagnostics__mutmut['x_async_get_config_entry_diagnostics__mutmut_3'] = x_async_get_config_entry_diagnostics__mutmut_3 # type: ignore # mutmut generated
mutants_x_async_get_config_entry_diagnostics__mutmut['x_async_get_config_entry_diagnostics__mutmut_4'] = x_async_get_config_entry_diagnostics__mutmut_4 # type: ignore # mutmut generated
mutants_x_async_get_config_entry_diagnostics__mutmut['x_async_get_config_entry_diagnostics__mutmut_5'] = x_async_get_config_entry_diagnostics__mutmut_5 # type: ignore # mutmut generated
mutants_x_async_get_config_entry_diagnostics__mutmut['x_async_get_config_entry_diagnostics__mutmut_6'] = x_async_get_config_entry_diagnostics__mutmut_6 # type: ignore # mutmut generated
mutants_x_async_get_config_entry_diagnostics__mutmut['x_async_get_config_entry_diagnostics__mutmut_7'] = x_async_get_config_entry_diagnostics__mutmut_7 # type: ignore # mutmut generated
mutants_x_async_get_config_entry_diagnostics__mutmut['x_async_get_config_entry_diagnostics__mutmut_8'] = x_async_get_config_entry_diagnostics__mutmut_8 # type: ignore # mutmut generated
mutants_x_async_get_config_entry_diagnostics__mutmut['x_async_get_config_entry_diagnostics__mutmut_9'] = x_async_get_config_entry_diagnostics__mutmut_9 # type: ignore # mutmut generated
mutants_x_async_get_config_entry_diagnostics__mutmut['x_async_get_config_entry_diagnostics__mutmut_10'] = x_async_get_config_entry_diagnostics__mutmut_10 # type: ignore # mutmut generated
