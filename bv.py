import os
import spidev
import time

Vref = 5.0

file = os.path.abspath("/dev/rfcomm0")

fileobj = open(file, "w")

while True:

    ch0 = [0x06,0x00,0x00]

    spi = spidev.SpiDev()
    spi.open(0,0) #bus 0,cs 0
    spi.max_speed_hz = 1000000 # 1MHz

    adc = spi.xfer2(ch0)
    data = ((adc[1] & 0x0f) << 8) | adc[2]
    fileobj.write(str(Vref*data/4096)+"\n")

    spi.close()