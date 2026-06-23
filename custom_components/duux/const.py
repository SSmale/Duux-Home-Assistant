# custom_components/duux/const.py
from enum import Enum

DOMAIN = "duux"
CONF_EMAIL = "email"
CONF_PASSWORD = "password"
ATTRIBUTION = "Data provided by Duux"

# API URLs
API_BASE_URL = "https://v5.api.cloudgarden.nl"
API_LOGIN = "/auth/v4/login"
API_SENSORS = "/smarthome/sensors"
API_COMMANDS = "/sensor/{deviceMac}/commands"

# Sensor Type IDs
DUUX_STID_THREESIXTY_TWO = 31
DUUX_STID_THREESIXTY_2023 = 49
DUUX_STID_EDGEHEATER_V2 = 50
DUUX_STID_EDGEHEATER_2000 = 33
DUUX_STID_EDGEHEATER_2023_V1 = 51
DUUX_STID_BORA_2024 = 62
DUUX_STID_BEAM_MINI = 35
DUUX_STID_WHISPER_FLEX_2 = 67
DUUX_STID_WHISPER_FLEX = 36
DUUX_STID_WHISPER_FLEX_ULTIMATE = 40
DUUX_STID_WHISPER_FLEX_ELIVATE = 70
DUUX_STID_BRIGHT_2 = 61
DUUX_STID_NEO = 47
DUUX_STID_NORTH = 42

# Device Type IDs
DUUX_DTID_THERMOSTAT = [50]
DUUX_DTID_HEATER = [51, 52, 21, 23]
DUUX_DTID_HUMIDIFIER = [56, 25]
DUUX_DTID_FAN = [26, 58, 27, 59]
DUUX_DTID_AIR_PURIFIER = [55, 32]

# North AC reports googleDeviceType: null inconsistently, so it's matched
# directly on device_type_id rather than via the last_word fallback.
DUUX_DTID_AIR_CONDITIONER = [28]

DUUX_DTID_OTHER_HEATER = []

DUUX_CLIMATE_TYPES = ["THERMOSTAT", "HEATER"]
DUUX_HUMIDIFIER_TYPES = ["HUMIDIFIER"]
DUUX_FAN_TYPES = ["FAN", "AIRPURIFIER"]
DUUX_AIR_PURIFIER_TYPES = ["AIRPURIFIER"]

DUUX_SUPPORTED_TYPES = (
    DUUX_CLIMATE_TYPES
    + DUUX_HUMIDIFIER_TYPES
    + DUUX_FAN_TYPES
    + DUUX_AIR_PURIFIER_TYPES
)


_ERRID_UNAVAILABLE = object()

# Error codes
class DUUX_ERRID(Enum):
    Unavailable = _ERRID_UNAVAILABLE
    OK = 0
    Ice_Detected = 4
    Water_Tank_Full = 8
    Unknown_Error = 9999999

    @classmethod
    def _missing_(cls, value):
        if value is None:
            return cls.OK
        return cls.Unknown_Error
