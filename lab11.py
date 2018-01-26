#Robert Schreibman


import RPi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)

try:
	while True:
		GPIO.output(25,True)
		t.sleep(1)
		GPIO.output(25,False)
		t.sleep(1)
#except(KeyboardInterrupt, SystemExit):
#	print("User requested exit... shutting down now")

finally:
	GPIO.cleanup()

