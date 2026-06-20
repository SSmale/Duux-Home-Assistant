"""A few basic unit tests for duux_api.py — one scenario per test, JUnit
style. No Home Assistant needed, just pytest + requests.

Run with:
    pytest tests/test_duux_api.py -v
"""

from unittest.mock import MagicMock
import pytest

from custom_components.duux.duux_api import DuuxAPI


@pytest.fixture
def api():
    """A DuuxAPI instance with a mocked session — no real network calls."""
    instance = DuuxAPI(email="test@testMail.com", password="escapeTheMatrix")
    instance.session = MagicMock()
    return instance


def test_login_success(api):
    response = MagicMock()
    response.json.return_value = {"token": "abc123"}
    api.session.post.return_value = response

    result = api.login()

    assert result is True
    assert api.token == "abc123"


def test_login_fails_when_no_token_returned(api):
    response = MagicMock()
    response.json.return_value = {}
    api.session.post.return_value = response

    result = api.login()

    assert result is False


def test_set_power_sends_correct_command(api):
    api.session.post.return_value = MagicMock()

    api.set_power("AA:BB", True)

    sent_command = api.session.post.call_args.kwargs["json"]["command"]
    assert sent_command == "tune set power 01"


def test_set_speed_clamps_out_of_range_value(api):
    """Regression test: set_speed used to name its own parameters
    'min'/'max', shadowing the builtin min()/max() functions used inside
    the method body. If that ever comes back, this test fails."""
    api.session.post.return_value = MagicMock()

    api.set_speed("AA:BB", 999, min_speed=1, max_speed=30)

    sent_command = api.session.post.call_args.kwargs["json"]["command"]
    assert sent_command == "tune set speed 30"