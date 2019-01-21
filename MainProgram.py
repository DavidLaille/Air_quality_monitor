import socket
import ubinascii
import struct
import math
import pycom
import time
import Config

from machine import Pin, I2C
from network import LoRa

from SDS011 import SDS011
#from dust_test import data as ddata
import dust_test
from Multichannel import MULTIGAS

from dth import DTH


#LoRa Config
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
#OTAA parameters
app_eui = ubinascii.unhexlify('70B3D57ED00157A3')
app_key = ubinascii.unhexlify('4EEE1610A5CB82390ED42D172BBE9EFD')


while(True):
    #Dust Sensor
    try:
        ddata=dust_test.getdust()
        print(ddata)
        avgpm10=int(math.ceil(ddata["pm10"]*10))
        avgpm25=int(math.ceil(ddata["pm25"]*10))
        dpack=struct.pack(">II",avgpm25, avgpm10)
    except:
        print('The Dust sensor is not connected')


    #Multichannel gas sensor
    i2c = I2C(1, I2C.MASTER, baudrate=100000, pins=(Config.SDA_Multi, Config.SCL_Multi))

    #Define address of Multichannel Gas Sensor
    gasadd=0x19
    try:
        gas = MULTIGAS(i2c, gasadd)
        gases=gas.readData(gasadd)
        #print(gases)
        NH3 =int(math.ceil(gases["NH3"]*100000))
        CO=int(math.ceil(gases["CO"]*100000))
        NO2=int(math.ceil(gases["NO2"]*100000))
        gpack=struct.pack(">QQQ",NH3, CO, NO2)
    except:
        print("Multichannel Gas sensor is not connected")
        pass


    #DHT22 Sensor
    th = DTH(Pin('P8', mode=Pin.OPEN_DRAIN),1)
    x=0

    try:
        for x in range(8):
                result = th.read()
                if result.is_valid():
                    print('Temperature: {:3.2f}'.format(result.temperature/1.0))
                    print('Humidity: {:3.2f}'.format(result.humidity/1.0))
                    #print(bmp.values)
                    time.sleep(1)
                time.sleep(1)
    except:
        print("DHT sensor is not connected")
        pass

    temp=int(result.temperature*10)
    humidity=int(result.humidity*10)
    print('final temp and humidity')
    print(temp)
    print(humidity)




    payload=struct.pack(">IIQQQihIIQQQih",avgpm25, avgpm10, NH3, CO, NO2, temp, humidity)
    #Payload format:
    #(avgpm25*10),(avgpm10*10)
    #(NH3*100 000),(CO*100 000),(NO2*100 000)
    #(temp*10), (humidity*10)


    unpack=struct.unpack(">IIQQQih",payload)
    print (unpack)



    #Joining the LoRa Network (TTN)
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

    while not lora.has_joined():
        time.sleep(2.5)
        print('Not yet joined...')

    # create a LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    # set the LoRaWAN data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

    # make the socket blocking
    # (waits for the data to be sent and for the 2 receive windows to expire)
    s.setblocking(True)

    # send the Payload
    s.send(payload)

    # make the socket non-blocking
    # (because if there's no data received it will block forever...)

    s.setblocking(False)
    print('Data is sent')

    # get any data received (if any...)
    #receiveddata = s.recv(64)
    #print("received from LoRa:")
    #print(receiveddata)
