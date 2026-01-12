# custom_components/duux/const.py

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
DUUX_DTID_THERMOSTAT = 50
DUUX_DTID_HEATER = 51
DUUX_DTID_HUMIDIFIER = 56