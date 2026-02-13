# pytest plugin for Home Assistant custom component tests
import os
import sys

# Ensure repo root is on sys.path so `import custom_components...` works
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

pytest_plugins = ["pytest_homeassistant_custom_component"]

import json
import pytest


@pytest.fixture
def fixtures_path():
    """Path to fixtures directory in the repo root."""
    return os.path.join(os.path.dirname(__file__), "..", "fixtures")


@pytest.fixture
def devices_fixture(fixtures_path):
    """Load the fixtures/devices.json payload (list of devices)."""
    path = os.path.join(fixtures_path, "devices.json")
    with open(path, "r", encoding="utf-8") as fh:
        payload = json.load(fh)
    return payload.get("data", [])
