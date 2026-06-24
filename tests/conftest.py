"""Shared fixtures and lightweight test doubles for the Duux integration tests.

These tests intentionally avoid the heavyweight ``pytest-homeassistant-custom-component``
test harness. The integration's entities only ever touch a handful of attributes on
``hass``/``coordinator`` (``.data``, ``.async_add_executor_job``,
``.async_request_refresh`` / ``.async_set_updated_data``, ``.async_add_listener``), so
small explicit fakes exercise the real code paths just as well while staying fast,
dependency-light, and easy to reason about. The only real Home Assistant dependency
is the ``homeassistant`` core package itself (for the actual entity base classes
under test), which is declared in tests/requirements.txt.
"""

import json
import os
import sys
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock

import pytest

# Make `custom_components.duux` importable regardless of where pytest is invoked
# from. pytest.ini's rootdir handles this for the documented `pytest tests -q`
# invocation, but this keeps individual test files runnable directly too.
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)


# ---------------------------------------------------------------------------
# Device fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def _devices_payload():
    """Load fixtures/devices.json once per test session."""
    path = os.path.join(REPO_ROOT, "fixtures", "devices.json")
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


@pytest.fixture
def devices_fixture(_devices_payload):
    """Return a fresh, deep-copied device list so tests can mutate it freely."""
    return json.loads(json.dumps(_devices_payload["data"]))


@pytest.fixture
def device_by_stid(devices_fixture):
    """Factory fixture: device_by_stid(sensor_type_id) -> matching device dict.

    Returns a deep copy of the fixture device, so callers can tweak fields
    (e.g. flip "online") without affecting other tests.
    """

    def _find(sensor_type_id):
        for device in devices_fixture:
            if device["sensorTypeId"] == sensor_type_id:
                return device
        raise LookupError(f"No fixture device with sensorTypeId={sensor_type_id}")

    return _find


# ---------------------------------------------------------------------------
# Coordinator / hass test doubles
# ---------------------------------------------------------------------------


class FakeCoordinator:
    """Minimal stand-in for DataUpdateCoordinator.

    Implements just enough of the real interface (``.data``,
    ``.last_update_success``, ``.async_add_listener()``,
    ``.async_request_refresh()``, ``.async_set_updated_data()``) for entities
    to be exercised without booting a real Home Assistant core instance.
    """

    def __init__(self, data=None):
        self.data = dict(data) if data else {}
        self.last_update_success = True
        self.async_request_refresh = AsyncMock()
        self._listeners = []

    def async_add_listener(self, update_callback, context=None):
        self._listeners.append(update_callback)
        return lambda: self._listeners.remove(update_callback)

    def async_set_updated_data(self, data):
        self.data = data
        for listener in list(self._listeners):
            listener()


@pytest.fixture
def make_coordinator():
    """Factory fixture: make_coordinator({...}) -> FakeCoordinator."""
    return FakeCoordinator


class FakeHass:
    """Minimal stand-in for homeassistant.core.HomeAssistant.

    ``async_add_executor_job`` runs the callable inline (no real thread
    executor), so assertions against mocked ``api`` methods work
    synchronously within tests.
    """

    def __init__(self):
        self.data = {}
        self.config_entries = SimpleNamespace(
            async_forward_entry_setups=AsyncMock(return_value=None),
            async_unload_platforms=AsyncMock(return_value=True),
        )

    async def async_add_executor_job(self, func, *args):
        return func(*args)


@pytest.fixture
def make_hass():
    """Factory fixture: make_hass() -> FakeHass."""
    return FakeHass


@pytest.fixture
def fake_hass():
    """A ready-to-use FakeHass instance, for tests that only need one."""
    return FakeHass()


@pytest.fixture
def mock_api():
    """A MagicMock standing in for DuuxAPI, safe to assert call args on."""
    return MagicMock()
