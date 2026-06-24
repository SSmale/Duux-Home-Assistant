"""Unit tests for custom_components.duux.sensor."""

from custom_components.duux import const
from custom_components.duux.sensor import (
    DuuxAirQualitySensor,
    DuuxConnectionTypeSensor,
    DuuxErrorSensor,
    DuuxTVOCSensor,
    DuuxTempSensor,
    async_setup_entry,
)


# ---------------------------------------------------------------------------
# DuuxTempSensor -- plain key passthrough
# ---------------------------------------------------------------------------


def test_temp_sensor_initial_value(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(50)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxTempSensor(coordinator, mock_api, device)

    assert entity.native_value == 19


def test_temp_sensor_updates_on_coordinator_push(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(50)
    coordinator = make_coordinator(device["latestData"]["fullData"])
    entity = DuuxTempSensor(coordinator, mock_api, device)
    entity.async_write_ha_state = lambda: None  # not registered with hass

    coordinator.async_set_updated_data({"temp": 25})
    entity._handle_coordinator_update()

    assert entity.native_value == 25


# ---------------------------------------------------------------------------
# DuuxTVOCSensor / DuuxAirQualitySensor -- numeric -> label mapping
# ---------------------------------------------------------------------------


def test_tvoc_sensor_maps_raw_value_to_label(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(61)
    coordinator = make_coordinator(device["latestData"]["fullData"])  # tvoc == 0
    entity = DuuxTVOCSensor(coordinator, mock_api, device)
    entity.async_write_ha_state = lambda: None

    entity._handle_coordinator_update()

    assert entity.native_value == "healthy"


def test_tvoc_sensor_unknown_raw_value_passed_through(make_coordinator, mock_api):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Purifier"}
    coordinator = make_coordinator({"tvoc": 99})
    entity = DuuxTVOCSensor(coordinator, mock_api, device)
    entity.async_write_ha_state = lambda: None

    entity._handle_coordinator_update()

    assert entity.native_value == 99


def test_air_quality_sensor_maps_raw_value_to_label(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(61)
    coordinator = make_coordinator(device["latestData"]["fullData"])  # aq == 1
    entity = DuuxAirQualitySensor(coordinator, mock_api, device)
    entity.async_write_ha_state = lambda: None

    entity._handle_coordinator_update()

    assert entity.native_value == "very_good"


# ---------------------------------------------------------------------------
# DuuxErrorSensor -- DUUX_ERRID enum -> human readable name
# ---------------------------------------------------------------------------


def test_error_sensor_ok_state(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(61)
    coordinator = make_coordinator(device["latestData"]["fullData"])  # err == 0
    entity = DuuxErrorSensor(coordinator, mock_api, device)

    assert entity.native_value == "OK"


def test_error_sensor_unknown_code(make_coordinator, mock_api):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Heater"}
    coordinator = make_coordinator({"err": 424242})
    entity = DuuxErrorSensor(coordinator, mock_api, device)

    assert entity.native_value == "Unknown Error"


def test_error_sensor_null_api_value_is_ok(make_coordinator, mock_api):
    """JSON null (Python None) on the err key means no error."""
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Heater"}
    coordinator = make_coordinator({"err": None})
    entity = DuuxErrorSensor(coordinator, mock_api, device)

    assert entity.native_value == "OK"


def test_error_sensor_missing_key_is_unavailable(make_coordinator, mock_api):
    """Key absent entirely means the device hasn't reported an error state yet."""
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Heater"}
    coordinator = make_coordinator({})
    entity = DuuxErrorSensor(coordinator, mock_api, device)

    assert entity.native_value == "Unavailable"


# ---------------------------------------------------------------------------
# DuuxConnectionTypeSensor
# ---------------------------------------------------------------------------


def test_connection_type_sensor_normalises_to_lowercase(
    device_by_stid, make_coordinator, mock_api
):
    device = device_by_stid(50)
    data = dict(device["latestData"]["fullData"])
    data["connectionType"] = "MQTT"
    coordinator = make_coordinator(data)
    entity = DuuxConnectionTypeSensor(coordinator, mock_api, device)

    assert entity.native_value == "mqtt"


def test_connection_type_sensor_none_when_missing(make_coordinator, mock_api):
    device = {"id": 1, "deviceId": "AA:BB", "displayName": "Heater"}
    coordinator = make_coordinator({})
    entity = DuuxConnectionTypeSensor(coordinator, mock_api, device)

    assert entity.native_value is None


# ---------------------------------------------------------------------------
# available
# ---------------------------------------------------------------------------


def test_available_false_when_offline(device_by_stid, make_coordinator, mock_api):
    device = device_by_stid(50)
    data = dict(device["latestData"]["fullData"])
    data["online"] = False
    coordinator = make_coordinator(data)
    entity = DuuxTempSensor(coordinator, mock_api, device)

    assert entity.available is False


# ---------------------------------------------------------------------------
# Platform dispatch
# ---------------------------------------------------------------------------


async def test_async_setup_entry_bright2_gets_air_quality_sensor_suite(
    fake_hass, devices_fixture, make_coordinator
):
    coordinators = {
        d["deviceId"]: make_coordinator(d["latestData"]["fullData"])
        for d in devices_fixture
    }
    entry = type("Entry", (), {"entry_id": "entry_1"})()
    fake_hass.data[const.DOMAIN] = {
        "entry_1": {
            "api": object(),
            "coordinators": coordinators,
            "devices": devices_fixture,
        }
    }

    added = []
    await async_setup_entry(fake_hass, entry, added.append)
    entities = added[0]

    by_device = {}
    for entity in entities:
        by_device.setdefault(entity._device_mac, []).append(type(entity).__name__)

    bright2_sensors = sorted(by_device["AA:00:00:00:00:10"])
    assert bright2_sensors == sorted(
        [
            "DuuxPM25Sensor",
            "DuuxTVOCSensor",
            "DuuxFilterLifeSensor",
            "DuuxAirQualitySensor",
            "DuuxBright2TimeRemainingSensor",
            "DuuxErrorSensor",
            "DuuxConnectionTypeSensor",
        ]
    )

    # A plain heater (Edge V2) just gets the generic temp + error + connection sensors.
    edge_sensors = sorted(by_device["AA:00:00:00:00:01"])
    assert edge_sensors == sorted(
        ["DuuxTempSensor", "DuuxErrorSensor", "DuuxConnectionTypeSensor"]
    )

    # Bora 2024 gets humidity + time-remaining + error + connection.
    bora_sensors = sorted(by_device["AA:00:00:00:00:05"])
    assert bora_sensors == sorted(
        [
            "DuuxHumiditySensor",
            "DuuxBora2024TimeRemainingSensor",
            "DuuxErrorSensor",
            "DuuxConnectionTypeSensor",
        ]
    )

    # Beam Mini gets humidity + temp + error + connection.
    beam_sensors = sorted(by_device["AA:00:00:00:00:06"])
    assert beam_sensors == sorted(
        [
            "DuuxHumiditySensor",
            "DuuxTempSensor",
            "DuuxErrorSensor",
            "DuuxConnectionTypeSensor",
        ]
    )
