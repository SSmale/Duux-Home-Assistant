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
                    "username": self.email,
                    "password": self.password
                }
            )
            response.raise_for_status()
            data = response.json()
            self.token = data.get("token")
            if self.token:
                self.session.headers.update({
                    "Authorization": f"{self.token}"
                })
                _LOGGER.warning("Successfully logged in to Duux API")
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
            devices = response.json().get('data')
            _LOGGER.info(f"Found {len(devices)} Duux device(s)")
            return devices
        except Exception as e:
        	# todo: refresh the login session and try again.
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
        # note: Both temperature for heaters and humidity for de-humidifiers
        #       use 'set-point' (aka 'sp') to track a target value.
        return self.send_command(device_mac, f"tune set sp {temp}")
    
    def set_humidity(self, device_mac, humidity):
        """Set target humidity (30-80%)."""
        temp = max(30, min(80, int(humidity)))
        # note: Both temperature for heaters and humidity for de-humidifiers
        #       use 'set-point' (aka 'sp') to track a target value.
        return self.send_command(device_mac, f"tune set sp {humidity}")
    
    def set_mode(self, device_mac, mode):
        """Set heater mode (1=Low, 2=High, 3=Boost)."""
        mode_val = max(1, min(3, int(mode)))
        return self.send_command(device_mac, f"tune set heating {mode_val}")
    
    def set_dry_mode(self, device_mac, mode):
        """Set dryer mode (0=Auto, 1=Continuous)."""
        mode_val = max(0, min(1, int(mode)))
        return self.send_command(device_mac, f"tune set mode {mode_val}")
    
    def set_fan(self, device_mac, mode):
        """Set fan mode (1=Low, 0=High)."""
        mode_val = max(0, min(1, int(mode)))
        return self.send_command(device_mac, f"tune set fan {mode_val}")
    
    def set_night_mode(self, device_mac, night_on):
        """Set night mode."""
        value = "01" if night_on else "00"
        return self.send_command(device_mac, f"tune set night {value}")
    
    def set_sleep_mode(self, device_mac, sleep_on):
        """Set sleep mode."""
        value = "01" if sleep_on else "00"
        return self.send_command(device_mac, f"tune set sleep {value}")
    
    def set_lock(self, device_mac, locked):
        """Set child lock."""
        value = 1 if locked else 0
        return self.send_command(device_mac, f"tune set lock {value}")
    
    def set_cleaning_mode(self, device_mac, cleaning_on):
        """Set self-cleaning mode."""
        value = "01" if cleaning_on else "00"
        return self.send_command(device_mac, f"tune set dry {value}")
    
    def set_laundry_mode(self, device_mac, laundry_on):
        """Set laundry mode."""
        value = "01" if laundry_on else "00"
        return self.send_command(device_mac, f"tune set laundr {value}")
    
    def set_timer_mode(self, device_mac, mode):
        """Set timer mode in hours."""
        mode_val = max(0, min(24, int(hours)))
        return self.send_command(device_mac, f"tune set timer {value}")