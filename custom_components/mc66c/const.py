"""Constants for component."""
from datetime import timedelta
from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass

DOMAIN = "mc66c"

DEFAULT_NAME = "mc66c"
DEFAULT_SCAN_INTERVAL = timedelta(seconds=30)

# See page 9 in 5511- 634 GB Rev C1.qxd.pdf -  1.4. Display function.
# Format: data position, name, unit, icon.
SENSOR_TYPES = {
    "energy": [0, "Energy", "GJ", "mdi:radiator", SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING],
    "volume": [1, "Volume", "M3", "mdi:water", None, SensorStateClass.TOTAL_INCREASING],
    "op_hrs": [2, "Operating hours", "hrs", "mdi:timer-sand", SensorDeviceClass.DURATION, SensorStateClass.TOTAL_INCREASING],
    "temperature_in": [3, "Temperature in", "°C", "mdi:coolant-temperature", SensorDeviceClass.TEMPERATURE, SensorStateClass.MEASUREMENT],
    "temperature_out": [4, "Temperature out", "°C", "mdi:coolant-temperature", SensorDeviceClass.TEMPERATURE, SensorStateClass.MEASUREMENT],
    "temperature_diff": [5, "Temperature difference", "°C", "mdi:coolant-temperature", SensorDeviceClass.TEMPERATURE, SensorStateClass.MEASUREMENT],
    "power": [6, "Power", "kW", "mdi:flash", SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT],
    "flow": [7, "Flow", "l/h", "mdi:water", None, SensorStateClass.MEASUREMENT],
    "peak_power": [8, "Peak power", "kWp", "mdi:flash", SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT],
    "info_code": [9, "Info code", "", "mdi:alert-outline", None, None],
}
