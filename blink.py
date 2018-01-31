#Author: Robert Schreibman
#Date: 1-31-18
#CSCI250 - Sensors
#Lab 1
# Description (+ extra credit): This will make 2 LEDs connected to general purpose 
# pins 25 and 23 alternate blinking while button is not pressed. They will turn 
# off when button pressed (like an LED alarm system)

#Import Libraries
import RPi.GPIO as GPIO		#controls General Purpose I/O pins
import time as t		#contains sleep command

#These are good names because they describe what those numbers represent
#This makes code easier to read and understand
pin25 = 25			# first LED output
pin24 = 24			# Reads Button signal
pin23 = 23			# Second LED output
sleeptime = 0.2			# Blinking speed

GPIO.setmode(GPIO.BCM)		#set pin mode to use numbers from the board
GPIO.setup(pin25,GPIO.OUT)	#set pin number to be an output pin direction
GPIO.setup(pin24,GPIO.IN)	
GPIO.setup(pin23,GPIO.OUT)

#blink - pull high, True, 3.3V OR low, Flase, 0V

def slowblinkmode():
	GPIO.output(pin25,True)
	GPIO.output(pin23,False)
	t.sleep(slowsleeptime)
	GPIO.output(pin25,False)
	GPIO.output(pin23,True)
	t.sleep(slowsleeptime)

def blinkmode():
	GPIO.output(pin25,True)
	GPIO.output(pin23,False)
	t.sleep(sleeptime)
	GPIO.output(pin25,False)
	GPIO.output(pin23,True)
	t.sleep(sleeptime)

def offmode():
	GPIO.output(pin25, False)
	GPIO.output(pin23, False)

def doNothing():
	offmode()

try:
	while True:
		if GPIO.input(pin24) == False:	
			print("Blink Mode")
			blinkmode()
		if GPIO.input(pin24) == True:
			print("Off")
			offmode()

<<<<<<< HEAD
# The code below will recognize button presses and enter 3 different
# modes of LED light blinking. The LEDs connected to pin23 and pin25 alternate blinking.
'''
try:
	while True:
		while GPIO.input(pin24) == True:
			doNothin()
		while GPIO.input(pin24) == False:	
			slowblinkmode()

		while GPIO.input(pin24) == True:
			doNothing()
		while GPIO.input(pin24) == False:
			blinkmode()
=======
>>>>>>> 0bffafdfaa4186813fd0528b134fea2c3ba89446
		
		while GPIO.input(pin24) == True:
			doNothing()
		while GPIO.input(pin24) == False:
			offmode()

'''
except(KeyboardInterrupt, SystemExit):
	print("User requested exit... shutting down now")

finally:
	GPIO.cleanup()
