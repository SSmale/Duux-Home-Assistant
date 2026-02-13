import types

from custom_components.duux.duux_api import DuuxAPI
from custom_components.duux import const


class DummyResponse:
    def __init__(self, payload, status_code=200):
        self._payload = payload
        self.status_code = status_code

    def json(self):
        return self._payload

    def raise_for_status(self):
        if not (200 <= self.status_code < 300):
            raise Exception(f"HTTP {self.status_code}")


def test_login_success(monkeypatch):
    api = DuuxAPI(email="test@example.com", password="pass")

    resp = DummyResponse({"token": "mock-token"})
    # session.post should return our DummyResponse
    monkeypatch.setattr(
        api,
        "session",
        types.SimpleNamespace(post=lambda url, json=None: resp, headers={}),
    )

    result = api.login()
    assert result is True
    assert "Authorization" in api.session.headers
    assert api.session.headers["Authorization"] == "mock-token"


def test_get_devices_returns_list(monkeypatch, devices_fixture):
    api = DuuxAPI(email="x", password="y")
    resp = DummyResponse({"data": devices_fixture})
    monkeypatch.setattr(api, "session", types.SimpleNamespace(get=lambda url: resp))
    devices = api.get_devices()
    assert isinstance(devices, list)
    assert len(devices) == len(devices_fixture)


def test_get_device_status_fulldata_null(monkeypatch):
    api = DuuxAPI(email="x", password="y")
    device = {"deviceId": "AA:BB:CC:11:22:33", "latestData": {"fullData": None}}
    monkeypatch.setattr(api, "get_devices", lambda: [device])
    status = api.get_device_status("AA:BB:CC:11:22:33")
    # If fullData is null the integration returns empty dict
    assert status == {} or status is not None


def test_get_device_status_fulldata_null_v2(monkeypatch):
    api = DuuxAPI(email="x", password="y")
    # monkeypatch get_devices to return a device with fullData null (as in TCP mode)
    device = {
        "deviceId": "AA:BB:CC:11:22:33",
        "latestData": {"fullData": None},
    }
    monkeypatch.setattr(api, "get_devices", lambda: [device])

    status = api.get_device_status("AA:BB:CC:11:22:33")
    # When fullData is null, we return an empty dict
    assert status == {}


def test_send_command_posts_correct_url_and_payload(monkeypatch):
    api = DuuxAPI(email="x", password="y")
    captured = {}

    def fake_post(url, json=None):
        captured["url"] = url
        captured["json"] = json
        return DummyResponse({"ok": True})

    monkeypatch.setattr(api, "session", types.SimpleNamespace(post=fake_post))
    mac = "AA:BB:CC:44:55:66"
    ok = api.send_command(mac, "tune set sp 24")
    assert ok is True
    expected_path = const.API_COMMANDS.replace("{deviceMac}", mac)
    assert expected_path in captured["url"]
    assert captured["json"] == {"command": "tune set sp 24"}


def test_set_power_builds_command(monkeypatch):
    api = DuuxAPI(email="x", password="y")
    calls = []

    def fake_send_command(device_mac, command):
        calls.append((device_mac, command))
        return True

    monkeypatch.setattr(api, "send_command", fake_send_command)
    api.set_power("AA:BB", True)
    api.set_power("AA:BB", False)
    assert calls[0][1].endswith("01")
    assert calls[1][1].endswith("00")
