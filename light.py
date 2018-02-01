#Robert Schreibman
#csci250 - Sensors
#Lab2

import numpy as n
from time import sleep
import spidev
import reader

adc_channel = 0
spi_channel = 0
arr = []


spi = spidev.SpiDev()
spi.open(adc_channel, spi_channel)
spi.max_speed_hz = 1000000

for i in range(1,500):
	sleep(.001)
	x = reader.read(0)
	#print(x)
	arr.append(x)

print(arr)




