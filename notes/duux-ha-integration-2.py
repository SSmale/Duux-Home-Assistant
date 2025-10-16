"""
Duux Heater Integration for Home Assistant with Passwordless Auth
Based on reverse engineering by Simon Smale
"""
# custom_components/duux/__init__.py

import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN
from .duux_api import DuuxAPI

_LOGGER = logging.getLogger(__name__)

PLATFORMS = [Platform.CLIMATE]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duux from a config entry."""
    api = DuuxAPI(email=entry.data["email"])
    
    # Authenticate using passwordless flow
    if not await hass.async_add_executor_job(api.login_passwordless):
        _LOGGER.error("Failed to authenticate with Duux API")
        return False
    
    # Get devices
    devices = await hass.async_add_executor_job(api.get_devices)
    if not devices:
        _LOGGER.error("No Duux devices found")
        return False
    
    # Create coordinator for each device
    coordinators = {}
    for device in devices:
        coordinator = DuuxDataUpdateCoordinator(
            hass,
            api=api,
            device_id=device["deviceId"],
            device_name=device.get("displayName", "Duux Heater")
        )
        
        await coordinator.async_config_entry_first_refresh()
        coordinators[device["deviceId"]] = coordinator
    
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "coordinators": coordinators,
        "devices": devices
    }
    
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    
    return unload_ok


class DuuxDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Duux data."""
    
    def __init__(self, hass, api, device_id, device_name):
        """Initialize."""
        self.api = api
        self.device_id = device_id
        self.device_name = device_name
        
        super().__init__(
            hass,
            _LOGGER,
            name=f"Duux {device_name}",
            update_interval=timedelta(seconds=30),
        )
    
    async def _async_update_data(self):
        """Fetch data from API."""
        try:
            data = await self.hass.async_add_executor_job(
                self.api.get_device_status, self.device_id
            )
            return data
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")


# custom_components/duux/const.py

DOMAIN = "duux"
CONF_EMAIL = "email"
CONF_STATE_KEY = "state_key"  # For storing OTP code temporarily

# API URLs
API_BASE_URL = "https://v5.api.cloudgarden.nl"
API_PASSWORDLESS_CODE = "/auth/passwordlessLogin/code"
API_TOKEN = "/auth/token"
API_SENSORS = "/smarthome/sensors"
API_COMMANDS = "/sensor/{deviceMac}/commands"


# custom_components/duux/duux_api.py

import requests
import logging
import time
import hashlib
import secrets

from .const import (
    API_BASE_URL, 
    API_PASSWORDLESS_CODE, 
    API_TOKEN,
    API_SENSORS, 
    API_COMMANDS
)

_LOGGER = logging.getLogger(__name__)


