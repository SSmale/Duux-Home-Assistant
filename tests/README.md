# Tests

Unit tests for the Duux Home Assistant integration.

## Running

```bash
pip install -r tests/requirements.txt
pytest -q
```

(`pytest.ini` at the repo root points `pytest` at this directory, so `pytest -q`
from anywhere in the repo works too.)

## Design notes

**No `pytest-homeassistant-custom-component`.** That package gives you a real,
working fake `hass` instance, which is great for true integration tests, but
it's a large, fast-moving dependency pinned to a specific Home Assistant core
release, and it's overkill for unit-testing a single custom component. These
tests instead import the real entity base classes from a plain `homeassistant`
install and exercise them with small, explicit fakes for `hass` / `coordinator`
(see `conftest.py`: `FakeHass`, `FakeCoordinator`). That keeps the suite fast,
easy to debug, and far less likely to break on unrelated HA core changes.

`FakeCoordinator` implements just `.data`, `.last_update_success`,
`.async_add_listener()`, `.async_request_refresh()`, and
`.async_set_updated_data()` — the only coordinator surface the integration's
entities actually touch. `FakeHass.async_add_executor_job` runs the given
callable inline (no real thread executor), so assertions against the mocked
`api` object happen synchronously inside the `await`.

`DuuxDataUpdateCoordinator` itself (in `__init__.py`) is the one place a real
Home Assistant class is constructed directly rather than faked — its
`_async_update_data()` doesn't touch the event loop/scheduler, so it's safe to
exercise directly (see `test_init.py`). `async_setup_entry()`'s own
device-classification logic is tested separately by substituting a trivial
fake in place of `DuuxDataUpdateCoordinator`, so that test doesn't depend on
coordinator internals at all.

**Fixture data:** `fixtures/devices.json` has one representative device per
supported product (covering every `sensorTypeId` branch across `climate.py`,
`fan.py`, `humidifier.py`, `switch.py`, and `select.py`), so the platform
dispatch tests (`test_*_async_setup_entry_dispatches_*`) double as a
regression check that each device type still routes to the correct entity
classes.

## Dependency management

`tests/requirements.txt` is **generated** — do not edit it directly.

The source of truth is `tests/requirements.in`, which lists loose constraints.
To regenerate the locked file after changing `.in` or to pull in a newer HA
release:

```bash
make compile-deps
```

CI installs from `tests/requirements.txt` and runs on Python 3.13 (required by
`homeassistant >= 2025.2.0`).

## Minimum HA version

Three files must always agree on the minimum Home Assistant version the
integration requires:

| File | Field |
| --- | --- |
| `hacs.json` | `"homeassistant"` |
| `custom_components/duux/manifest.json` | `"homeassistant"` |
| `tests/requirements.in` | `homeassistant>=` lower bound |

When you use a new HA API, find the release it was introduced in and, if it is
higher than the current minimum, run:

```bash
make bump-min-ha VERSION=2025.3.0
```

This updates all three files and regenerates `tests/requirements.txt` in one
step. Commit all four files together.
