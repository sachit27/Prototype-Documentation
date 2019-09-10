import sys
import urllib2
import bme680
import time
import datetime
import csv
from time import sleep
from bme680 import BME680
from pms5003 import PMS5003, ReadTimeoutError

myAPI = '74599RU6EKNNO8XJ' #Change the code for using it for different accounts
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.
pms5003 = PMS5003()
readings = pms5003.read()
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

def get_temp():
    temperature = sensor.get_sensor_data()
    temperature = sensor.data.temperature
    temperature = round((temperature),2)
    temperature = temperature -2
    temperature = str(temperature)
    return(temperature)

def get_temp():
    temperature = sensor.get_sensor_data()
    temperature = sensor.data.temperature
    temperature = round((temperature),2)
    temperature = temperature -2
    temperature = str(temperature)
    return(temperature)

def get_pressure():
    pressure = sensor.get_sensor_data()
    pressure = sensor.data.pressure
    pressure = str(pressure)
    return(pressure)
    
def get_humidity():
    humidity = sensor.get_sensor_data()
    humidity = sensor.data.humidity
    humidity = str(humidity)
    return(humidity)

def get_pm1():
    variable = "pm1"
    unit = "ug/m3"
    data = pms5003.read()
    data = data.pm_ug_per_m3(1.0)
    return(data)

def get_pm25():
    variable = "pm25"
    unit = "ug/m3"
    data = pms5003.read()
    data = data.pm_ug_per_m3(2.5)
    return(data)

def get_pm10():
    variable = "pm10"
    unit = "ug/m3"
    data = pms5003.read()
    data = data.pm_ug_per_m3(10)
    return(data)

def date_now():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    today = str(today)
    return(today)

def time_now():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    now = str(now)
    return(now)

conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s' % (get_temp(),get_pressure(), get_humidity(), get_pm1(), get_pm25(), get_pm10()))
print conn.read()
                        # Closing the connection
conn.close()
