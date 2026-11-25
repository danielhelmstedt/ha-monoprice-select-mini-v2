import asyncio
import logging

import aiohttp
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)


class MPSelectMiniV2Coordinator(DataUpdateCoordinator):
    """Fetch printer data once and share it with all sensor entities."""

    def __init__(self, hass: HomeAssistant, host: str) -> None:
        self.host = host
        self._session = async_get_clientsession(hass)

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=SCAN_INTERVAL,
        )

    async def _async_update_data(self) -> str:
        url = f"http://{self.host}/inquiry"

        try:
            async with self._session.get(
                url, timeout=aiohttp.ClientTimeout(total=5)
            ) as response:
                response.raise_for_status()
                return await response.text()
        except (aiohttp.ClientError, asyncio.TimeoutError) as err:
            _LOGGER.warning("Error fetching data from printer at %s: %s", self.host, err)
            raise UpdateFailed(f"Error communicating with printer: {err}") from err
