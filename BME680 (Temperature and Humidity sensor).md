The first step is to solder the BME680 to the breakout.

There is a piece of right-angle female header that you can solder on and then pop the breakout right onto pins 1, 3, 5, 7, and 9 of your Raspberry Pi.

Changing the default I2C address

The breakout has a default I2C address of 0x76, but this can be changed so that you can use up to two breakouts on the same Raspberry Pi or Arduino. To change the I2C address to 0x77, simply flow a small blob of solder across the two solder pads so that it bridges the pads. If you decide to change it back at a later date, then you can use a solder sucker or some solder braid to remove the solder and un-bridge the pads.

You'll need to have I2C enabled on your Raspberry Pi. You can do this in the Interfaces section of the Raspberry Pi Configuration menu, by typing sudo raspi-config in the terminal.

-Libraries to install:
The Adafruit library for the GPIO lines is required by the Adafruit BME680 library to access I2C bus. It is advisable to install also some packages from the Raspbian distro, otherwise the python setup will try to download and install a local version:
  
  sudo apt-get install python-dev python-setuptools python-spidev

The Adafruit Python library is installed from the Git repository:

cd /usr/local/src/

sudo git clone https://github.com/adafruit/Adafruit_Python_GPIO.git

cd Adafruit_Python_GPIO

python setup.py install

-Required software
On the Raspberry Pi we need some extra packages containing some tools for the I2C bus:

sudo apt-get install python-smbus i2c-tools

To detect I2C device, run this command

i2cdetect -y 1

-Connecting the sensor and getting the data
Type the following to clone the repository and install it:

git clone https://github.com/pimoroni/bme680

cd bme680/library

OR
You can also use pip to install the BME680 library

sudo pip install bme680

Note: If you don’t have pip or git, please install it in the Pi before proceeding with these commands.

Adapted from: https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-bme680-breakout
https://www.rigacci.org/wiki/doku.php/doc/appunti/hardware/raspberrypi_air
