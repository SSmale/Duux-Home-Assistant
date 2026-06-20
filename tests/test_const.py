"""Unit tests for custom_components.duux.const."""

from custom_components.duux.const import DUUX_ERRID


def test_known_error_codes_resolve_by_value():
    assert DUUX_ERRID(0) is DUUX_ERRID.OK
    assert DUUX_ERRID(4) is DUUX_ERRID.Ice_Detected
    assert DUUX_ERRID(8) is DUUX_ERRID.Water_Tank_Full
    assert DUUX_ERRID(None) is DUUX_ERRID.Unavailable


def test_unrecognised_error_code_falls_back_to_unknown_error():
    """The _missing_ hook should catch any code we don't explicitly model."""
    assert DUUX_ERRID(123456) is DUUX_ERRID.Unknown_Error


def test_unknown_error_name_is_human_readable():
    # binary_sensor.py / sensor.py rely on `.name.replace("_", " ")`
    assert DUUX_ERRID.Unknown_Error.name.replace("_", " ") == "Unknown Error"
    assert DUUX_ERRID.Ice_Detected.name.replace("_", " ") == "Ice Detected"
