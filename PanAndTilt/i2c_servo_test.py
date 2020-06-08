# Testing basic i2c stuff
max = 100
min = 0
position = 255 # valid range is 0 - 180 for servo positioning

import smbus
from time import *

channel = 1

address = 0x04

reg_write_dac = 0x40

bus = smbus.SMBus(channel)

for i in range(0,181):
    bus.write_byte(address, i)
    print(i)
    sleep(.1)
    

#bus.write_byte_data(address, 0x00, 0xb4)
#bus.write_byte_data(address, 0x00, position)
#sleep(1)

bus.write_byte(address, 0x00)