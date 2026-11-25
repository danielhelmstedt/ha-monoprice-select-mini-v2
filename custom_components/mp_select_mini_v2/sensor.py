import logging
import re

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import UnitOfTemperature
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    sensors = [
        MPSelectMiniV2Sensor(coordinator, entry.entry_id, "Extruder Temperature", "temperature"),
        MPSelectMiniV2Sensor(coordinator, entry.entry_id, "Extruder Target", "temperature"),
        MPSelectMiniV2Sensor(coordinator, entry.entry_id, "Bed Temperature", "temperature"),
        MPSelectMiniV2Sensor(coordinator, entry.entry_id, "Bed Target", "temperature"),
        MPSelectMiniV2Sensor(coordinator, entry.entry_id, "Printer Status", "enum"),
        MPSelectMiniV2Sensor(coordinator, entry.entry_id, "Printer Progress", None),
    ]
    async_add_entities(sensors)

class MPSelectMiniV2Sensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, entry_id, name, device_class):
        super().__init__(coordinator)
        self._entry_id = entry_id
        self._name = name
        self._device_class = device_class

    @property
    def unique_id(self):
        return f"{self._entry_id}_{self._name}"

    @property
    def name(self):
        return self._name

    @property
    def native_value(self):
        if self.coordinator.data is None:
            return None
        return self.parse_response(self.coordinator.data)
    
    @property
    def device_class(self):
        return self._device_class
    
    @property
    def native_unit_of_measurement(self):
        if self._device_class == "temperature":
            return UnitOfTemperature.CELSIUS
    
    @property
    def options(self):
        """Return the list of available options for the Printer Status sensor."""
        if self._name == "Printer Status":
            return ["Idle", "Printing", "Unknown"]

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._entry_id)},
            "name": "Monoprice Select Mini V2",
            "manufacturer": "Monoprice",
            "model": "Select Mini V2",
        }

    @property
    def available(self):
        return self.coordinator.last_update_success

    def parse_response(self, data):
        if not data:
            return None

        values = re.findall(r"\d+", data)
        if self._name == "Extruder Temperature":
            value_index = 0
        elif self._name == "Extruder Target":
            value_index = 1
        elif self._name == "Bed Temperature":
            value_index = 2
        elif self._name == "Bed Target":
            value_index = 3
        elif self._name == "Printer Status":
            c = data[-1]
            return "Idle" if c == 'I' else "Printing" if c == 'P' else "Unknown"
        elif self._name == "Printer Progress":
            c = data[-1]
            if c != "P":
                return "Idle"
            value_index = 4
        else:
            return None

        if len(values) <= value_index:
            _LOGGER.warning("Missing data parsing %s from printer response", self._name)
            return None
        return values[value_index]