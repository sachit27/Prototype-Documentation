import bme680
import time
From datetime import datetime
print("""temperature-pressure-humidity.py - Displays temperature, pressure, and humidity.
If you don't need gas readings, then you can read temperature,
pressure and humidity quickly.
Press Ctrl+C to exit
""")
try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

print('Polling:')
try:
    while True:
        if sensor.get_sensor_data():
            output = datetime.now().strftime('%Y-%m-%d,%H:%M:%S,')+
'{0:.2f} C,{1:.2f} hPa,{2:.3f} %RH'.format(
                sensor.data.temperature,
                sensor.data.pressure,
                sensor.data.humidity)
            print(output)
		sleep.time(60)	
except KeyboardInterrupt:
    pass
