# Contributing to Duux Heater Integration

Thank you for your interest in contributing!

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/Duux-Home-Assistant.git`
3. Create a branch: `git checkout -b feature/your-feature-name`

## Development Setup

The fastest way to get started is with the provided devcontainer (VS Code Dev Containers or GitHub Codespaces). It installs all dependencies and wires up the pre-commit hooks automatically on container creation.

If you prefer a local setup, run the setup script instead:

```bash
scripts/setup
```

This installs all Python dependencies (including ruff and pre-commit) and registers the git hooks.

## Testing

Before submitting a PR:

1. Test the integration with a real Duux heater
2. Verify all heating modes work correctly
3. Check that temperature changes are reflected properly
4. Ensure no errors appear in the logs

## Code Style

This project uses [ruff](https://docs.astral.sh/ruff/) for linting and formatting. It is configured in `pyproject.toml` and runs automatically as a pre-commit hook on every commit.

To run it manually:

```bash
ruff check --fix .   # lint and auto-fix
ruff format .        # format
```

Beyond what ruff enforces automatically:

- Use type hints where possible
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
