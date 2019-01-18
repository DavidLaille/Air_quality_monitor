
import time
from machine import I2C
from Multichannel import MULTIGAS

gases={}


#import multigas


i2c = I2C(1, I2C.MASTER, baudrate=100000, pins=('P23', 'P22')) #SDA=P23, SCL=P22

#Define address of Multichannel Gas Sensor
gadd=0x19


gas = MULTIGAS(i2c, gasadd)
gases=gas.readData(gasadd)
print(gases)


print("Multichannel Gas sensor is not connected")
pass
