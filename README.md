# Duux Heater Integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/ssmale/Duux-Home-Assistant.svg)](https://github.com/ssmale/Duux-Home-Assistant/releases)
[![License](https://img.shields.io/github/license/ssmale/Duux-Home-Assistant.svg)](LICENSE)

A Home Assistant integration for Duux Edge heaters, allowing you to control your heater directly from Home Assistant.

## Features

- 🌡️ **Temperature Control**: Set target temperature (5-36°C)
- 🔥 **Three Heating Modes**: Low, Boost, and High
- 🌙 **Night Mode**: Dim the display
- 🔒 **Child Lock**: Prevent accidental changes
- 📊 **Real-time Status**: Current temperature and heating state
- 🔄 **Auto-discovery**: Automatically finds all your Duux devices

## Supported Devices

- Duux Edge Heater (v2)
- Other Duux smart heaters using the Duux app

## Installation

### HACS (Recommended)

1. Open HACS in Home Assistant
2. Click on "Integrations"
3. Click the three dots in the top right corner
4. Select "Custom repositories"
5. Add this repository URL: `https://github.com/ssmale/Duux-Home-Assistant`
6. Select category: "Integration"
7. Click "Add"
8. Find "Duux Heater" in the integration list and click "Download"
9. Restart Home Assistant

### Manual Installation

1. Copy the `custom_components/duux` folder to your Home Assistant's `custom_components` directory
2. Restart Home Assistant
3. Add the integration via the UI

## Configuration

1. Go to **Settings → Devices & Services**
2. Click **+ Add Integration**
3. Search for "Duux Heater"
4. Enter your credentials:
   - **Email**: Your Duux account email
   - **Password**: Your Duux account password

**Note**: If you only use the mobile app with OTP login, you'll need to set a password first:
1. Go to `https://app.cloudgarden.nl`
2. Click "Forgot Password"
3. Enter your email and set a new password

## Usage

### Climate Entity

The integration creates a climate entity for each heater:

```yaml
climate.office_heater
```

**Attributes:**
- `current_temperature`: Current room temperature
- `temperature`: Target temperature
- `hvac_mode`: `heat` or `off`
- `preset_mode`: `low`, `boost`, or `high`

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
          preset_mode: "low"
      - service: climate.set_temperature
        target:
          entity_id: climate.office_heater
        data:
          temperature: 18
```

**Temperature-Based Control:**
```yaml
automation:
  - alias: "Auto Heat Control"
    trigger:
      platform: numeric_state
      entity_id: climate.office_heater
      attribute: current_temperature
      below: 19
    action:
      - service: climate.set_temperature
        target:
          entity_id: climate.office_heater
        data:
          temperature: 21
```

### Lovelace Card Example

```yaml
type: thermostat
entity: climate.office_heater
name: Office Heater
```

Or use a more detailed card:

```yaml
type: vertical-stack
cards:
  - type: thermostat
    entity: climate.office_heater
  - type: entities
    entities:
      - entity: climate.office_heater
        attribute: current_temperature
        name: Current Temperature
      - entity: climate.office_heater
        attribute: preset_mode
        name: Heating Mode
```

## Services

All standard Home Assistant climate services are supported:

- `climate.turn_on`
- `climate.turn_off`
- `climate.set_temperature`
- `climate.set_hvac_mode`
- `climate.set_preset_mode`

## Troubleshooting

### Authentication Issues

If you can't log in:
1. Verify your credentials at `https://app.cloudgarden.nl`
2. Make sure you've set a password (not just using OTP)
3. Check Home Assistant logs for detailed error messages

### Device Not Found

If your heater doesn't appear:
1. Ensure the heater is connected to the Duux app
2. Check that the heater is online in the Duux app
3. Try removing and re-adding the integration
4. Check the logs: Settings → System → Logs

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

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This is an unofficial integration and is not affiliated with or endorsed by Duux. Use at your own risk.