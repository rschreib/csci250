#Name: Wendy Fisher (TA: Benjamin Tarman)
#Date: Feb 22, 2018
#Description: This sample file is for Lab4 - and intended as a bare-bones structure to
#       work with the I2C and the accelerometer. Once the device is wired and RPi
#       running, this code should work as is. Students are tasked to modify this
#       code to an object-oriented solution for credit.
import smbus 
import time

# Get I2C bus - initial bus to channel 1
bus = smbus.SMBus(1) 
#class Accelerometer():



try:
    while True:
        #Parameters for write_byte_data
        #1. Address of the device
        #2. Communication data - active mode control register
        #3. Our data - 0 (standby mode) or 1 (active)
        bus.write_byte_data(0x1D, 0x2A, 1) 
        time.sleep(0.5)

        #Read from the status register, real-time status register 0x00
        #Data returned will be an array
        #Contents of 7 bytes read and stored in data array represent:
        #status (ignore), MSBx, LSBx, MSBy, LSBy, MSBz, LSBz
        data = bus.read_i2c_block_data(0x1D, 0x00, 7)     

		
        #put register in standbye mode
        bus.write_byte_data(0x1D, 0x2A, 0) 
        time.sleep(0.5)

        print(data)
		
		#MSB_x = data[1]
		#LSB_x = data[2]
		#numberOfBits = 16
		#xAccl = (MSB_x * 256 + LSB_x) / numberOfBits
		#if xAccl > 2047:
		#	xAccl -= 4096
		

#capture the control c and exit cleanly
except(KeyboardInterrupt, SystemExit): 
    print("User requested exit... bye!")
    
#Sample modified from https://www.controleverything.com/content/Accelorometer?sku=MMA8452Q_I2CS#tabs-0-product_tabset-2
