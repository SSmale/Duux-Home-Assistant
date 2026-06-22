"""Unit tests for custom_components.duux.duux_api.DuuxAPI.

These tests never touch the network: DuuxAPI.session is replaced with a
MagicMock, so every test asserts on the *shape* of the HTTP call (URL,
method, JSON body) rather than performing one.
"""

from unittest.mock import MagicMock

import pytest

from custom_components.duux import const
from custom_components.duux.duux_api import DuuxAPI


def make_response(payload=None, status_code=200, raise_exc=None):
    """Build a fake `requests.Response`-like object."""
    response = MagicMock()
    response.status_code = status_code
    response.json.return_value = payload or {}
    if raise_exc is not None:
        response.raise_for_status.side_effect = raise_exc
    else:
        response.raise_for_status.return_value = None
    return response


@pytest.fixture
def api():
    instance = DuuxAPI(email="user@example.com", password="hunter2")
    instance.session = MagicMock()
    return instance


# ---------------------------------------------------------------------------
# login
# ---------------------------------------------------------------------------


def test_login_success_sets_token_and_auth_header(api):
    api.session.post.return_value = make_response({"token": "mock-token"})

    assert api.login() is True
    assert api.token == "mock-token"
    api.session.headers.update.assert_called_once_with({"Authorization": "mock-token"})
    posted_url = api.session.post.call_args.args[0]
    assert posted_url == f"{const.API_BASE_URL}{const.API_LOGIN}"
    assert api.session.post.call_args.kwargs["json"] == {
        "username": "user@example.com",
        "password": "hunter2",
    }


def test_login_no_token_in_response_returns_false(api):
    api.session.post.return_value = make_response({})

    assert api.login() is False
    assert api.token is None


def test_login_http_error_returns_false(api):
    api.session.post.return_value = make_response(
        status_code=401, raise_exc=Exception("401 Unauthorized")
    )

    assert api.login() is False


# ---------------------------------------------------------------------------
# get_devices / get_device_status
# ---------------------------------------------------------------------------


def test_get_devices_returns_list(api, devices_fixture):
    api.session.get.return_value = make_response({"data": devices_fixture})

    devices = api.get_devices()

    assert devices == devices_fixture
    api.session.get.assert_called_once_with(f"{const.API_BASE_URL}{const.API_SENSORS}")


def test_get_devices_on_error_returns_empty_list(api):
    api.session.get.side_effect = Exception("network error")

    assert api.get_devices() == []


def test_get_device_status_merges_online_and_connection_type(api):
    device = {
        "deviceId": "AA:BB:CC",
        "online": True,
        "connectionType": "mqtt",
        "latestData": {"fullData": {"power": 1, "sp": 21}},
    }
    api.session.get.return_value = make_response({"data": [device]})

    status = api.get_device_status("AA:BB:CC")

    assert status == {
        "power": 1,
        "sp": 21,
        "online": True,
        "connectionType": "mqtt",
    }


def test_get_device_status_fulldata_null_returns_online_and_type_only(api):
    """TCP-mode devices report latestData.fullData as null."""
    device = {
        "deviceId": "AA:BB:CC",
        "online": False,
        "connectionType": "tcp",
        "latestData": {"fullData": None},
    }
    api.session.get.return_value = make_response({"data": [device]})

    status = api.get_device_status("AA:BB:CC")

    assert status == {"online": False, "connectionType": "tcp"}


def test_get_device_status_latest_data_missing_entirely(api):
    device = {"deviceId": "AA:BB:CC", "online": True, "connectionType": "mqtt"}
    api.session.get.return_value = make_response({"data": [device]})

    status = api.get_device_status("AA:BB:CC")

    assert status == {"online": True, "connectionType": "mqtt"}


def test_get_device_status_unknown_device_returns_empty_dict(api):
    api.session.get.return_value = make_response({"data": []})

    assert api.get_device_status("doesnt-exist") == {}


def test_get_device_status_does_not_mutate_source_data(api):
    """data_copy must be a copy, not a live reference into fullData."""
    full_data = {"power": 1, "sp": 21}
    device = {
        "deviceId": "AA:BB:CC",
        "online": True,
        "connectionType": "mqtt",
        "latestData": {"fullData": full_data},
    }
    api.session.get.return_value = make_response({"data": [device]})

    status = api.get_device_status("AA:BB:CC")
    status["sp"] = 999

    assert full_data["sp"] == 21


