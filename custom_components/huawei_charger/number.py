from homeassistant.components.number import NumberEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([HuaweiMaxPowerNumber(entry.entry_id)], True)

class HuaweiMaxPowerNumber(NumberEntity):
    def __init__(self, entry_id):
        self._attr_name = "Max Charging Power"
        self._attr_native_min_value = 0
        self._attr_native_max_value = 22
        self._attr_native_step = 1
        self._attr_native_unit_of_measurement = "kW"
        self._attr_unique_id = f"{entry_id}_maxChargingPower"
        self._value = 0

    @property
    def native_value(self):
        return self._value

    async def async_set_native_value(self, value: float):
        self._value = value

    async def async_update(self):
        self._value = 11
