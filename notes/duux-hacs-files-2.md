# README.md

# Duux Heater Integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/yourusername/duux-homeassistant.svg)](https://github.com/yourusername/duux-homeassistant/releases)
[![License](https://img.shields.io/github/license/yourusername/duux-homeassistant.svg)](LICENSE)

A Home Assistant integration for Duux Edge heaters with **passwordless authentication** and automatic token refresh, allowing you to control your heater directly from Home Assistant.

## Features

- 🔐 **Passwordless Login**: Uses one-time codes sent to your email (same as mobile app)
- 🔄 **Automatic Token Refresh**: Keeps you logged in indefinitely
- 🌡️ **Temperature Control**: Set target temperature (5-36°C)
- 🔥 **Three Heating Modes**: Low, Boost, and High
- 🌙 **Night Mode**: Dim the display
- 🔒 **Child Lock**: Prevent accidental changes
- 📊 **Real-time Status**: Current temperature and heating state
- 🔍 **Auto-discovery**: Automatically finds all your Duux devices

## Supported Devices

- Duux Edge Heater (v2)
- Other Duux smart heaters using the Duux app

## Installation

### HACS (Recommended)

1. Open HACS in Home Assistant
2. Click on "Integrations"
3. Click the three dots in the top right corner
4. Select "Custom repositories"
5. Add this repository URL: `https://github.com/yourusername/duux-homeassistant`
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

This integration is based on the reverse engineering work by [Simon Smale](https://simonsmale.com). 

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

---

# hacs.json

{
  "name": "Duux Heater",
  "render_readme": true,
  "domains": ["climate"],
  "iot_class": "cloud_polling",
  "homeassistant": "2023.1.0"
}

---

# .github/workflows/validate.yaml

name: Validate

on:
  push:
  pull_request:
  schedule:
    - cron: "0 0 * * *"

jobs:
  validate:
    runs-on: ubuntu-latest
    name: Validate
    steps:
      - name: Check out repository
        uses: actions/checkout@v3

      - name: HACS validation
        uses: hacs/action@main
        with:
          category: integration

      - name: Hassfest validation
        uses: home-assistant/actions/hassfest@master

---

# .github/workflows/release.yaml

name: Release

on:
  release:
    types: [published]

jobs:
  release:
    name: Prepare release
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Create zip
        run: |
          cd custom_components/duux
          zip -r ../../duux.zip .

      - name: Upload zip to release
        uses: svenstaro/upload-release-action@v2
        with:
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          file: duux.zip
          asset_name: duux.zip
          tag: ${{ github.ref }}

---

# LICENSE

MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

# .gitignore

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# macOS
.DS_Store

---

# info.md

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

[Full Documentation](https://github.com/yourusername/duux-homeassistant)

---

# CONTRIBUTING.md

# Contributing to Duux Heater Integration

Thank you for your interest in contributing!

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/duux-homeassistant.git`
3. Create a branch: `git checkout -b feature/your-feature-name`

## Development Setup

1. Install Home Assistant in development mode
2. Link your custom component:
   ```bash
   ln -s /path/to/duux-homeassistant/custom_components/duux /path/to/homeassistant/config/custom_components/duux
   ```
3. Restart Home Assistant

## Testing

Before submitting a PR:

1. Test the integration with a real Duux heater
2. Verify all heating modes work correctly
3. Check that temperature changes are reflected properly
4. Ensure no errors appear in the logs

## Code Style

- Follow PEP 8
- Use type hints where possible
- Add docstrings to all functions
- Keep functions focused and small

## Pull Request Process

1. Update the README.md with details of changes
2. Update the version number in `manifest.json`
3. Ensure all GitHub Actions pass
4. Request review from maintainers

## Reporting Issues

When reporting issues, please include:

- Home Assistant version
- Integration version
- Heater model
- Full error logs
- Steps to reproduce

## Questions?

Open a discussion on GitHub or create an issue!

---

# CHANGELOG.md

# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-10-15

### Added
- Initial release
- Climate entity support for Duux Edge heaters
- Temperature control (5-36°C)
- Three preset modes (Low, Boost, High)
- Night mode support
- Auto-discovery of devices
- HACS support
- Configuration flow via UI

### Known Issues
- None

## Future Plans

- [ ] Add switch entities for lock and timer
- [ ] Add sensor entities for power consumption
- [ ] Support for Duux fans
- [ ] Local API support (if available)
- [ ] Energy dashboard integration