# ---------------------------------------------------------------------------
# send_command
# ---------------------------------------------------------------------------


def test_send_command_posts_correct_url_and_payload(api):
    api.session.post.return_value = make_response({"ok": True})

    result = api.send_command("AA:BB:CC", "tune set sp 24")

    assert result is True
    expected_url = f"{const.API_BASE_URL}{const.API_COMMANDS}".replace(
        "{deviceMac}", "AA:BB:CC"
    )
    api.session.post.assert_called_once_with(
        expected_url, json={"command": "tune set sp 24"}
    )


def test_send_command_http_error_returns_false(api):
    api.session.post.return_value = make_response(
        status_code=500, raise_exc=Exception("boom")
    )

    assert api.send_command("AA:BB:CC", "tune set sp 24") is False


# ---------------------------------------------------------------------------
# Convenience setters -> correct command strings
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("method", "args", "expected_command"),
    [
        ("set_power", (True,), "tune set power 01"),
        ("set_power", (False,), "tune set power 00"),
        ("set_temperature", (24,), "tune set sp 24"),
        ("set_temperature", (1,), "tune set sp 5"),  # clamps to min 5
        ("set_temperature", (99,), "tune set sp 36"),  # clamps to max 36
        ("set_humidity", (55,), "tune set sp 55"),
        ("set_humidity", (5,), "tune set sp 30"),  # clamps to min 30
        ("set_humidity", (200,), "tune set sp 80"),  # clamps to max 80
        ("set_mode", (2,), "tune set heating 2"),
        ("set_mode", (0,), "tune set heating 1"),  # clamps to min 1
        ("set_mode", (99,), "tune set heating 3"),  # clamps to max 3
        ("set_dry_mode", (1,), "tune set mode 1"),
        ("set_fan", (0,), "tune set fan 0"),
        ("set_ionizer", (True,), "tune set ion 1"),
        ("set_ionizer", (False,), "tune set ion 0"),
        ("set_night_mode", (True,), "tune set night 01"),
        ("set_night_mode", (False,), "tune set night 00"),
        ("set_sleep_mode", (True,), "tune set sleep 01"),
        ("set_lock", (True,), "tune set lock 1"),
        ("set_lock", (False,), "tune set lock 0"),
        ("set_cleaning_mode", (True,), "tune set dry 01"),
        ("set_laundry_mode", (True,), "tune set laundr 01"),
        ("set_timer", (4,), "tune set timer 4"),
        ("set_timer", (99,), "tune set timer 24"),  # clamps to max 24
        ("set_humidifier_mode", (1,), "tune set mode 1"),
        ("set_horosc_angle", (2,), "tune set horosc 2"),
        ("set_horosc_angle", (99,), "tune set horosc 3"),  # clamps to max 3
        ("set_horosc_bool", (1,), "tune set horosc 1"),
        ("set_horosc_bool", (0,), "tune set horosc 0"),
        ("set_horosc_bool", (99,), "tune set horosc 1"),  # clamps to max 3
        ("set_verosc", (1,), "tune set verosc 1"),
        ("set_verosc", (99,), "tune set verosc 2"),  # clamps to max 2
        ("set_swing", (2,), "tune set swing 2"),
        ("set_swing", (99,), "tune set swing 3"),  # clamps to max 3
        ("set_tilt", (1,), "tune set tilt 1"),
        ("set_tilt", (99,), "tune set tilt 2"),  # clamps to max 2
        ("set_fan_speed", (15,), "tune set speed 15"),
        ("set_fan_speed", (999,), "tune set speed 30"),  # clamps to max 30
        ("set_purifier_speed", (2,), "tune set speed 2"),
        ("set_purifier_speed", (999,), "tune set speed 4"),  # clamps to max 4
    ],
)
def test_convenience_setters_build_expected_command(
    api, method, args, expected_command
):
    api.session.post.return_value = make_response({"ok": True})

    result = getattr(api, method)("AA:BB:CC", *args)

    assert result is True
    assert api.session.post.call_args.kwargs["json"] == {"command": expected_command}
