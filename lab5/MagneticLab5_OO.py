#Author: Robert Schreibman
#Date: 3/8/18
#Description: Magnetic Sensor

#import the GPIO and time libraries
import RPi.GPIO as GPIO
import time
from time import sleep

class Speedometer():
   def calculateSpeed(self, radius_cm):
      self.speedMPS = 2*3.14159*radius_cm / self.elapsedTime
   def __init__(self):
      self.elapsedTime = 0.0
      self.startTime = time.time()
      self.speedMPS = 0
      self.totalDistance = 0
      self.pulseCount = 0
   def __call__(self,channel):
      self.pulseCount += 1
      self.elapsedTime = time.time() - self.startTime
      self.calculateSpeed(2)
      self.totalDistance += self.speedMPS*self.elapsedTime
      self.printData()
      self.startTime = time.time()
   def printData(self):
      print("Elapsed Time:",self.elapsedTime)
      print("Start Time:",self.startTime)
      print("Total Distance:",self.totalDistance)
      print("Pulse Count:",self.pulseCount)
      print("SpeedMPS:",self.speedMPS)
   # def __repr__(self):
   #    self.printData()

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
    speedometer = Speedometer()
    readSensor = GPIO.add_event_detect(sensor,GPIO.FALLING,callback=speedometer, bouncetime = 25)
    count = 0
    while True:
        #capture and print the input from the reed switch using GPIO.input
        readSensor = GPIO.input(sensor)
        count +=1
        # speedometer.calculateSpeed(2)
        # print(speedometer)
        # speedometer(sensor)
        # speedometer.printData()
        # print(readSensor, " ",count)
        if (readSensor == 1):       # if the captured input is 1, then pull a LED high (True)
            GPIO.output(LED, True)

            sleep(.2)
        else:                       # otherwise, pull a LED low (False)
            GPIO.output(LED, False)
            #sleep for a bit, just to slow things down, how long is up to you
            sleep(.2)



#capture the control c and exit cleanly
except(KeyboardInterrupt, SystemExit):
   print("User requested exit... bye!")
   GPIO.cleanup()
