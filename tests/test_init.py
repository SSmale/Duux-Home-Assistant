"""Unit tests for custom_components.duux (async_setup_entry / async_unload_entry /
DuuxDataUpdateCoordinator).

async_setup_entry's own device-classification logic is tested in isolation by
replacing DuuxDataUpdateCoordinator with a fake that skips straight past the
real coordinator's network/event-loop machinery -- that machinery is exercised
directly in the DuuxDataUpdateCoordinator tests further down instead.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from custom_components.duux import (
    DuuxDataUpdateCoordinator,
    async_remove_config_entry_device,
    async_setup_entry,
    async_unload_entry,
    const,
)
from homeassistant.helpers.update_coordinator import UpdateFailed


class FakeConfigEntry:
    def __init__(self, data, entry_id="entry_1"):
        self.data = data
        self.entry_id = entry_id


class FakeCoordinatorForSetup:
    """Stands in for DuuxDataUpdateCoordinator inside async_setup_entry tests."""

    instances = []

    def __init__(self, hass, api, device_id, device_name, config_entry=None):
        self.hass = hass
        self.api = api
        self.device_id = device_id
        self.device_name = device_name
        self.data = {}
        FakeCoordinatorForSetup.instances.append(self)

    async def async_config_entry_first_refresh(self):
        return None


@pytest.fixture(autouse=True)
def _reset_fake_coordinator_instances():
    FakeCoordinatorForSetup.instances = []
    yield
    FakeCoordinatorForSetup.instances = []


# ---------------------------------------------------------------------------
# async_setup_entry
# ---------------------------------------------------------------------------


async def test_async_setup_entry_creates_coordinator_per_device(
    fake_hass, devices_fixture
):
    entry = FakeConfigEntry(data={"email": "x@example.com", "password": "y"})

    with (
        patch("custom_components.duux.DuuxAPI.login", return_value=True),
        patch(
            "custom_components.duux.DuuxAPI.get_devices",
            return_value=devices_fixture,
        ),
        patch(
            "custom_components.duux.DuuxDataUpdateCoordinator",
            FakeCoordinatorForSetup,
        ),
    ):
        result = await async_setup_entry(fake_hass, entry)

    assert result is True
    assert const.DOMAIN in fake_hass.data
    stored = fake_hass.data[const.DOMAIN][entry.entry_id]
    assert len(stored["devices"]) == len(devices_fixture)
    assert len(stored["coordinators"]) == len(devices_fixture)
    assert len(FakeCoordinatorForSetup.instances) == len(devices_fixture)
    # Platforms get forwarded once setup succeeds.
    fake_hass.config_entries.async_forward_entry_setups.assert_awaited_once()


async def test_async_setup_entry_login_failure_returns_false(fake_hass):
    entry = FakeConfigEntry(data={"email": "x@example.com", "password": "y"})

    with patch("custom_components.duux.DuuxAPI.login", return_value=False):
        result = await async_setup_entry(fake_hass, entry)

    assert result is False
    assert const.DOMAIN not in fake_hass.data


async def test_async_setup_entry_no_devices_returns_false(fake_hass):
    entry = FakeConfigEntry(data={"email": "x@example.com", "password": "y"})

    with (
        patch("custom_components.duux.DuuxAPI.login", return_value=True),
        patch("custom_components.duux.DuuxAPI.get_devices", return_value=[]),
    ):
        result = await async_setup_entry(fake_hass, entry)

    assert result is False


async def test_async_setup_entry_warns_on_unrecognised_device(fake_hass):
    """A device with an unknown device_type_id and an unmatched google type
    should be skipped, but still allow setup to succeed with the recognised
    devices."""
    entry = FakeConfigEntry(data={"email": "x@example.com", "password": "y"})

    unrecognised = {
        "id": 999,
        "deviceId": "AA:UNKNOWN",
        "displayName": "Mystery Device",
        "sensorTypeId": 9999,
        "online": True,
        "connectionType": "mqtt",
        "sensorType": {
            "type": 9999,
            "name": "Mystery",
            "googleDeviceType": "action.devices.types.SOMETHING_ELSE",
        },
    }

    with (
        patch("custom_components.duux.DuuxAPI.login", return_value=True),
        patch(
            "custom_components.duux.DuuxAPI.get_devices",
            return_value=[unrecognised],
        ),
        patch(
            "custom_components.duux.DuuxDataUpdateCoordinator",
            FakeCoordinatorForSetup,
        ),
        patch("custom_components.duux.ir.async_create_issue") as mock_issue,
    ):
        result = await async_setup_entry(fake_hass, entry)

    assert result is True
    mock_issue.assert_called_once()
    assert mock_issue.call_args.kwargs["translation_key"] == "device_not_recognised"
    # No coordinator should have been created for the skipped device.
    assert fake_hass.data[const.DOMAIN][entry.entry_id]["coordinators"] == {}


async def test_async_setup_entry_warns_on_non_mqtt_device(fake_hass, device_by_stid):
    entry = FakeConfigEntry(data={"email": "x@example.com", "password": "y"})
    device = device_by_stid(50)  # Edge Heater V2 fixture
    device["connectionType"] = "tcp"

    with (
        patch("custom_components.duux.DuuxAPI.login", return_value=True),
        patch(
            "custom_components.duux.DuuxAPI.get_devices",
            return_value=[device],
        ),
        patch(
            "custom_components.duux.DuuxDataUpdateCoordinator",
            FakeCoordinatorForSetup,
        ),
        patch("custom_components.duux.ir.async_create_issue") as mock_issue,
    ):
        result = await async_setup_entry(fake_hass, entry)

    assert result is True
    mock_issue.assert_called_once()
    assert mock_issue.call_args.kwargs["translation_key"] == "device_not_mqtt"


# ---------------------------------------------------------------------------
# async_unload_entry
# ---------------------------------------------------------------------------


async def test_async_unload_entry_removes_stored_data_on_success(fake_hass):
    entry = FakeConfigEntry(data={}, entry_id="entry_1")
    fake_hass.data[const.DOMAIN] = {"entry_1": {"api": MagicMock()}}
    fake_hass.config_entries.async_unload_platforms = AsyncMock(return_value=True)

    result = await async_unload_entry(fake_hass, entry)

    assert result is True
    assert "entry_1" not in fake_hass.data[const.DOMAIN]


async def test_async_unload_entry_keeps_data_when_unload_fails(fake_hass):
    entry = FakeConfigEntry(data={}, entry_id="entry_1")
    fake_hass.data[const.DOMAIN] = {"entry_1": {"api": MagicMock()}}
    fake_hass.config_entries.async_unload_platforms = AsyncMock(return_value=False)

    result = await async_unload_entry(fake_hass, entry)

    assert result is False
    assert "entry_1" in fake_hass.data[const.DOMAIN]


# ---------------------------------------------------------------------------
# DuuxDataUpdateCoordinator (the real class, exercised directly -- this is
# the one place we construct the genuine DataUpdateCoordinator subclass,
# since _async_update_data() doesn't touch hass scheduling/event-loop internals)
# ---------------------------------------------------------------------------


async def test_coordinator_update_data_returns_api_payload(fake_hass):
    api = MagicMock()
    api.get_device_status.return_value = {"power": 1, "sp": 21}

    coordinator = DuuxDataUpdateCoordinator(
        fake_hass, api=api, device_id="AA:BB", device_name="Test Device",
        config_entry=MagicMock(),
    )

    data = await coordinator._async_update_data()

    assert data == {"power": 1, "sp": 21}
    api.get_device_status.assert_called_once_with("AA:BB")


async def test_coordinator_update_data_wraps_errors_in_update_failed(fake_hass):
    api = MagicMock()
    api.get_device_status.side_effect = RuntimeError("connection reset")

    coordinator = DuuxDataUpdateCoordinator(
        fake_hass, api=api, device_id="AA:BB", device_name="Test Device",
        config_entry=MagicMock(),
    )

    with pytest.raises(UpdateFailed):
        await coordinator._async_update_data()


# ---------------------------------------------------------------------------
# async_remove_config_entry_device
#
# The entity registry itself is mocked out here rather than exercised for
# real: this function's own job is the looping/filtering/removal logic, and
# the entity registry is a well-tested HA core collaborator, not something
# this integration needs to re-verify.
# ---------------------------------------------------------------------------


def _make_entity(entity_id, device_id):
    return type("RegistryEntity", (), {"entity_id": entity_id, "device_id": device_id})()


async def test_async_remove_config_entry_device_removes_all_matching_entities(
    fake_hass,
):
    entry = FakeConfigEntry(data={}, entry_id="entry_1")
    device_entry = type("DeviceEntry", (), {"id": "device_1"})()

    entity_1 = _make_entity("climate.heater", "device_1")
    entity_2 = _make_entity("sensor.temp", "device_1")
    other_device_entity = _make_entity("switch.other", "device_2")

    mock_registry = MagicMock()

    with (
        patch("custom_components.duux.er.async_get", return_value=mock_registry),
        patch(
            "custom_components.duux.er.async_entries_for_config_entry",
            side_effect=[
                [entity_1, entity_2, other_device_entity],  # before removal
                [other_device_entity],  # after removal
            ],
        ),
    ):
        result = await async_remove_config_entry_device(fake_hass, entry, device_entry)

    assert result is True
    assert mock_registry.async_remove.call_count == 2
    mock_registry.async_remove.assert_any_call("climate.heater")
    mock_registry.async_remove.assert_any_call("sensor.temp")


async def test_async_remove_config_entry_device_blocks_if_entities_remain(fake_hass):
    """If entities for this device are still registered after the removal
    pass (e.g. one couldn't be removed), removal should be refused."""
    entry = FakeConfigEntry(data={}, entry_id="entry_1")
    device_entry = type("DeviceEntry", (), {"id": "device_1"})()

    entity_1 = _make_entity("climate.heater", "device_1")
    mock_registry = MagicMock()

    with (
        patch("custom_components.duux.er.async_get", return_value=mock_registry),
        patch(
            "custom_components.duux.er.async_entries_for_config_entry",
            side_effect=[[entity_1], [entity_1]],
        ),
    ):
        result = await async_remove_config_entry_device(fake_hass, entry, device_entry)

    assert result is False


async def test_async_remove_config_entry_device_no_matching_entities_is_a_noop(
    fake_hass,
):
    entry = FakeConfigEntry(data={}, entry_id="entry_1")
    device_entry = type("DeviceEntry", (), {"id": "device_1"})()
    other_device_entity = _make_entity("switch.other", "device_2")

    mock_registry = MagicMock()

    with (
        patch("custom_components.duux.er.async_get", return_value=mock_registry),
        patch(
            "custom_components.duux.er.async_entries_for_config_entry",
            return_value=[other_device_entity],
        ),
    ):
        result = await async_remove_config_entry_device(fake_hass, entry, device_entry)

    assert result is True
    mock_registry.async_remove.assert_not_called()
