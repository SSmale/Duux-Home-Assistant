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
