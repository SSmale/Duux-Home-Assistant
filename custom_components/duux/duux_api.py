# custom_components/duux/duux_api.py

import logging

import requests

from .const import API_BASE_URL, API_COMMANDS, API_LOGIN, API_SENSORS

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
                json={"username": self.email, "password": self.password},
            )
            response.raise_for_status()
            data = response.json()
            self.token = data.get("token")
        except Exception as e:
            _LOGGER.error("Login failed: %s", e)
            return False
        else:
            if self.token:
                self.session.headers.update({"Authorization": f"{self.token}"})
                _LOGGER.info("Successfully logged in to Duux API")
                return True
            _LOGGER.error("No token received from Duux API")
            return False

    def get_devices(self):
        """Get all Duux devices."""
        try:
            response = self.session.get(f"{API_BASE_URL}{API_SENSORS}")
            response.raise_for_status()
            devices = response.json().get("data")
        except Exception as e:
            # todo: refresh the login session and try again.
            _LOGGER.error("Failed to get devices: %s", e)
            return []
        else:
            _LOGGER.debug("Found %s Duux device(s)", len(devices))
            return devices

    def get_device_status(self, device_id):
        """Get status of a specific device."""
        devices = self.get_devices()
        for device in devices:
            if device.get("deviceId") == device_id:
                connection_type = device.get("connectionType")
                latest_data = device.get("latestData")
                if latest_data is None:
                    return {
                        "online": device.get("online", True),
                        "connectionType": connection_type,
                    }

                data = latest_data.get("fullData")
                if data is None:
                    return {
                        "online": device.get("online", True),
                        "connectionType": connection_type,
                    }

                data_copy = data.copy()
                data_copy["online"] = device.get("online", True)
                data_copy["connectionType"] = connection_type
                return data_copy
        return {}

    def send_command(self, device_mac, command):
        """Send command to device."""
        try:
            url = f"{API_BASE_URL}{API_COMMANDS}".replace("{deviceMac}", device_mac)
            response = self.session.post(url, json={"command": command})
            response.raise_for_status()
        except Exception as e:
            _LOGGER.error("Failed to send command: %s", e)
            return False
        else:
            _LOGGER.info("Command sent: %s", command)
            return True

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

    def set_fan_speed(self, device_mac, speed):
        """Set fan speed (1-30)."""
        return self.set_speed(device_mac, speed, 1, 30)

    def set_purifier_speed(self, device_mac, speed):
        """Set purifier speed (0=Auto, 1-4=Speed)."""
        return self.set_speed(device_mac, speed, 0, 4)

    def set_speed(self, device_mac, speed, min_speed, max_speed):
        """Set device speed, clamped to [min_speed, max_speed]."""
        speed = max(min_speed, min(max_speed, int(speed)))
        return self.send_command(device_mac, f"tune set speed {speed}")

    def set_humidity(self, device_mac, humidity):
        """Set target humidity (30-80%)."""
        humidity = max(30, min(80, int(humidity)))
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

    def set_ionizer(self, device_mac, ion_on):
        """Set ionizer on or off."""
        value = "1" if ion_on else "0"
        return self.send_command(device_mac, f"tune set ion {value}")

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

    def set_timer(self, device_mac, hours):
        """Set timer in hours."""
        value = max(0, min(24, int(hours)))
        return self.send_command(device_mac, f"tune set timer {value}")

    def set_humidifier_mode(self, device_mac, mode):
        """Set humidifier mode (0=Normal, 1=Auto)."""
        mode_val = max(0, min(1, int(mode)))
        return self.send_command(device_mac, f"tune set mode {mode_val}")

    def set_horosc_angle(self, device_mac, value):
        """Set horizontal oscillation (0=off, 1=30°, 2=60°, 3=90°)."""
        value = max(0, min(3, int(value)))
        return self.send_command(device_mac, f"tune set horosc {value}")

    def set_horosc_bool(self, device_mac, value):
        """Set horizontal oscillation (0=off, 1=on)."""
        value = max(0, min(1, int(value)))
        return self.send_command(device_mac, f"tune set horosc {value}")

    def set_verosc(self, device_mac, value):
        """Set vertical oscillation (0=off, 1=45°, 2=100°)."""
        value = max(0, min(2, int(value)))
        return self.send_command(device_mac, f"tune set verosc {value}")

    def set_swing(self, device_mac, value):
        """Set swing level (0=off, 1=30°, 2=60°, 3=90°)."""
        value = max(0, min(3, int(value)))
        return self.send_command(device_mac, f"tune set swing {value}")

    def set_tilt(self, device_mac, value):
        """Set vertical tilt (0=off, 1=45°, 2=100°)."""
        value = max(0, min(2, int(value)))
        return self.send_command(device_mac, f"tune set tilt {value}")
