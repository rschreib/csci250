#Author: Robert Schreibman
#Date: 1-31-18
#CSCI250 - Sensors
#Lab 1
#Description: This will make an LED connected to general purpose pin 25 blink

#Import Libraries
import RPi.GPIO as GPIO		#controls General Purpose I/O pins
import time as t		#contains sleep command

#These are good names because they describe what those numbers represent
#This makes code easier to read and understand
pin25 = 25
pin24 = 24
sleeptime = 0.2

GPIO.setmode(GPIO.BCM)		#set pin mode to use numbers from the board
GPIO.setup(pin25,GPIO.OUT)	#set pin number to be an output pin direction
GPIO.setup(pin24,GPIO.IN)

#blink - pull high, True, 3.3V OR low, Flase, 0V

def blinkmode():
	GPIO.output(pin25,True)
	t.sleep(sleeptime)
	GPIO.output(pin25,False)
	t.sleep(sleeptime)
def offmode():
	GPIO.output(pin25, False)
	t.sleep(sleeptime)

try:
	while True:
		while GPIO.input(pin24) == True:	
			blinkmode()
		while GPIO.input(pin24) == False:
			offmode()
		
except(KeyboardInterrupt, SystemExit):
	print("User requested exit... shutting down now")

finally:
	GPIO.cleanup()
