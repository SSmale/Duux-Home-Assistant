# custom_components/duux/config_flow.py
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
    DUUX_DTID_HEATER,
    DUUX_DTID_THERMOSTAT,
)
from .duux_api import DuuxAPI


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
        return DuuxOptionsFlow()


class DuuxOptionsFlow(OptionsFlowWithReload):
    """Handle options flow for Duux."""

    def __init__(self):
        """Initialize options flow."""
        self._devices: dict = {}
        self._selected_device = None

    async def async_step_init(self, user_input=None):
        """Manage the options - select device to configure."""
        if (
            DOMAIN in self.hass.data
            and self.config_entry.entry_id in self.hass.data[DOMAIN]
        ):
            devices = self.hass.data[DOMAIN][self.config_entry.entry_id].get("devices")

            for device in devices:
                sensor_type = device.get("sensorType") or {}
                device_type_id = sensor_type.get("type")
                if device_type_id not in [*DUUX_DTID_HEATER, *DUUX_DTID_THERMOSTAT]:
                    continue
                device_id = device.get("deviceId")
                device_name = (
                    device.get("displayName")
                    or sensor_type.get("name")
                    or device.get("name")
                )
                self._devices[device_id] = device_name

        if not self._devices:
            # No devices found, show global options only
            return await self.async_step_global_options(user_input)

        if user_input is not None:
            if "device_id" in user_input:
                self._selected_device = user_input["device_id"]
                return await self.async_step_device_mode_mapping()
            return self.async_create_entry(data=dict(self.config_entry.options))

        device_schema = {vol.Optional("device_id"): vol.In(self._devices)}

        return self.async_show_form(
            last_step=False,
            step_id="init",
            data_schema=vol.Schema(device_schema),
        )

    async def async_step_device_mode_mapping(self, user_input=None):
        """Configure mode mapping for selected device."""
        if user_input is not None:
            device_mapping = {
                "0": user_input["mode_0"],
                "1": user_input["mode_1"],
                "2": user_input["mode_2"],
                "3": user_input["mode_3"],
            }
            options = {
                **self.config_entry.options,
                CONF_MODE_MAPPING: {
                    **self.config_entry.options.get(CONF_MODE_MAPPING, {}),
                    self._selected_device: device_mapping,
                },
            }
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
                        "mode_3", default=current_mapping.get("3")
                    ): vol.In(AVAILABLE_PRESETS),
                }
            ),
            description_placeholders={"device_name": device_name},
        )

    async def async_step_global_options(self, user_input=None):
        """Show global options if no devices available."""
        if user_input is not None:
            return self.async_create_entry(data=user_input)

        return self.async_show_form(
            step_id="global_options",
            data_schema=vol.Schema({}),
        )
