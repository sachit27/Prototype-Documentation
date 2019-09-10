Instructions for setting up DHT22 (Temperature and Humidity sensor) with Raspberry Pi Zero

Parts Needed:
1. A Raspberry Pi Zero that is connected to the internet.

2. DHT22 sensor.

3. A resistor. We have used 1k Ohm resistor. But it has been suggested that you can use either a 4.7k Ohm resistor or a 10k Ohm resistor as well.

4. Jumper cables to connect the parts.

5. A breadboard, which may make it easier to connect the parts. 

-Wiring:

Wire the sensor as shown in the following picture. The first sensor pin is 3V-5V, the second is bidirectional serial data, the third is not used and the fourth is ground. The resistor is used as a pull-up resistor. 

The figure shows how the connection looks like:
![alt text](https://github.com/sachit27/Prototype-Documentation/blob/master/figures/9.png)

-How to get temperature and humidity

-Log in to the Pi using Terminal by running: ssh pi@AirKit2.local 

-Run sudo apt-get update and sudo apt-get upgrade -y to ensure your system is up to date. 

-Correct the timezone by checking if it is correct. It can be done using date.  To set the correct timezone, use sudo raspi-config. 

-Install setup tools for python by using this command 
        
                                sudo apt-get -y install python-setuptools python-dev build-essential

-To communicate with the sensor, the Adafruit_Python_DHT library is used. It talks to the GPIO pins. To install it, get the dependencies with 
                  
                              sudo apt-get install -y build-essential python-dev git 
                              
  and then download and install the library with
	
                              mkdir -p /home/pi/sources
	
                              cd /home/pi/sources

                              git clone https://github.com/adafruit/Adafruit_Python_DHT.git
                              
                              cd Adafruit_Python_DHT

                              sudo python setup.py install

-To get temperature and humidity, use this command

                              sudo /home/pi/sources/Adafruit_Python_DHT/examples/AdafruitDHT.py 22 4

The first argument is the sensor type, it can be 11 or 22 or other type of sensor. The second argument is the RPi GPIO pin which is connected to the sensor data pin.

The result looks like this
![alt text](https://github.com/sachit27/Prototype-Documentation/blob/master/figures/10.png)
