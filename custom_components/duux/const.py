# custom_components/duux/const.py
from enum import IntEnum

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
DUUX_DTID_THERMOSTAT = [50, 52]
DUUX_DTID_HEATER = [51, 21]
DUUX_DTID_HUMIDIFIER = [56]

DUUX_DTID_OTHER_HEATER = [23]

DUUX_CLIMATE_TYPES = ["THERMOSTAT", "HEATER"]
DUUX_HUMIDIFIER_TYPES = ["HUMIDIFIER"]

DUUX_SUPPORTED_TYPES = DUUX_CLIMATE_TYPES + DUUX_HUMIDIFIER_TYPES

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
#         {
#             "typeName": "DUUX Bora 2024",
#             "typeId": 62,
#             "typeNumber": 56,
#         },
#     ],
# }

# Error codes
class DUUX_ERRID(IntEnum):
    OK = 0
    Ice_Detected = 4
    Water_Tank_Full = 8
    
    Unknown_Error=9999999
    
    @classmethod
    def _missing_(cls, value):
        return cls.Unknown_Error