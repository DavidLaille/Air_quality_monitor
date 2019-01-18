import time
from machine import I2C
gas={}
class MULTIGAS:

    def __init__(self, i2c, address):
        self.i2c = i2c
        self.address=address
        is_connected = 0

    def readData(self,address):
        #PowerOn the Heater
        self.i2c.writeto(address, 0x0b)
        self.i2c.writeto(address, 0x01)

        #Retrieve measures of A0(constant) from ADC
        self.i2c.writeto(address, 0x06)
        A0=self.i2c.readfrom_mem(address,0x08, 6)

        #translating bytes into float
        A01 = float(A0[0]*256 + A0[1])
        A02 = float(A0[2]*256 + A0[3])
        A03 = float(A0[4]*256 + A0[5])

        #Retrieve measures of An from ADC
        self.i2c.writeto(address, 0x01)
        An11=self.i2c.readfrom(address, 2)
        An22=self.i2c.readfrom_mem(address,0x02, 2)
        An33=self.i2c.readfrom_mem(address,0x03, 2)

        #translating bytes into float
        An1=float(An11[0]*256 + An11[1])
        An2=float(An22[0]*256 + An22[1])
        An3=float(An33[0]*256 + An33[1])

        #Computing the ratio
        ratio1=(An1/A01)*((1023.0-A01)/(1023.0-An1))
        ratio2=(An2/A02)*((1023.0-A02)/(1023.0-An2))
        ratio3=(An3/A03)*((1023.0-A03)/(1023.0-An3))


        #Calculating Gas concentrations (from data sheet model)
        cCO = (ratio2**-1.179)*4.385;
        cNO2 = pow(ratio3, 1.007)/6.855;
        cNH3 = pow(ratio1, -1.67)/1.47;

        #defining dictionary
        gas["CO"]=cCO
        gas["NO2"]=cNO2
        gas["NH3"]=cNH3
        return gas
