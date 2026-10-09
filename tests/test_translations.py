"""Ensure every supported language covers the authentication flow."""

import json
from pathlib import Path

import pytest

TRANSLATIONS = (
    Path(__file__).resolve().parents[1] / "custom_components/duux/translations"
)


@pytest.mark.parametrize(
    "path", sorted(TRANSLATIONS.glob("*.json")), ids=lambda p: p.stem
)
def test_authentication_steps_and_errors_are_translated(path):
    config = json.loads(path.read_text(encoding="utf-8"))["config"]
    for menu in ("user", "reauth_confirm"):
        assert set(config["step"][menu]["menu_options"]) == {
            "passwordless",
            "password",
        }
    assert set(config["step"]["password"]["data"]) == {"email", "password"}
    assert set(config["step"]["passwordless"]["data"]) == {"email"}
    assert set(config["step"]["verify_code"]["data"]) == {"code", "resend"}
    assert "{email}" in config["step"]["verify_code"]["description"]
    assert "{email}" in config["step"]["reauth_confirm"]["description"]
    assert {
        "invalid_auth",
        "invalid_code",
        "cannot_connect",
        "rate_limited",
        "invalid_response",
        "wrong_account",
    } <= config["error"].keys()
    assert {
        "already_configured",
        "reauth_successful",
        "reconfigure_successful",
        "login_cancelled",
    } <= config["abort"].keys()
