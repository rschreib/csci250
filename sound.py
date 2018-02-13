#Author: Robert Schreibman
#Date: 2-8-18
#Description:
#Think Exercise Answers: a1, a2, a3, and c1

#Questions
#a1) At what clock value is data transmitted? (0-falling or 1-rising?)
    # 0-falling edge of clock
#a2) At what clock value is data received? (0-falling or 1-rising?)
    # 1-rising edge of clock
#a3) How many bytes are transmitted/received? (recall 1 byte = 8 bits)
    # 2 bytes are transmitted (only uses 10 bits though)

#import libraries:
from time import sleep          #time to use the sleep command
import numpy	                #numpy for arrays
import spidev                   #spidev as spi for working with the ADC
#import reader                   #ADC reader code ... inline vs. included library
#import json
import matplotlib.pyplot as p
import RPi.GPIO as GPIO		#controls General Purpose I/O pins

spi = spidev.SpiDev() #create spidev object
spi.open(0,0) #(port, channel)
spi.max_speed_hz = 1000000 #optional, use so you dont overwork RPi

pin18 = 18      #Button (input signal)
pin19 = 19      #Green LED (output signal)
pin20 = 20      #Red LED (output signal)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin18,GPIO.IN)       
GPIO.setup(pin19,GPIO.OUT)
GPIO.setup(pin20,GPIO.OUT)

def readAdc(channel):
    #You may use the incoming parameter to make more flexible later
    #Read the raw data for channel 0 using the xfer2 method, which
    #sends AND receives depending on the clock rise/fall.
    r = spi.xfer2([int('01100000',2), 15])

    #Get data
    #get 10 bit bitstring from r[0]
    s = bin(r[0])[2:].zfill(10)
    #append 8 '0's to last 2 bits from r[0]
    data = int(s[8:] + '0'*8, 2) + r[1]
    return data

try:  
	while True:
		x = readAdc(0)
		print(x)
	
except(KeyboardInterrupt, SystemExit):
	print("User requested exit... shutting down now")

finally:
	GPIO.cleanup()
