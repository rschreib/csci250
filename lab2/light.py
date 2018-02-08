#Author: Robert Schreibman
#Date: 2-1-18
#csci250 - Sensors
#Lab2

#Description: This code will receive light readings from the mini photocell transducer
# and store 500 readings into a numpy array, then store the array into a dictionary, and finally
# graph the numpy array elements

#Extra Credit:
#1)     Each element is multiplied by 100 and rounded down to 2 decimal places (so 33.33333 will be 33.33)
#       and then converted to a string, diplayed using json library and dumps function
#2)     Data is Graphed
#3)     Program is Interfaced with a button so the program will not read sensor values unless the button
#       is pressed. Green LED displays while program is running, Red LED displays otherwise

#Must exit out of Graph display before pressing the Button Again

import numpy as n
from time import sleep
import spidev
import reader
import json
import matplotlib.pyplot as p
import RPi.GPIO as GPIO		#controls General Purpose I/O pins
import time as t		#contains sleep command

adc_channel = 0
spi_channel = 0

#we will just be calling the defined read function with a zero: (e.g., read(0)) for our lab
spi = spidev.SpiDev()                   #initiate spi object
spi.open(adc_channel, spi_channel)      #adc channel=0 (can use 1) and spi channel=0
spi.max_speed_hz = 1000000              #is 1 MHz can change the value but this worked best

pin18 = 18      #Button (input signal)
pin19 = 19      #Green LED (output signal)
pin20 = 20      #Red LED (output signal)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin18,GPIO.IN)       
GPIO.setup(pin19,GPIO.OUT)
GPIO.setup(pin20,GPIO.OUT)

def program():                        
        arr = []
        for i in range(500):    #loop 500 times
                sleep(.001)     #sleep .001s in between light readings
                x = reader.read(0)
                arr.append(x)   #append to list
                print("Reading {}".format(i))

        nArray = n.array(arr)   #store data elements into numpy array
        
        stringArr = {}          #creates the dictionary using a key and value                        
        for i in range(len(nArray)):
                key = "Reading " + str(i)
                value = "%.2f" % (nArray[i]*100) + "%"
                stringArr[key] = value

                                #Displays the dictionary alphabetically (not numerically)
        print(json.dumps(stringArr, sort_keys=True, indent=4))

        x = range(len(nArray))
        y = nArray              #nArray values are still in order
        p.plot(x,y)
        p.show()        

try:
        while True:
                                #Button pressed  
                if GPIO.input(pin18) == True:   
                        GPIO.output(pin19,True)
                        GPIO.output(pin20,False)
                        program()
                        GPIO.output(pin19,False)

                                #Button not pressed
                elif GPIO.input(pin18) == False:
                        GPIO.output(pin19,False)
                        GPIO.output(pin20,True)


except(KeyboardInterrupt, SystemExit):
	print("User requested exit... shutting down now")

finally:
	GPIO.cleanup()