class DuuxAPI:
    """Class to communicate with Duux API using passwordless auth."""
    
    def __init__(self, email):
        """Initialize the API."""
        self.email = email
        self.token = None
        self.session = requests.Session()
        self.state_key = None
        self.code_verifier = None
    
    def _generate_code_verifier(self):
        """Generate a code verifier for PKCE."""
        # Generate random 43-128 character string
        return secrets.token_urlsafe(96)[:128]
    
    def _generate_code_challenge(self, verifier):
        """Generate code challenge from verifier."""
        # SHA256 hash of verifier, base64url encoded
        digest = hashlib.sha256(verifier.encode('utf-8')).digest()
        import base64
        return base64.urlsafe_b64encode(digest).decode('utf-8').rstrip('=')
    
    def request_login_code(self):
        """Request a passwordless login code to be sent to email."""
        try:
            # Generate PKCE parameters
            self.code_verifier = self._generate_code_verifier()
            code_challenge = self._generate_code_challenge(self.code_verifier)
            
            # Generate state key for this request
            self.state_key = secrets.token_urlsafe(32)
            
            response = self.session.post(
                f"{API_BASE_URL}{API_PASSWORDLESS_CODE}",
                json={
                    "email": self.email,
                    "codeChallenge": code_challenge,
                    "codeChallengeMethod": "S256",
                    "state": self.state_key
                }
            )
            response.raise_for_status()
            
            _LOGGER.info(f"Login code sent to {self.email}")
            return True
            
        except Exception as e:
            _LOGGER.error(f"Failed to request login code: {e}")
            return False
    
    def verify_code(self, code):
        """Verify the passwordless login code and get token."""
        try:
            response = self.session.post(
                f"{API_BASE_URL}{API_TOKEN}",
                json={
                    "email": self.email,
                    "code": code,
                    "codeVerifier": self.code_verifier,
                    "state": self.state_key
                }
            )
            response.raise_for_status()
            data = response.json()
            
            self.token = data.get("token") or data.get("access_token")
            if self.token:
                self.session.headers.update({
                    "Authorization": f"Bearer {self.token}"
                })
                _LOGGER.info("Successfully authenticated with Duux API")
                return True
            
            _LOGGER.error("No token received from Duux API")
            return False
            
        except Exception as e:
            _LOGGER.error(f"Failed to verify code: {e}")
            return False
    
    def login_passwordless(self):
        """
        Full passwordless login flow.
        This is a synchronous method that will wait for user input.
        In production, this should be split into async steps.
        """
        if not self.request_login_code():
            return False
        
        # In Home Assistant integration, we'll handle this via config flow
        # For now, this is a placeholder
        _LOGGER.info("Waiting for code verification via config flow...")
        return True
    
    def get_devices(self):
        """Get all Duux devices."""
        try:
            response = self.session.get(f"{API_BASE_URL}{API_SENSORS}")
            response.raise_for_status()
            devices = response.json()
            _LOGGER.info(f"Found {len(devices)} Duux device(s)")
            return devices
        except Exception as e:
            _LOGGER.error(f"Failed to get devices: {e}")
            return []
    
    def get_device_status(self, device_id):
        """Get status of a specific device."""
        devices = self.get_devices()
        for device in devices:
            if device.get("deviceId") == device_id:
                return device.get("latestData", {}).get("fullData", {})
        return {}
    
    def send_command(self, device_mac, command):
        """Send command to device."""
        try:
            url = f"{API_BASE_URL}{API_COMMANDS}".replace("{deviceMac}", device_mac)
            response = self.session.post(
                url,
                json={"command": command}
            )
            response.raise_for_status()
            _LOGGER.info(f"Command sent: {command}")
            return True
        except Exception as e:
            _LOGGER.error(f"Failed to send command: {e}")
            return False
    
    def set_power(self, device_mac, power_on):
        """Turn device on or off."""
        value = "01" if power_on else "00"
        return self.send_command(device_mac, f"tune set power {value}")
    
    def set_temperature(self, device_mac, temperature):
        """Set target temperature (5-36°C)."""
        temp = max(5, min(36, int(temperature)))
        return self.send_command(device_mac, f"tune set sp {temp}")
    
    def set_mode(self, device_mac, mode):
        """Set heater mode (0=Low, 1=Boost, 2=High)."""
        mode_val = max(0, min(2, int(mode)))
        return self.send_command(device_mac, f"tune set heating {mode_val}")
    
    def set_night_mode(self, device_mac, night_on):
        """Set night mode."""
        value = "01" if night_on else "00"
        return self.send_command(device_mac, f"tune set night {value}")
    
    def set_lock(self, device_mac, locked):
        """Set child lock."""
        value = 1 if locked else 0
        return self.send_command(device_mac, f"tune set lock {value}")


# custom_components/duux/climate.py

from homeassistant.components.climate import (
    ClimateEntity,
    ClimateEntityFeature,
    HVACMode,
)
from homeassistant.const import ATTR_TEMPERATURE, UnitOfTemperature
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN

PRESET_LOW = "low"
PRESET_BOOST = "boost"
PRESET_HIGH = "high"

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duux climate entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinators = data["coordinators"]
    devices = data["devices"]
    
    entities = []
    for device in devices:
        device_id = device["deviceId"]
        coordinator = coordinators[device_id]
        entities.append(DuuxClimate(coordinator, api, device))
    
    async_add_entities(entities)


