# custom_components/duux/const.py

DOMAIN = "duux"
CONF_EMAIL = "email"
CONF_PASSWORD = "password"

# API URLs
API_BASE_URL = "https://v5.api.cloudgarden.nl"
API_LOGIN = "/auth/v4/login"
API_SENSORS = "/smarthome/sensors"
API_COMMANDS = "/sensor/{deviceMac}/commands"