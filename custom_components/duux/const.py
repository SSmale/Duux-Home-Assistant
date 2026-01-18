# custom_components/duux/const.py
"""Constants for the Duux integration."""

from homeassistant.components.climate.const import (
    PRESET_BOOST,
    PRESET_COMFORT,
    PRESET_ECO,
)

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
DUUX_STID_EDGEHEATER_2023_V1 = 51
DUUX_STID_BORA_2024 = 62

# Device Type IDs

DUUX_DTID_THERMOSTAT = [50]
DUUX_DTID_HEATER = [51]
DUUX_DTID_HUMIDIFIER = [56]

DUUX_DTID_OTHER_HEATER = [52, 21, 23]


# {
#     "data": [
#         {
#             "typeName": "DUUX Threesixty 2023",
#             "typeId": 49,
#             "typeNumber": 50,
#         },
#         {
#             "typeName": "DUUX Edge heater 2023",
#             "typeId": 51,
#             "typeNumber": 52,
#         },
#         {
#             "typeName": "DUUX Threesixty 2",
#             "typeId": 31,
#             "typeNumber": 21,
#         },
#         {
#             "typeName": "DUUX Edge heater",
#             "typeId": 33,
#             "typeNumber": 23,
#         },
#         {
#             "typeName": "DUUX Edge heater v2",
#             "typeId": 50,
#             "typeNumber": 51,
#         },
#     ],
# }


# Mode mapping options
CONF_MODE_MAPPING = "mode_mapping"

# Default mode mappings (mode index -> preset name)
DEFAULT_MODE_MAPPING = {0: "low", 1: "high", 2: "boost"}

AVAILABLE_PRESETS = [None, PRESET_ECO, PRESET_COMFORT, PRESET_BOOST]
