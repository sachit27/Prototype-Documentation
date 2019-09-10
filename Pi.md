Step by step instruction for Pi Prototype

Setting up The RPZW Headless

1. We are setting up the RPZW in headless mode which means that we don’t require any peripheral devices (screen, keyboard, mouse etc.). For this we need:

  Rasberry Pi Zero W 
  USB cable
  SD card > 4GB
  Laptop with SD card reader
  Access to a WLAN

2. Flash the SD Card

Download the Raspbian Buster Lite image as a zip file from this website: https://www.raspberrypi.org/downloads/raspbian/
Download and install balenaEtcher from: https://www.balena.io/etcher/ 
Connect a blank SD card to your computer and open the balenaEtcher app.
It will take a few minutes to flash the drive. Once it is complete you will need to take the SD card out of your SD card reader and then reinsert it. You will notice that the SD card is now called ‘boot’ and will contain files that look a bit like this.

3.Enable SSH

You can access the command line of a Raspberry Pi remotely from another computer or device on the same network using SSH.
This is not enabled by default on the RPZW so we have to create a file to enable it. We just need to add a file ‘ssh’ no extensions to the SD card.
On Mac OS or Linux
Go to the Terminal application
Write this command and press enter.
  
  touch /Volumes/boot/ssh

It will create a file called ssh in the ‘boot’ directory.

4. On Mac OS or Linux, Go to the Terminal application
  Write this command and press enter.
  
  touch /Volumes/boot/wpa_supplicant.conf
  
Navigate to the ‘boot’ directory and open the wpa_supplicant.conf file you have created in a text editor (we used Atom). Copy and paste the following text with some adjustment. Change ssid to your network name

5. On Mac, Open up a terminal window and run the following commands.
  
  ssh-keygen -R raspberrypi.local
  
  ssh pi@raspberrypi.local
  

The first command just clears out any references to raspberrypi.local so don’t worry if you get an error.
The last command initialises SSH between your computer and the Pi. You will need to confirm that you want to connect with it by entering yes and pressing return.
You now need to type in the password for the RPZW this is raspberry as default. If you see the pi@raspberrypi: ~ $ you are now able to connect with the RPZW through the command line.
