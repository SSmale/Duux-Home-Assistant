"""Entity-level regression test — needs the real Home Assistant core.

Setup (once, in a clean virtual environment — see README_TESTS.md):

    python3 -m venv .venv
    source .venv/bin/activate          # Windows: .venv\\Scripts\\activate
    pip install pytest-homeassistant-custom-component

Run with:
    pytest tests/test_entity_registration.py -v

This covers a bug already documented in the project summary:
sensor.DuuxErrorSensor and binary_sensor.DuuxErrorSensor both build their
unique_id as f"duux_{device_id}_err" — same string, same device, two
different entities. Once that's fixed (e.g. by adding a suffix on one
side), update this test to assert the IDs are DIFFERENT instead.
"""

from custom_components.duux import sensor as duux_sensor
from custom_components.duux import binary_sensor as duux_binary_sensor


class FakeCoordinator:
    """Lightweight stand-in for DuuxDataUpdateCoordinator — just needs
    .data and .last_update_success for these entities to initialise."""

    def __init__(self, data):
        self.data = data
        self.last_update_success = True

    def async_add_listener(self, *_args, **_kwargs):
        return lambda: None


def make_fake_device():
    return {
        "id": "123",
        "deviceId": "AA:BB:CC",
        "displayName": "Test Heater",
        "manufacturer": "Duux",
        "sensorType": {"name": "Edge Heater"},
    }


def test_error_sensor_unique_ids_currently_collide():
    coordinator = FakeCoordinator(data={"err": 0, "online": True})
    device = make_fake_device()

    sensor_entity = duux_sensor.DuuxErrorSensor(coordinator, api=None, device=device)
    binary_entity = duux_binary_sensor.DuuxErrorSensor(coordinator, api=None, device=device)

    # Currently PASSES because the bug is still present (both IDs match).
    assert sensor_entity.unique_id == binary_entity.unique_id