import sys
import smbus
import time
import urllib2
import time
import datetime
import csv
from time import sleep

myAPI = 'RD062717YDOGPJ3D'
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 
# Get I2C bus
bus = smbus.SMBus(1)
time.sleep(2)

bus.write_i2c_block_data(0x44, 0x2C, [0x06])

time.sleep(2)

data = bus.read_i2c_block_data(0x44, 0x00, 6)
 
# Convert the data
temp = data[0] * 256 + data[1]
cTemp = -45 + (175 * temp / 65535.0)
fTemp = -49 + (315 * temp / 65535.0)
humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

def get_temp():
    temperature =str(cTemp)
    return(temperature)

def get_humidity():
    Humidity = str(humidity)
    return(Humidity)
#print ("Temperature in Celsius is : %.2f C" %cTemp)
#print ("Relative Humidity is : %.2f %%RH" %humidity)
conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s' % (get_temp(),get_humidity()))
print conn.read()
                        # Closing the connection
conn.close()



