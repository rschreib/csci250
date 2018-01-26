#Author: Robert Schreibman	
#Date:	1/25/18
#Description: Lab 1
#This makes pin25 Blink

#import library to control the general purpose I/O pins and use short name
import RPi.GPIO	as GPIO

#import the time library to use	the sleep command
import time

#using name Gpin tells us that this references a general purpose pin
#using name sleeptime tells us this is how long the led will sleep for
Gpin=24
sleeptime=1

#set the pin mode to use the numbers from the board
GPIO.setmode(GPIO.BCM)

#set the pin number 25 to be an output pin, direction
GPIO.setup(Gpin,GPIO.OUT)

#blink	- pull high, True, 3.3V OR low, False, 0 Volts
#NOTE:	you can use control C to kill your  program for or  see slides for hints on a cleaner way to exit

try:
    while True:
        GPIO.output(Gpin,True)
        time.sleep(sleeptime)
        GPIO.output(Gpin,False)
        time.sleep(sleeptime)
        
except(KeyboardInterrupt, SystemExit):
    print("User requested exit... shutting down now")

finally:
    GPIO.cleanup()


    
    #Author: Robert Schreibman	
#Date:	1/25/18
#Description: Lab 1
#This makes pin25 Blink

#import	library	to control the general purpose I/O pins	and use	short name
import RPi.GPIO	as GPIO

#import	the time library to use	the sleep command
import time

#using name Gpin tells us that this references a general purpose pin
#using name sleeptime tells us this is how long the led will sleep for
Gpin=25
sleeptime=1

#set the pin mode to use the numbers from the board
GPIO.setmode(GPIO.BCM)

#set the pin number 25 to be an output pin, direction
GPIO.setup(Gpin,GPIO.OUT)

#blink	- pull high, True, 3.3V OR low,	False, 0 Volts
#NOTE:	you can use control C to kill your  program for or  see	slides	for hints on a cleaner way to exit

try:
    while True:
        GPIO.output(Gpin,True)
        time.sleep(sleeptime)
        GPIO.output(Gpin,False)
        time.sleep(sleeptime)
        
except(KeyboardInterrupt, SystemExit):
    print("User requested exit... shutting down now")


finally:
    GPIO.cleanup()


    
    
