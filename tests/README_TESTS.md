# How to run these tests (written for someone new to Python)

There are **two "tiers"** of tests here, with different requirements.

## Tier 1 — `test_duux_api.py` (simple, zero Home Assistant)

These only test `duux_api.py` (login, commands, value clamping, etc.)
against a mocked HTTP session. They never touch `homeassistant`, so
**nothing heavy needs to be installed**.

```bash
pip install pytest requests
pytest tests/test_duux_api.py -v
```

(If you get an "externally-managed-environment" error, use
`pip install --break-system-packages pytest requests` instead.)

You should see `4 passed`.

## Tier 2 — `test_entity_registration.py` (needs real Home Assistant)

This one instantiates real entities (`sensor.py`, `binary_sensor.py`),
so it needs the actual `homeassistant` package installed.

```bash
# Once, inside the repo folder:
python3 -m venv .venv

# Every time you open a new terminal to work on the tests:
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# Once, inside the active venv:
pip install pytest-homeassistant-custom-component
```

### Important: version pin

`pytest-homeassistant-custom-component` can pull in a `pytest` + `pytest-asyncio`
combo that are incompatible with each other (pytest-asyncio 1.x removed
an `event_loop` fixture this package still relies on internally — an
upstream coordination gap, not something in our code). If you hit
errors mentioning `enable_event_loop_debug` or `event_loop`, run:

```bash
pip install "pytest<9" "pytest-asyncio<1"
```

This turns the issue from a hard failure into a harmless warning. The
`pytest.ini` in the repo root also silences that specific warning, so
you shouldn't see it at all once both are in place.

```bash
pytest tests/test_entity_registration.py -v
```

You should see `1 passed`. This test currently **documents** a known
bug (the `duux_X_err` unique_id collision). It will keep passing as
long as that bug exists. Once it's fixed, change the test's `assert ... ==` to
`assert ... !=` so it catches a regression of the same bug in the future.

## Running everything together

Inside the active venv (which already has pytest + requests once Tier 2
is installed):

```bash
pytest tests/ -v
```

## For later

Tests for other files (`select.py`, `switch.py`, `climate.py`, the
`__init__.py` setup flow) would also need the Tier 2 setup, since they
import `homeassistant.components.*`.