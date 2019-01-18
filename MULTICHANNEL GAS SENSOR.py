import ubinascii
import time

class MULTIGAS:
    #address = None
    is_connected = 0
    res=[0]*3

    def __init__(self, i2c, address=0x19):
        self.i2c = i2c
        self.address=address
        is_connected = 0
        if self.readR0() >= 0:
            self.is_connected = 1
            print('its connected')
        print(self.readR0())
    def readR0(self):
        rtnData = 0

        rtnData = self.readData(0x11)
        if(rtnData >= 0):
            self.res0[0] = rtnData
        else:
            return rtnData

        rtnData = self.readData(0x12)
        if(rtnData >= 0):
            self.res0[0] = rtnData
        else:
            return rtnData

        rtnData = self.readData(0x13)
        if(rtnData >= 0):
            self.res0[0] = rtnData
        else:
            return rtnData
        return 0

    def readData(self,cmd):
        timeout = 0
        buffer=[0]*4
        checksum = 0
        rtnData = 0


        #buffer=bus.read_i2c_block_data(self.address, cmd, 4)

        print(self.i2c.scan())

        '''
        #start byte?
        self.i2c.writeto(0x48, 0)

        self.i2c.writeto(0x48, 0x0B)
        self.i2c.writeto(0x48, 1)

        help(I2C)
        buffe=0x48
        '''

        self.i2c.writeto(0x19, 0x0b)
        self.i2c.writeto(0x19, 0x01)
        #self.i2c.writeto(0x04, 0x01)

        #self.i2c.writeto(0x19, 0x06)
        #self.i2c.writeto(0x19, 0x08)


        self.i2c.writeto(0x19, 0x06)
        A0=i2c.readfrom_mem(0x19,0x08, 6)
        print('testA0=')
        print(A0)
        print('testA01=')
        print(A0[1])
        A01 = float(A0[0]*256 + A0[1])
        A02 = float(A0[2]*256 + A0[3])
        A03 = float(A0[4]*256 + A0[5])
        print(A03)

        self.i2c.writeto(0x19, 0x01)
        An11=i2c.readfrom(0x19, 2)
        An1=float(An11[0]*256 + An11[1])
        print('testAn=')
        #print(An1)

        An22=i2c.readfrom_mem(0x19,0x02, 2)
        An2=float(An22[0]*256 + An22[1])
        #print(An2)

        An33=i2c.readfrom_mem(0x19,0x03, 2)
        An3=float(An33[0]*256 + An33[1])
        print(An3)


        ratio1=(An1/A01)*((1023.0-A01)/(1023.0-An1))

        ratio2=(An2/A02)*((1023.0-A02)/(1023.0-An2))
        ratio3=(An3/A03)*((1023.0-A03)/(1023.0-An3))

        print('ratio3')
        print(ratio3)

        cCO = (ratio2**-1.179)*4.385;
        cNO2 = pow(ratio3, 1.007)/6.855;
        cNH3 = pow(ratio1, -1.67)/1.47;

        print('gases')
        print(cCO)
        print(cNO2)
        print(cNH3)

        '''
        #self.i2c.readfrom_into(0x48, buffe)
        buffer0=self.i2c.readfrom_mem(0x19,0x02,5)
        buffer1=self.i2c.readfrom_mem(0x19,0x01,1)
        buffer2=self.i2c.readfrom_mem(0x19,0x01,1)
        buffer3=self.i2c.readfrom_mem(0x19,0x01,1)
        print('Buffer:')
        print(buffer0)
        print(buffer1)
        print(buffer2)
        print(buffer3)
        #print(buffer[3])
        '''

        checksum = buffer[0] + buffer[1] + buffer[2]
        if checksum != buffer[3]:
            return -4
        rtnData = ((buffer[1] << 8) + buffer[2])

        return rtnData

    def sendI2C(self,cmd):
        bus.write_byte(self.address, cmd)

'''
if __name__ == "__main__":
	m= MutichannelGasSensor()

'''
import time
from machine import I2C
#import multigas

i2c = I2C(1, I2C.MASTER, baudrate=100000)

gas = MULTIGAS(i2c)
'''
slave=i2c.scan() #<-show slave list
print(slave)

while(True):
        data = gas.read()
'''
