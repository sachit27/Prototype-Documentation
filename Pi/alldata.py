import bme680
import time
from datetime import datetime
from pms5003 import PMS5003, ReadTimeoutError

print("""print all the sensor data
Press Ctrl+C to exit!
""")
# BME280 temperature/pressure/humidity sensor
bme280 = BME280()

# PMS5003 particulate sensor
pms5003 = PMS5003()

# Create a values dict to store the data
variables = ["temperature",
             "pressure",
             "humidity",
             "pm1",
             "pm25",
             "pm10"]

values = {}

for v in variables:
    values[v] = [1] * WIDTH

try:
    while True:
        
            if mode == 0:
                variable = "temperature"
                unit = "C"
                data = bme280.get_temperature()
                display_text(variable, data, unit)

            if mode == 1:
                variable = "pressure"
                unit = "hPa"
                data = bme280.get_pressure()
                display_text(variable, data, unit)

            if mode == 2:
                variable = "humidity"
                unit = "%"
                data = bme280.get_humidity()
                display_text(variable, data, unit)
                
            if mode == 3:
                variable = "pm1"
                unit = "ug/m3"
                data = pms5003.read()
                data = data.pm_ug_per_m3(1.0)
                display_text(variable, data, unit)

            if mode == 4:
                variable = "pm25"
                unit = "ug/m3"
                data = pms5003.read()
                data = data.pm_ug_per_m3(2.5)
                display_text(variable, data, unit)

            if mode == 5:
                variable = "pm10"
                unit = "ug/m3"
                data = pms5003.read()
                data = data.pm_ug_per_m3(10)
                display_text(variable, data, unit)            
    
except KeyboardInterrupt:
    sys.exit(0)
