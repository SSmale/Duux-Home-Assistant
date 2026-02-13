# Tests for Duux Home Assistant integration

This folder contains pytest-based tests for the Duux custom integration. Tests are written following Home Assistant best practices and use the `pytest-homeassistant-custom-component` plugin.

Prerequisites
- Python 3.11 (recommended)
- Git, pip

Setup (local)
1. Create a virtual environment and activate it:
   - python -m venv .venv
   - source .venv/bin/activate

2. Upgrade pip and install test dependencies:
   - pip install -U pip
   - pip install pytest pytest-asyncio pytest-homeassistant-custom-component

Run tests
- From the repository root:
  - pytest tests -q

Notes
- Tests rely on `fixtures/devices.json` for representative device payloads. Make sure that file exists (it was added previously when creating the mock server).
- If you need to run a single test file, use:
  - pytest tests/test_integration_setup.py -q
- The CI workflow runs `pytest tests -q`; results should be similar locally.

Troubleshooting
- If tests cannot import Home Assistant test helpers, ensure `pytest-homeassistant-custom-component` is installed in the same interpreter.