class DuuxClimate(CoordinatorEntity, ClimateEntity):
    """Representation of a Duux Heater."""
    
    _attr_temperature_unit = UnitOfTemperature.CELSIUS
    _attr_hvac_modes = [HVACMode.HEAT, HVACMode.OFF]
    _attr_preset_modes = [PRESET_LOW, PRESET_BOOST, PRESET_HIGH]
    _attr_supported_features = (
        ClimateEntityFeature.TARGET_TEMPERATURE
        | ClimateEntityFeature.PRESET_MODE
        | ClimateEntityFeature.TURN_OFF
        | ClimateEntityFeature.TURN_ON
    )
    _attr_min_temp = 5
    _attr_max_temp = 36
    _attr_target_temperature_step = 1
    
    def __init__(self, coordinator, api, device):
        """Initialize the climate entity."""
        super().__init__(coordinator)
        self._api = api
        self._device = device
        self._device_id = device["deviceId"]
        self._device_mac = device["deviceId"]
        
        self._attr_unique_id = f"duux_{self._device_id}"
        self._attr_name = device.get("displayName", "Duux Heater")
        self._attr_device_info = {
            "identifiers": {(DOMAIN, self._device_id)},
            "name": self._attr_name,
            "manufacturer": device.get("manufacturer", "Duux"),
            "model": device.get("sensorType", {}).get("name", "Edge Heater"),
        }
    
    @property
    def current_temperature(self):
        """Return the current temperature."""
        return self.coordinator.data.get("temp")
    
    @property
    def target_temperature(self):
        """Return the temperature we try to reach."""
        return self.coordinator.data.get("sp")
    
    @property
    def hvac_mode(self):
        """Return current operation."""
        power = self.coordinator.data.get("power", 0)
        return HVACMode.HEAT if power == 1 else HVACMode.OFF
    
    @property
    def preset_mode(self):
        """Return the current preset mode."""
        mode = self.coordinator.data.get("mode", 0)
        if mode == 0:
            return PRESET_LOW
        elif mode == 1:
            return PRESET_BOOST
        else:
            return PRESET_HIGH
    
    async def async_set_hvac_mode(self, hvac_mode):
        """Set new target hvac mode."""
        if hvac_mode == HVACMode.HEAT:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, True
            )
        else:
            await self.hass.async_add_executor_job(
                self._api.set_power, self._device_mac, False
            )
        await self.coordinator.async_request_refresh()
    
    async def async_set_temperature(self, **kwargs):
        """Set new target temperature."""
        temperature = kwargs.get(ATTR_TEMPERATURE)
        if temperature is not None:
            await self.hass.async_add_executor_job(
                self._api.set_temperature, self._device_mac, temperature
            )
            await self.coordinator.async_request_refresh()
    
    async def async_set_preset_mode(self, preset_mode):
        """Set new preset mode."""
        mode_map = {
            PRESET_LOW: 0,
            PRESET_BOOST: 1,
            PRESET_HIGH: 2,
        }
        mode = mode_map.get(preset_mode, 0)
        await self.hass.async_add_executor_job(
            self._api.set_mode, self._device_mac, mode
        )
        await self.coordinator.async_request_refresh()


# custom_components/duux/config_flow.py

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_EMAIL
from homeassistant.core import callback

from .const import DOMAIN, CONF_STATE_KEY
from .duux_api import DuuxAPI

class DuuxConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Duux with passwordless authentication."""
    
    VERSION = 1
    
    def __init__(self):
        """Initialize the config flow."""
        self._api = None
        self._email = None
    
    async def async_step_user(self, user_input=None):
        """Handle the initial step - request email."""
        errors = {}
        
        if user_input is not None:
            self._email = user_input[CONF_EMAIL]
            self._api = DuuxAPI(email=self._email)
            
            # Request login code
            if await self.hass.async_add_executor_job(self._api.request_login_code):
                # Move to code verification step
                return await self.async_step_verify_code()
            else:
                errors["base"] = "cannot_connect"
        
        data_schema = vol.Schema({
            vol.Required(CONF_EMAIL): str,
        })
        
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
            description_placeholders={
                "info": "You will receive a code via email to complete the login."
            }
        )
    
    async def async_step_verify_code(self, user_input=None):
        """Handle the code verification step."""
        errors = {}
        
        if user_input is not None:
            code = user_input.get("code")
            
            # Verify the code
            if await self.hass.async_add_executor_job(self._api.verify_code, code):
                # Successfully authenticated, create entry
                return self.async_create_entry(
                    title=self._email,
                    data={
                        CONF_EMAIL: self._email,
                    }
                )
            else:
                errors["base"] = "invalid_code"
        
        data_schema = vol.Schema({
            vol.Required("code"): str,
        })
        
        return self.async_show_form(
            step_id="verify_code",
            data_schema=data_schema,
            errors=errors,
            description_placeholders={
                "email": self._email,
                "info": f"Enter the code sent to {self._email}"
            }
        )
    
    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return DuuxOptionsFlowHandler(config_entry)


class DuuxOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle Duux options."""
    
    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry
    
    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                # Add any options here in the future
            })
        )


# custom_components/duux/manifest.json

{
  "domain": "duux",
  "name": "Duux Heater",
  "codeowners": ["@yourusername"],
  "config_flow": true,
  "dependencies": [],
  "documentation": "https://github.com/yourusername/duux-homeassistant",
  "iot_class": "cloud_polling",
  "requirements": ["requests>=2.31.0"],
  "version": "2.0.0"
}