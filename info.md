# Duux Heater Integration

Control your Duux Edge heater directly from Home Assistant!

## Features

- 🌡️ Set target temperature (5-36°C)
- 🔥 Three heating modes (Low, Boost, High)
- 🌙 Night mode support
- 📊 Real-time temperature monitoring
- 🔄 Automatic device discovery

## Quick Start

1. Install via HACS
2. Restart Home Assistant
3. Add integration via UI
4. Enter your Duux credentials

## Need a Password?

If you only use the mobile app:
1. Visit https://app.cloudgarden.nl
2. Click "Forgot Password"
3. Set a password for your account

## Example Automation

```yaml
automation:
  - alias: "Morning Warmup"
    trigger:
      platform: time
      at: "06:30:00"
    action:
      - service: climate.set_temperature
        target:
          entity_id: climate.office_heater
        data:
          temperature: 22
          preset_mode: "boost"
```

[Full Documentation](https://github.com/ssmale/Duux-Home-Assistant)