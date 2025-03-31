from homeassistant.components.select import SelectEntity
from .const import DOMAIN

CONTROL_OPTIONS = ["Off", "Paused", "Charging"]

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([HuaweiChargingControlSelect(entry.entry_id)], True)

class HuaweiChargingControlSelect(SelectEntity):
    def __init__(self, entry_id):
        self._attr_name = "Charging Control"
        self._attr_options = CONTROL_OPTIONS
        self._attr_unique_id = f"{entry_id}_chargingControl"
        self._current_option = CONTROL_OPTIONS[0]

    @property
    def current_option(self):
        return self._current_option

    async def async_select_option(self, option: str):
        self._current_option = option

    async def async_update(self):
        self._current_option = "Charging"
