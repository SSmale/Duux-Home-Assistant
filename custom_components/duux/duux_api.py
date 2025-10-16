# custom_components/duux/duux_api.py

import requests
import logging

from .const import API_BASE_URL, API_LOGIN, API_SENSORS, API_COMMANDS

_LOGGER = logging.getLogger(__name__)


class DuuxAPI:
    """Class to communicate with Duux API."""
    
    def __init__(self, email, password):
        """Initialize the API."""
        self.email = email
        self.password = password
        self.token = None
        self.session = requests.Session()
    
    def login(self):
        """Login to Duux API."""
        try:
            response = self.session.post(
                f"{API_BASE_URL}{API_LOGIN}",
                json={
                    "email": self.email,
                    "password": self.password
                }
            )
            response.raise_for_status()
            data = response.json()
            _LOGGER.debug(f"Login response: {data}")
            self.token = data.get("token")
            if self.token:
                self.session.headers.update({
                    "Authorization": f"Bearer {self.token}"
                })
                _LOGGER.info("Successfully logged in to Duux API")
                return True
            
            _LOGGER.error("No token received from Duux API")
            return False
            
        except Exception as e:
            _LOGGER.error(f"Login failed: {e}")
            return False
    
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