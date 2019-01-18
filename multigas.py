
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

        d[1]=11
        d[2]=1
        print(d[])
        self.i2c.writeto(0x19,'11')
        self.i2c.writeto(0x19,'1')
        try:
            buffer=self.i2c.readfrom(cmd,10)
            print('thibbb:')
        except:
            print('this much:')
            buffer=self.i2c.readfrom(0x13,2)
            print('this much:')
            print(buffer)
            print('then data:')
            print(data)


        checksum = buffer[0] + buffer[1] + buffer[2]
        if checksum != buffer[3]:
            return -4
        rtnData = ((buffer[1] << 8) + buffer[2])

        return rtnData

    def sendI2C(self,cmd):
        bus.write_byte(self.address, cmd)


if __name__ == "__main__":
	m= MutichannelGasSensor()






'''class MULTIGAS:
    #MEASUREMENT_TIME = const(120)

    def __init__(self, i2c, addr=0x19):
        self.i2c = i2c
        #self.period = period
        self.addr = addr
        self.time = 0
        self.value = 0

        self.i2c.writeto(addr, 0x21) # Power ON

    def read(self):
        data = self.i2c.readfrom(self.addr, 30)

        return data
'''
