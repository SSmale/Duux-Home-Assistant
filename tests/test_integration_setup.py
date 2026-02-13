from unittest.mock import patch

import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.duux import const


@pytest.mark.asyncio
async def test_async_setup_entry_creates_coordinators(
    hass, devices_fixture, monkeypatch
):
    """Integration setup should create coordinators and store devices in hass.data."""
    # Patch DuuxAPI.login and get_devices to return our fixtures
    with (
        patch("custom_components.duux.duux_api.DuuxAPI.login", return_value=True),
        patch(
            "custom_components.duux.duux_api.DuuxAPI.get_devices",
            return_value=devices_fixture,
        ),
    ):
        entry = MockConfigEntry(
            domain=const.DOMAIN, data={"email": "x", "password": "y"}
        )
        entry.add_to_hass(hass)

        # Trigger config entry setup (this calls async_setup_entry)
        assert await hass.config_entries.async_setup(entry.entry_id)
        await hass.async_block_till_done()

        # hass.data should be populated
        assert const.DOMAIN in hass.data
        assert entry.entry_id in hass.data[const.DOMAIN]
        data = hass.data[const.DOMAIN][entry.entry_id]
        assert "devices" in data
        assert "coordinators" in data
        assert len(data["devices"]) == len(devices_fixture)


# import asyncio
# from unittest.mock import patch, AsyncMock

# import pytest
# from pytest_homeassistant_custom_component.common import MockConfigEntry

# from custom_components.duux import const


# @pytest.mark.asyncio
# async def test_async_setup_entry_creates_coordinators(
#     hass, devices_fixture, monkeypatch
# ):
#     """Integration setup should create coordinators and store devices in hass.data."""
#     # Patch DuuxAPI.login and get_devices to return our fixtures
#     with (
#         patch("custom_components.duux.duux_api.DuuxAPI.login", return_value=True),
#         patch(
#             "custom_components.duux.duux_api.DuuxAPI.get_devices",
#             return_value=devices_fixture,
#         ),
#         patch.object(
#             hass.config_entries,
#             "async_forward_entry_setups",
#             new=AsyncMock(return_value=None),
#         ),
#     ):
#         entry = MockConfigEntry(
#             domain=const.DOMAIN, data={"email": "x", "password": "y"}
#         )
#         entry.add_to_hass(hass)

#         # Trigger config entry setup (this calls async_setup_entry)
#         result = await hass.config_entries.async_setup(entry.entry_id)
#         await hass.async_block_till_done()

#         assert result is True

#         # hass.data should be populated
#         assert const.DOMAIN in hass.data
#         assert entry.entry_id in hass.data[const.DOMAIN]
#         data = hass.data[const.DOMAIN][entry.entry_id]
#         assert "devices" in data
#         assert "coordinators" in data
#         assert len(data["devices"]) == len(devices_fixture)
