#Name: Robert Schreibman & Robinson Merillat
#Date:
#Class: csci250 - Sensors
#Description:

#Extra Credit:
#1) Created 2 methods that converts an array of objects to a string: __repr__ & myPrint(arr)
#2) Added method average(self): this averages the first 3 recorded x,y,z values for calibration
#4) Added some LEDs. The LEDs turn on when tilted in the Y-direction and will blink when tilted
#   in the X-direction.


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
        print(GPIO.input(pin20))
        if flag == 0:
            flag = 1
            firstvalue = GPIO.input(pin20)
        else:
            if GPIO.input(pin20 != firstvalue):
                break
            

        #Parameters for write_byte_data
        # #1. Address of the device
        # #2. Communication data - active mode control register
        # #3. Our data - 0 (standby mode) or 1 (active)
        # bus.write_byte_data(0x1D, 0x2A, 1)
        # time.sleep(0.5)
        #
        # #Read from the status register, real-time status register 0x00
        # #Data returned will be an array
        # #Contents of 7 bytes read and stored in data array represent:
        # #status (ignore), MSBx, LSBx, MSBy, LSBy, MSBz, LSBz
        # data = bus.read_i2c_block_data(0x1D, 0x00, 7)
        #
        # #put register in standbye mode
        # bus.write_byte_data(0x1D, 0x2A, 0)
        # # time.sleep(0.5)
        #
        # MSB_x = data[1]
        # LSB_x = data[2]
        # MSB_y = data[3]
        # LSB_y = data[4]
        # MSB_z = data[5]
        # LSB_z = data[6]
        # numberOfBits = 16
        # xAccl = (MSB_x * 256 + LSB_x) / numberOfBits
        # yAccl = (MSB_y * 256 + LSB_y) / numberOfBits
        # zAccl = (MSB_z * 256 + LSB_z) / numberOfBits
        #
        # if xAccl > 2047:
        #     xAccl -= 4096
        # if yAccl > 2047:
        #     yAccl -= 4096
        # if zAccl > 2047:
        #     zAccl -= 4096
        #print("x: ",xAccl," y: ",yAccl," z: ",zAccl)
        #print(data)

        #created class Acceleromter that stores the x, y, z coordinates
        #inside the instance point. The instance is then appended to the
        #array arr. Member functions are then called to print the data



#capture the control c and exit cleanly
except(KeyboardInterrupt, SystemExit):
    print("User requested exit... bye!")

#Sample modified from https://www.controleverything.com/content/Accelorometer?sku=MMA8452Q_I2CS#tabs-0-product_tabset-2
