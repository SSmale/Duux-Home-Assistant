# custom_components/duux/config_flow.py
import datetime
import logging

import voluptuous as vol
from homeassistant.config_entries import ConfigFlow, OptionsFlowWithReload
from homeassistant.components.climate.const import (
    PRESET_BOOST,
    PRESET_COMFORT,
    PRESET_ECO,
)
from homeassistant.const import CONF_EMAIL, CONF_PASSWORD
from homeassistant.core import callback

from .const import (
    AVAILABLE_PRESETS,
    CONF_MODE_MAPPING,
    DEFAULT_MODE_MAPPING,
    DOMAIN,
)
from .duux_api import DuuxAPI

_LOGGER = logging.getLogger(__name__)


class DuuxConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Duux."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Test the credentials
            api = DuuxAPI(
                email=user_input[CONF_EMAIL], password=user_input[CONF_PASSWORD]
            )

            if await self.hass.async_add_executor_job(api.login):
                # Create entry
                return self.async_create_entry(
                    title=user_input[CONF_EMAIL], data=user_input
                )
            else:
                errors["base"] = "invalid_auth"

        data_schema = vol.Schema(
            {
                vol.Required(CONF_EMAIL): str,
                vol.Required(CONF_PASSWORD): str,
            }
        )

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        # return MyOptionsFlow()
        return DuuxOptionsFlow()


class DuuxOptionsFlow(OptionsFlowWithReload):
    """Handle options flow for Duux."""

    def __init__(self):
        """Initialize options flow."""
        self._devices = None
        self._selected_device = None

    async def async_step_init(self, user_input=None):
        """Manage the options - select device to configure."""
        # Get devices from integration data
        if (
            DOMAIN in self.hass.data
            and self.config_entry.entry_id in self.hass.data[DOMAIN]
        ):
            devices = self.hass.data[DOMAIN][self.config_entry.entry_id].get("devices")

            for device in devices:
                device_id = device.get("deviceId")
                device_name = device.get("displayName") or device.get("name")
                if self._devices is None:
                    self._devices = {}
                self._devices[device_id] = device_name

        if not self._devices:
            # No devices found, show global options only
            return await self.async_step_global_options(user_input)

        if user_input is not None:
            if "device_id" in user_input:
                self._selected_device = user_input["device_id"]
                res = await self.async_step_device_mode_mapping()
                _LOGGER.debug(
                    "Navigating to device mode mapping step for device %s", res
                )
                return res
            _LOGGER.debug("Saving options: %s", user_input)
            return self.async_create_entry(
                title="", data={"now": datetime.datetime.now()}
            )

        # Build device selection schema
        device_schema = {
            vol.Optional("device_id"): vol.In(self._devices, "Please select a device")
        }

        return self.async_show_form(
            last_step=False,
            step_id="init",
            data_schema=vol.Schema(device_schema),
            description_placeholders={
                "info": "Select a device to configure its heating mode mappings, or leave empty to finish."
            },
        )

    async def async_step_device_mode_mapping(self, user_input=None):
        """Configure mode mapping for selected device."""
        if user_input is not None:
            # Get existing options
            options = dict(self.config_entry.options)

            # Initialize mode_mapping dict if it doesn't exist
            if CONF_MODE_MAPPING not in options:
                options[CONF_MODE_MAPPING] = {}

            # Store the mapping for this device
            options[CONF_MODE_MAPPING][self._selected_device] = {
                "0": user_input["mode_0"],
                "1": user_input["mode_1"],
                "2": user_input["mode_2"],
                "3": user_input["mode_3"],
            }
            _LOGGER.debug(
                "Updated mode mapping for device %s: %s",
                self._selected_device,
                options[CONF_MODE_MAPPING][self._selected_device],
            )
            # Save and go back to device selection
            return self.async_create_entry(data=options)

        # Get current mapping for this device or use defaults
        current_mapping = self.config_entry.options.get(CONF_MODE_MAPPING, {}).get(
            self._selected_device, DEFAULT_MODE_MAPPING
        )

        # Convert keys to strings if they're integers
        if isinstance(current_mapping, dict) and all(
            isinstance(k, int) for k in current_mapping.keys()
        ):
            current_mapping = {str(k): v for k, v in current_mapping.items()}

        device_name = self._devices.get(self._selected_device, "Unknown Device")

        return self.async_show_form(
            step_id="device_mode_mapping",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        "mode_0", default=current_mapping.get("0", PRESET_ECO)
                    ): vol.In(AVAILABLE_PRESETS),
                    vol.Required(
                        "mode_1", default=current_mapping.get("1", PRESET_COMFORT)
                    ): vol.In(AVAILABLE_PRESETS),
                    vol.Required(
                        "mode_2", default=current_mapping.get("2", PRESET_BOOST)
                    ): vol.In(AVAILABLE_PRESETS),
                    vol.Required(
                        "mode_3", default=current_mapping.get("3", PRESET_BOOST)
                    ): vol.In(AVAILABLE_PRESETS),
                }
            ),
            description_placeholders={
                "device_name": device_name,
                "info": "Map each mode index (0, 1, 2, 3) to the corresponding heating preset (low, high, boost).",
            },
        )

    async def async_step_global_options(self, user_input=None):
        """Show global options if no devices available."""
        if user_input is not None:
            _LOGGER.debug("Saving global options: %s", user_input)
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="global_options",
            data_schema=vol.Schema({}),
            description_placeholders={
                "info": "No devices found. Make sure your heaters are connected."
            },
        )
