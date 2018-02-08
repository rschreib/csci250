from __future__ import division
import spidev

def bitstring(n): 
    s = bin(n)[2:]
    return '0'*(8-len(s)) + s #8bit

def read(adc_channel):
    spi_channel=0 #default channel is 0
    spi = spidev.SpiDev()
    spi.open(adc_channel, spi_channel)
    spi.max_speed_hz = 1000000 # 1.0 MHz (feel free to change this value to adjust speed at which inputs are read).
    cmd = 128
    if adc_channel:
        cmd += 32
    reply_bytes = spi.xfer2([cmd, 0])
    reply_bitstring = ''.join(bitstring(n) for n in reply_bytes)
    reply = reply_bitstring[5:15]
    return int(reply, 2) / 2**10
