from homeassistant.components.sensor import SensorEntity
from homeassistant.const import UnitOfElectricPotential, UnitOfElectricCurrent, UnitOfPower
from .const import DOMAIN

SENSOR_TYPES = {
    "phaseL1_voltage": ("Phase L1 Voltage", UnitOfElectricPotential.VOLT),
    "phaseL2_voltage": ("Phase L2 Voltage", UnitOfElectricPotential.VOLT),
    "phaseL3_voltage": ("Phase L3 Voltage", UnitOfElectricPotential.VOLT),
    "phaseL1_current": ("Phase L1 Current", UnitOfElectricCurrent.AMPERE),
    "phaseL2_current": ("Phase L2 Current", UnitOfElectricCurrent.AMPERE),
    "phaseL3_current": ("Phase L3 Current", UnitOfElectricCurrent.AMPERE),
    "totalPower": ("Total Power", UnitOfPower.KILO_WATT),
    "combined_voltage": ("Combined Voltage", UnitOfElectricPotential.VOLT),
    "combined_current": ("Combined Current", UnitOfElectricCurrent.AMPERE)
}

async def async_setup_entry(hass, entry, async_add_entities):
    sensors = []
    for sensor_type, (name, unit) in SENSOR_TYPES.items():
        sensors.append(HuaweiChargerSensor(entry.entry_id, sensor_type, name, unit))
    async_add_entities(sensors, True)


class HuaweiChargerSensor(SensorEntity):
    def __init__(self, entry_id, sensor_type, name, unit):
        self._attr_name = name
        self._attr_native_unit_of_measurement = unit
        self._attr_unique_id = f"{entry_id}_{sensor_type}"
        self._sensor_type = sensor_type
        self._state = None

    @property
    def native_value(self):
        return self._state

    async def async_update(self):
        self._state = 0  # Replace with actual value later
