#Names: Robert Schreibman & Robinson Merillat
#Date:
#Class: csci250 - Sensors
#Description:

# import smbus
import time
from time import sleep
import RPi.GPIO as GPIO
import math

pin20 = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin20,GPIO.IN)

# Get I2C bus - initial bus to channel 1
# bus = smbus.SMBus(1)
flag = 0
firstvalue = 9
try:
    while True:
        value = GPIO.input(pin20)
        print(value)
        if flag == 0:
            flag = 1
            firstvalue = GPIO.input(pin20)
        if value != firstvalue:
            break


#capture the control c and exit cleanly
except(KeyboardInterrupt, SystemExit):
    print("User requested exit... bye!")
