import pycom
import time
from machine import Pin, I2C
from dth import DTH
from bme280 import BME280

#i2c = I2C(0, I2C.MASTER, baudrate=100000)
#print(i2c.scan())
#bmp = BME280(i2c=i2c, address=0x77 )


# blue
th = DTH(Pin('P8', mode=Pin.OPEN_DRAIN),1)
time.sleep(2)
x=0
for x in range(4):
    result = th.read()
    if result.is_valid():
        # green
        print('Temperature: {:3.2f}'.format(result.temperature/1.0))
        print('Humidity: {:3.2f}'.format(result.humidity/1.0))
        print(result.temperature)
        time.sleep(1)
    time.sleep(1)



'''


from machine import Pin, I2C
from bme280 import *
import time


i2c = I2C(0)
i2c.scan()
print(i2c.scan())

bmp = BME280(i2c=i2c, address=0x77 )

for x in range(0, 100):
    print(bmp.values)
    time.sleep(1)
'''
