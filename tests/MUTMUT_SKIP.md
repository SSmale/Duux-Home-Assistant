# Surviving mutmut mutants — intentionally not tested

Run `mutmut results` to see the current survivor list.
Run `make mutmut` to re-run mutation testing.

The categories below survive and are **not worth adding tests for**. The reason is noted for each so the decision can be revisited if circumstances change.

---

## `async_setup_entry` in every platform module (~357 survivors)

**What mutmut mutates:** String literals and comparisons inside the platform setup loops — things like `sensorTypeId` comparisons, `translation_key` values, `device_class` constants, and the order entities are appended.

**Why not tested:** We already have platform-dispatch tests in each `test_*.py` file that check *which entity classes* get created for *which device types*. The detail-level mutations (e.g. changing `"error_message"` to `"XXerror_messageXX"` in a `translation_key`) are HA-framework values that are validated by HA's entity registry at runtime, not by unit tests. Catching them would require booting a real HA instance.

---

## `__init__` methods on entity classes (~200 survivors across all platforms)

**What mutmut mutates:** HA entity attribute assignments — `_attr_unique_id`, `_attr_has_entity_name`, `_attr_device_info`, `_attr_supported_features`, `_attr_attribution`, `native_unit_of_measurement`, `device_class`, `entity_category`, icon strings, etc.

**Why not tested:** These are HA integration contract values. Mutation of them (e.g. flipping `FanEntityFeature.OSCILLATE` out of `_attr_supported_features`) would only surface as a mismatch in the HA UI, not in unit tests. The setup is boilerplate verified by the platform-dispatch tests; exhaustive `__init__` assertions would be brittle and provide no regression value beyond what HA's own validation already provides.

---

## `_discover_speeds`, `_discover_modes`, `presets_discovery` (~200 survivors)

**What mutmut mutates:** Minor string parsing details inside the auto-discovery methods — field name lookups (`speed_name` vs `speedName`), fallback values in `dict.get()`, early-continue conditions for malformed trait entries.

**Why not tested:** These methods are already exercised by the existing autodiscovery tests (`test_fan_autodiscovery_parses_traits_for_speeds_and_modes`, `test_threesixty_climate_discovers_presets_from_fixture`, etc.). The surviving mutations are in defensive branches (handling of malformed fixture data) or in minor fallback strings that don't change observable behaviour in any fixture that exists. Adding tests for every field alias would require duplicating the full fixture structure per variant, producing fragile tests with no real-world failure scenario.

---

## `_get_traits` (~30 survivors)

**What mutmut mutates:** The deep-search helper that walks nested dicts/lists looking for the `Traits` key, and fallback logic when the key isn't found at the expected level.

**Why not tested:** `_get_traits` is a private implementation detail of autodiscovery. It is indirectly exercised by the autodiscovery tests. The surviving mutants are in the defensive fallback path (`_deep_find`) that only activates when `Traits` is nested unexpectedly — a situation not represented by any fixture and not seen in production data.

---

## `async_remove_config_entry_device` (~10 survivors)

**What mutmut mutates:** The cleanup logic run when HA removes a device from the config entry — coordinator cancellation, registry cleanup.

**Why not tested:** This function interacts with HA's device registry and entity registry internals. Unit-testing it without a running HA instance would require mocking the entire registry surface. The logic is simple (cancel coordinators, clean up state), and the risk of a bug here is low compared to the cost of maintaining the mocks.

---

## `DuuxDataUpdateCoordinator.__init__` (~7 survivors)

**What mutmut mutates:** The update interval value and the coordinator's `name` string.

**Why not tested:** These are HA DataUpdateCoordinator wiring values. The interval is a configuration constant; changing it has no effect in unit tests because `FakeCoordinator` in `conftest.py` doesn't use it. Testing the exact interval value would only be meaningful in an integration test with a real HA scheduler.

---

## `DuuxConfigFlowǁasync_step_user` (~8 survivors)

**What mutmut mutates:** String constants in the config flow form schema and error messages.

**Why not tested:** Config flow testing requires HA's flow manager (`hass.config_entries.flow`). The existing `test_config_flow.py` covers the happy path via the full HA test harness. Extending coverage to every mutated string constant would require the heavyweight `pytest-homeassistant-custom-component` setup that this project deliberately avoids (see `tests/requirements.txt`).

---

## `diagnostics.x_async_get_config_entry_diagnostics__mutmut_10`

**What mutmut mutates:** The error message string inside `raise UpdateFailed(...)` — changes `UpdateFailed(f"Error communicating with API: {err}")` to `UpdateFailed(None)`.

**Why not tested:** The exception *type* (`UpdateFailed`) is what HA cares about; the message is only for human-readable logs. Asserting the exact error message string is brittle and adds no safety net for real bugs.
