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
#c1) Max Value for 10 bits is 2^10 - 1 = 1023

#import libraries:
import numpy as np              #numpy for arrays
import time		        #time to use the sleep command
import spidev                   #spidev as spi for working with the ADC
import RPi.GPIO as GPIO		#controls General Purpose I/O pins

buzzerPin = 19      #(output signal)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin,GPIO.OUT)

spi = spidev.SpiDev() #create spidev object
spi.open(0,0) #(port, channel)
spi.max_speed_hz = 1000000 #optional, use so you dont overwork RPi

#Buzz function is provided (uses half period method)
#This code is derived from basics physics of how sound works but to save time
#we googled those calculations.
def buzz(pitch, duration):
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)
    for i in range(cycles):
        GPIO.output(buzzerPin, True)
        time.sleep(delay)
        GPIO.output(buzzerPin, False)
        time.sleep(delay)
        time.sleep(duration * 0.3)

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

data = np.loadtxt("song.txt")
print(data)
pitches = np.int_(data[:,0])
print(pitches)

while True:
    x = readAdc(0)
    print(x)
    for val1, val2 in zip(pitches,data[:,1]):
        buzz(val1, val2)

    buzz(500,.2)



