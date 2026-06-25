# Duux Integration for Home Assistant

Control your Duux devices directly from Home Assistant!

## Supported Devices

### 🌡️ Heaters

- **Edge Heater 2000** — Temperature control, Low/High modes, Night mode, Child lock
- **Edge Heater 2023 (v1)** — Temperature control, Low/High modes, Night mode, Child lock
- **Edge Heater (v2)** — Temperature control, Low/High/Boost modes, Night mode, Child lock, Timer
- **Threesixty 2** — Temperature control, Eco/Comfort/Boost modes
- **Threesixty 2023** — Temperature control, Eco/Comfort/Boost modes

### 💨 Fans

- **Whisper Flex Ultimate** — 30-speed fan, Normal/Natural/Night modes
- **Whisper Flex** — 25-speed fan, Normal/Natural/Night modes
- **Whisper Flex 2** — 29-speed fan, Normal/Natural modes

### ❄️ Air Conditioners

- **North** — Temperature control, Cool/Dry/Fan-only modes, 3-speed fan, Louver swing, Night mode, Timer

### 🌿 Air Purifiers

- **Bright 2** — 4-speed fan + Auto mode, PM2.5/TVOC/AQ sensors, HEPA filter life, Timer, Night mode, Ionizer

### 💧 Dehumidifiers & Humidifiers

- **Bora 2024** — Humidity control, Auto/Continuous modes, Fan speed, Laundry/Cleaning/Sleep modes, Timer
- **Beam Mini** — Humidity control, Auto/Manual modes, Humidity & temperature sensors, Timer
- **Neo** — Humidity control, Normal/Auto modes, Spray volume selector

Every device also includes a **connectivity sensor** and a **problem/error sensor**.

## Quick Start

1. Install via HACS
2. Restart Home Assistant
3. Go to **Settings → Devices & Services → Add Integration**
4. Search for **Duux** and enter your credentials

## Need a Password?

If you only use the mobile app with OTP login:

1. Visit `https://app.cloudgarden.nl`
2. Click "Forgot Password"
3. Set a password for your account

## My Device Isn't Listed?

The integration will attempt auto-discovery for unknown Duux devices and log the device details. Please open a [GitHub issue](https://github.com/SSmale/Duux-Home-Assistant/issues/new?template=device_not_supported.yaml) with those details so it can be added.

[Full Documentation](https://github.com/ssmale/Duux-Home-Assistant)