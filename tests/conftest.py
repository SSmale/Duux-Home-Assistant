"""Shared test setup.

`duux_api.py` itself needs zero Home Assistant (just `requests`). The
problem is that it lives inside the `custom_components.duux` package, and
that package's `__init__.py` imports a bunch of `homeassistant.*` modules.
A plain `import custom_components.duux.duux_api` would run that
`__init__.py` first and crash with `ModuleNotFoundError: homeassistant`.

We work around this by pre-registering empty placeholder packages in
`sys.modules` for `custom_components` and `custom_components.duux` before
duux_api.py gets imported. When duux_api.py then does
`from .const import ...`, Python resolves it against our placeholder's
`__path__` (which points at the real folder) and never touches the real
`__init__.py`.

This trick does NOT work for select.py / switch.py / sensor.py etc.,
since those import `homeassistant.components....` directly inside the
file itself, not just via the package's `__init__.py`.
"""

import sys
import types
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DUUX_DIR = REPO_ROOT / "custom_components" / "duux"


def _register_stub_package(name: str, path: Path) -> None:
    if name in sys.modules:
        return
    module = types.ModuleType(name)
    module.__path__ = [str(path)]
    sys.modules[name] = module


_register_stub_package("custom_components", REPO_ROOT / "custom_components")
_register_stub_package("custom_components.duux", DUUX_DIR)