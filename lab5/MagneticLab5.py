#Author: Robert Schreibman
#Date: 3/8/18
#Description: 

#import the GPIO and time libraries
import RPi.GPIO as GPIO
import time
from time import sleep

#setup two variables to hold the values for the pin numbers
#(one for LED and one for reed switch)
sensor = 20 #pin20
LED = 21 #pin21

#setup the pin mode for the GPIO 
GPIO.setmode(GPIO.BCM)


#turn off the warnings, this is optional
GPIO.setwarnings(False)

#setup the reed switch as an input pin
#we need to add as a third argument, pull_up_down=GPIO.PUD_DOWN for resistance
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

#setup the LED as an output pin
GPIO.setup(LED, GPIO.OUT)

#area for the logic to detect high/low from reed switch and light LED
try:
   while True:
      #capture and print the input from the reed switch using GPIO.input
      readSensor = GPIO.input(sensor)
      print(readSensor)
      sleep(.5)

      #if the captured input is 1, then pull a LED high (True)


      #otherwise, pull a LED low (False)


      #sleep for a bit, just to slow things down, how long is up to you

         
#capture the control c and exit cleanly
except(KeyboardInterrupt, SystemExit): 
   print("User requested exit... bye!")
   GPIO.cleanup()



