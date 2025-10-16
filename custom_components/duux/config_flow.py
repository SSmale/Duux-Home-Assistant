# custom_components/duux/config_flow.py

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_EMAIL, CONF_PASSWORD

from .const import DOMAIN
from .duux_api import DuuxAPI

class DuuxConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Duux."""
    
    VERSION = 1
    
    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        
        if user_input is not None:
            # Test the credentials
            api = DuuxAPI(
                email=user_input[CONF_EMAIL],
                password=user_input[CONF_PASSWORD]
            )
            
            if await self.hass.async_add_executor_job(api.login):
                # Create entry
                return self.async_create_entry(
                    title=user_input[CONF_EMAIL],
                    data=user_input
                )
            else:
                errors["base"] = "invalid_auth"
        
        data_schema = vol.Schema({
            vol.Required(CONF_EMAIL): str,
            vol.Required(CONF_PASSWORD): str,
        })
        
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
