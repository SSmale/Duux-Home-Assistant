# custom_components/duux/config_flow.py

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_EMAIL, CONF_PASSWORD

from .const import DOMAIN
from .duux_api import DuuxAPI


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut: MutantDict = {}  # type: ignore

class DuuxConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Duux."""
    
    VERSION = 1
    
    @_mutmut_mutated(mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut)
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
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_orig(self, user_input=None):
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
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_1(self, user_input=None):
        """Handle the initial step."""
        errors = None
        
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
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_2(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        
        if user_input is None:
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
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_3(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        
        if user_input is not None:
            # Test the credentials
            api = None
            
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
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_4(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        
        if user_input is not None:
            # Test the credentials
            api = DuuxAPI(
                email=None,
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
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_5(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        
        if user_input is not None:
            # Test the credentials
            api = DuuxAPI(
                email=user_input[CONF_EMAIL],
                password=None
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
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_6(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        
        if user_input is not None:
            # Test the credentials
            api = DuuxAPI(
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
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_7(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        
        if user_input is not None:
            # Test the credentials
            api = DuuxAPI(
                email=user_input[CONF_EMAIL],
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
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_8(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        
        if user_input is not None:
            # Test the credentials
            api = DuuxAPI(
                email=user_input[CONF_EMAIL],
                password=user_input[CONF_PASSWORD]
            )
            
            if await self.hass.async_add_executor_job(None):
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
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_9(self, user_input=None):
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
                    title=None,
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
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_10(self, user_input=None):
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
                    data=None
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
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_11(self, user_input=None):
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
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_12(self, user_input=None):
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
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_13(self, user_input=None):
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
                errors["base"] = None
        
        data_schema = vol.Schema({
            vol.Required(CONF_EMAIL): str,
            vol.Required(CONF_PASSWORD): str,
        })
        
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_14(self, user_input=None):
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
                errors["XXbaseXX"] = "invalid_auth"
        
        data_schema = vol.Schema({
            vol.Required(CONF_EMAIL): str,
            vol.Required(CONF_PASSWORD): str,
        })
        
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_15(self, user_input=None):
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
                errors["BASE"] = "invalid_auth"
        
        data_schema = vol.Schema({
            vol.Required(CONF_EMAIL): str,
            vol.Required(CONF_PASSWORD): str,
        })
        
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_16(self, user_input=None):
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
                errors["base"] = "XXinvalid_authXX"
        
        data_schema = vol.Schema({
            vol.Required(CONF_EMAIL): str,
            vol.Required(CONF_PASSWORD): str,
        })
        
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_17(self, user_input=None):
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
                errors["base"] = "INVALID_AUTH"
        
        data_schema = vol.Schema({
            vol.Required(CONF_EMAIL): str,
            vol.Required(CONF_PASSWORD): str,
        })
        
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_18(self, user_input=None):
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
        
        data_schema = None
        
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_19(self, user_input=None):
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
        
        data_schema = vol.Schema(None)
        
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_20(self, user_input=None):
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
            vol.Required(None): str,
            vol.Required(CONF_PASSWORD): str,
        })
        
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_21(self, user_input=None):
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
            vol.Required(None): str,
        })
        
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_22(self, user_input=None):
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
            step_id=None,
            data_schema=data_schema,
            errors=errors
        )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_23(self, user_input=None):
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
            data_schema=None,
            errors=errors
        )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_24(self, user_input=None):
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
            errors=None
        )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_25(self, user_input=None):
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
            data_schema=data_schema,
            errors=errors
        )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_26(self, user_input=None):
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
            errors=errors
        )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_27(self, user_input=None):
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
            )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_28(self, user_input=None):
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
            step_id="XXuserXX",
            data_schema=data_schema,
            errors=errors
        )
    
    async def xǁDuuxConfigFlowǁasync_step_user__mutmut_29(self, user_input=None):
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
            step_id="USER",
            data_schema=data_schema,
            errors=errors
        )

mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['_mutmut_orig'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_1'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_2'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_3'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_4'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_5'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_6'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_7'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_8'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_9'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_10'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_11'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_12'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_13'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_14'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_15'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_16'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_17'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_18'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_19'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_20'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_21'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_22'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_23'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_24'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_25'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_26'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_27'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_28'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDuuxConfigFlowǁasync_step_user__mutmut['xǁDuuxConfigFlowǁasync_step_user__mutmut_29'] = DuuxConfigFlow.xǁDuuxConfigFlowǁasync_step_user__mutmut_29 # type: ignore # mutmut generated
