# Duux Integration for Home Assistant

A Home Assistant integration for Duux products, allowing you to control your devices directly from Home Assistant.

[![Home Assistant](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=duux)

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)
![Install count](https://img.shields.io/badge/dynamic/json?color=41BDF5&logo=home-assistant&label=integration%20usage&suffix=%20installs&cacheSeconds=15600&url=https://analytics.home-assistant.io/custom_integrations.json&query=$.duux.total)
[![GitHub release](https://img.shields.io/github/release/ssmale/Duux-Home-Assistant.svg)](https://github.com/ssmale/Duux-Home-Assistant/releases)
[![License](https://img.shields.io/github/license/ssmale/Duux-Home-Assistant.svg)](LICENSE)
[![codecov](https://codecov.io/github/SSmale/Duux-Home-Assistant/graph/badge.svg?token=UPWPNCH49V)](https://codecov.io/github/SSmale/Duux-Home-Assistant)

## Features

- 📊 **Real-time Status**: Current temperature, humidity, and device state
- 🔄 **Auto-discovery**: Automatically finds all your Duux devices
- 🌐 **Offline Detection**: All entities are marked unavailable when a device is disconnected from the cloud

## Supported Devices

### 🌡️ Heaters

#### Duux Edge Heater 2000

- 🌡️ **Temperature Control**: Set target temperature (5–36°C)
- 🔥 **Two Heating Modes**: Low and High
- 🌙 **Night Mode**: Dim the display
- 🔒 **Child Lock**: Prevent accidental changes

#### Duux Edge Heater 2023 (v1)

- 🌡️ **Temperature Control**: Set target temperature (5–36°C)
- 🔥 **Two Heating Modes**: Low and High
- 🌙 **Night Mode**: Dim the display
- 🔒 **Child Lock**: Prevent accidental changes

#### Duux Edge Heater (v2)

- 🌡️ **Temperature Control**: Set target temperature (5–36°C)
- 🔥 **Three Heating Modes**: Low, High and Boost
- 🌙 **Night Mode**: Dim the display
- 🔒 **Child Lock**: Prevent accidental changes
- ⏲️ **Timer**: Set a shutdown timer (0–24 hours)

#### Duux Threesixty 2

- 🌡️ **Temperature Control**: Set target temperature (18–30°C)
- 🔥 **Three Heating Modes**: Eco, Comfort and Boost

#### Duux Threesixty 2023

- 🌡️ **Temperature Control**: Set target temperature (18–30°C)
- 🔥 **Three Heating Modes**: Eco, Comfort and Boost

---

### 💨 Fans

#### Duux Whisper Flex Ultimate

- ⚡ **Power**: On/Off control
- 💨 **30-Speed Fan**: Fine-grained speed control (1–30)
- 🌀 **Three Modes**: Normal, Natural and Night

#### Duux Whisper Flex

- ⚡ **Power**: On/Off control
- 💨 **25-Speed Fan**: Fine-grained speed control (1–25)
- 🌀 **Three Modes**: Normal, Natural and Night

#### Duux Whisper Flex 2

- ⚡ **Power**: On/Off control
- 💨 **30-Speed Fan**: Fine-grained speed control (1–30)
- 🌀 **Two Modes**: Normal and Natural

---

### 🌿 Air Purifiers

#### Duux Bright 2

- ⚡ **Power**: On/Off control
- 💨 **Fan Control**: 4 manual speeds + Auto mode
- 🌿 **Auto Speed**: Automatically adjusts based on air quality (AQ) and TVOC levels
- 🔬 **PM2.5 Sensor**: Real-time particulate matter monitoring
- 🧪 **TVOC Sensor**: Volatile organic compound level (Healthy / Acceptable / Polluted / Harmful)
- 🌬️ **Air Quality Index**: 6-level indicator (Excellent → Harmful)
- 🔋 **HEPA Filter Life**: Remaining filter lifespan (%)
- ⏲️ **Timer**: Preset durations (0, 1, 2, 4, 8 hours) with time-remaining sensor
- 🌙 **Night Mode**: Reduced noise and display dimming
- ⚡ **Ionizer**: On/off control (automatically disabled at minimum speed)

---

### 💧 Dehumidifiers & Humidifiers

#### Duux Bora Dehumidifier (2024)

- 💧 **Humidity Control**: Set target humidity (30–80%)
- ✌️ **Two Drying Modes**: Auto or Continuous
- 🍃 **Two Fan Speeds**: Low or High
- 👕 **Laundry Mode**: Start a laundry drying cycle
- 🧹 **Cleaning Mode**: Start a self-cleaning cycle
- 🌙 **Sleep Mode**: Dim the lights and silence the beep
- 💧 **Humidity Sensor**: Track current humidity levels
- ⏲️ **Timer**: Set a shutdown timer (0–24 hours) with time-remaining sensor

#### Duux Beam Mini Humidifier

- 💧 **Humidity Control**: Set target humidity (20–80%)
- 🌡️ **Temperature Sensor**: Real-time ambient temperature
- 💧 **Humidity Sensor**: Track current humidity levels
- 🔄 **Two Modes**: Auto and Manual
- ⏲️ **Timer**: Set a shutdown timer (0–24 hours)

#### Duux Neo Humidifier

- 💧 **Humidity Control**: Set target humidity (30–80%)
- 🔄 **Two Modes**: Normal and Auto
- 💧 **Humidity Sensor**: Track current humidity levels
- 🌬️ **Spray Volume**: Low, Mid or High selector

---

### ⚠️ All Devices

Every supported device also gets:

- 🔴 **Problem Sensor**: Fires when the device reports an error code (ice detected, water tank full, etc.)
- 🟢 **Connectivity Sensor**: Shows whether the device is online or offline, with last-seen timestamp
- 📡 **Connection Type Sensor**: Reports whether the device is connected via MQTT or TCP

---

## Support the Development

[![GitHub Sponsor Badge](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/ssmale)

## Installation

### HACS (Recommended)

1. Open HACS in Home Assistant
2. Click on "Integrations"
3. Find "Duux" in the integration list and click "Download"
4. Restart Home Assistant

### Manual Installation

1. Copy the `custom_components/duux` folder to your Home Assistant's `custom_components` directory
2. Restart Home Assistant
3. Add the integration via the UI

## Configuration

1. Go to **Settings → Devices & Services**
2. Click **+ Add Integration**
3. Search for "Duux"
4. Enter your credentials:
   - **Email**: Your Duux account email
   - **Password**: Your Duux account password

**Note**: If you only use the mobile app with OTP login, you'll need to set a password first:

1. Go to `https://app.cloudgarden.nl`
2. Click "Forgot Password"
3. Enter your email and set a new password

## Usage

### Climate Entity (Heaters)

The integration creates a climate entity for each heater:

```yaml
climate.office_heater
```

**Attributes:**

- `current_temperature`: Current room temperature
- `temperature`: Target temperature
- `hvac_mode`: `heat` or `off`
- `preset_mode`: `eco`, `comfort`, or `boost` (varies by model)

### Fan Entity

The integration creates a fan entity for each fan:

```yaml
fan.living_room_fan
```

**Attributes:**

- `percentage`: Current speed as a percentage
- `preset_mode`: `normal`, `natural`, or `night`
- `speed_count`: Total number of speed steps

### Humidifier Entity

```yaml
humidifier.bedroom_humidifier
```

**Attributes:**

- `current_humidity`: Current room humidity
- `humidity`: Target humidity
- `mode`: `auto`, `normal`, or `boost` (varies by model)

### Example Automations

**Morning Warmup:**

```yaml
automation:
  - alias: "Morning Heat Boost"
    trigger:
      platform: time
      at: "06:30:00"
    action:
      - service: climate.turn_on
        target:
          entity_id: climate.office_heater
      - service: climate.set_temperature
        target:
          entity_id: climate.office_heater
        data:
          temperature: 22
      - service: climate.set_preset_mode
        target:
          entity_id: climate.office_heater
        data:
          preset_mode: "boost"
```

**Energy Saving at Night:**

```yaml
automation:
  - alias: "Night Mode Energy Saving"
    trigger:
      platform: time
      at: "22:00:00"
    action:
      - service: climate.set_preset_mode
        target:
          entity_id: climate.office_heater
        data:
          preset_mode: "eco"
      - service: climate.set_temperature
        target:
          entity_id: climate.office_heater
        data:
          temperature: 18
```

**Fan Night Mode:**

```yaml
automation:
  - alias: "Fan Night Mode at Bedtime"
    trigger:
      platform: time
      at: "22:30:00"
    action:
      - service: fan.set_preset_mode
        target:
          entity_id: fan.bedroom_fan
        data:
          preset_mode: "night"
```

**Air Purifier Auto Mode when Air Quality Drops:**

```yaml
automation:
  - alias: "Purifier boost on poor air quality"
    trigger:
      platform: state
      entity_id: sensor.bright_2_air_quality_index
      to: "poor"
    action:
      - service: fan.set_preset_mode
        target:
          entity_id: fan.bright_2
        data:
          preset_mode: "auto"
```

### Lovelace Card Examples

**Heater:**

```yaml
type: thermostat
entity: climate.office_heater
name: Office Heater
```

**Fan:**

```yaml
type: entities
entities:
  - entity: fan.living_room_fan
  - entity: fan.living_room_fan
    type: attribute
    attribute: percentage
    name: Speed
  - entity: fan.living_room_fan
    type: attribute
    attribute: preset_mode
    name: Mode
```

## Troubleshooting

### Authentication Issues

If you can't log in:

1. Verify your credentials at `https://app.cloudgarden.nl`
2. Make sure you've set a password (not just using OTP)
3. Check Home Assistant logs for detailed error messages

### Device Not Found

If your device doesn't appear:

1. Ensure the device is connected to the Duux app
2. Check that the device is online in the Duux app
3. Try removing and re-adding the integration
4. Check the logs: Settings → System → Logs

### Device Shows as Unavailable

Check the Connectivity sensor for the device — it will show the last time the device was seen online. If the device has been offline for a while, check your Wi-Fi connection and the Duux app.

### My Device Isn't Listed Above

If your Duux device isn't in the supported list but is a fan, heater, or air purifier, the integration will attempt to set it up using auto-discovery and log a warning with the device details. Please open a [GitHub issue](https://github.com/SSmale/Duux-Home-Assistant/issues/new?template=device_not_supported.yaml) with those details so it can be added to the official list.

### Enable Debug Logging

Add this to your `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.duux: debug
```

## Credits

This integration is based on the reverse engineering work by [Simon Smale](https://smale.codes).

Thanks to:

- [Noah Evans](https://github.com/ThisIsNoahEvans/DuuxAPI) for the DuuxAPI reference implementation
- The Home Assistant community

## Translations

A big thank you to @Anokino for the translation work.

Currently the project has translations for:

- English
- French
- German
- Italian
- Dutch
- Spanish
- Greek

If you spot an issue with the translations, or want to create one for another language please open an issue!

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Disclaimer

This is an unofficial integration and is not affiliated with or endorsed by Duux. Use at your own risk.
