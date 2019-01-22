from machine import UART
from time import sleep_ms, ticks_ms

__version__ = "0." + "$Revision: 1.8 $"[11:-2]
__license__ = 'GPLV4'

# dflt pins=(Tx-pin,Rx-pin): wiring Tx-pin -> Rx GPS module
# default UART(port=1,baudrate=9600,timeout_chars=2,pins=('P3','P4'))
def GPS():
    try:
      from Config import useGPS
    except:
      useGPS = False

    uart = [-1]
    try:
      from Config import uart
    except: pass

    try:
      from Config import G_Tx, G_Rx
    except:
      import whichUART
      which = whichUART.identifyUART(uart=uart,debug=True)
      try:
        G_Tx = which.G_TX; G_Rx = which.G_RX
        useGPS = which.GPS
      except:
        useGPS = False

    if not useGPS: raise OSError("GPS not configured")

    print('GPS: using %s nr %d: Rx->pin %s, Tx->pin %s' % (useGPS,len(uart),G_Tx,G_Rx))

    last_read = 0
    def readCR(serial):
      global last_read
      if not last_read:
        serial.readall()
        last_read = ticks_ms()
      last_read = ticks_ms()-last_read
      if last_read < 200 and last_read >= 0:
        sleep_ms(200-last_read)
      try:
        line = serial.readline().decode('utf-8')
      except:
        print('Read line error')
        line = ''
      last_read = ticks_ms()
      return line.strip()

    try:
        print("test GPS raw:")
        ser = UART(1,baudrate=9600,timeout_chars=80,pins=(G_Tx,G_Rx))
        for cnt in range(10):
          try:
            x=readCR(ser)
          except:
            print("Cannot read GPS data")
            break
          print(x)
          sleep_ms(400)

        print("test using GPS Dexter:")
        import GPS_dexter as GPS
        # UART Pins pins=(Tx,Rx) default Tx=P3 and Rx=P4
        gps = GPS.GROVEGPS(port=1,baud=9600,debug=False,pins=(G_Tx,G_Rx))
        for cnt in range(10):
          data = gps.MyGPS()
          if data:
            print("Date/time: %s/%s" % (data['date'],data['timestamp']))
            print("lon %.6f, lat %.6f, alt %.2f m" % (data['longitude'],data['latitude'],data['altitude']))
            # print(data)
            gps.debug = False
          else:
            print('No satellites found for a fit')
            print('Turn on debugging')
            gps.debug = True
          sleep_ms(5000)

    except:
        print("Unable to get GPS data  on port %s" % useGPS)

    thisGPS = [0.0,0.0,0.0]
    LAT = const(0)
    LON = const(1)
    ALT = const(2)
    import struct
    from Config import thisGPS
    __version__ = "0." + "$Revision: 3.6 $"[11:-2]
    thisGPS[LAT] = round(float(data['longitude']),5)
    thisGPS[LON] = round(float(data['latitude']),5)
    thisGPS[ALT] = round(float(data['altitude']),1)
    lastGPS = thisGPS
    #sense |= 0x8
    lastGPS[0] = int(thisGPS[LAT]*100000)
    lastGPS[1] = int(thisGPS[LON]*100000)
    lastGPS[2] = int(thisGPS[ALT]*100000)

    print(lastGPS[0])
    print(lastGPS[1])
    print(lastGPS[2])
    version = int(__version__[0])*10+int(__version__[2])
    return lastGPS
    #BBZ = struct.pack('>lll', int(thisGPS[LAT]*100000),int(thisGPS[LON]*100000),int(thisGPS[ALT]*10))
    #print (BBZ)

    #Bz = struct.pack('l', 23)
    #print(Bz)
    # raw  GPS output something like
'''
    $GPGGA,001929.799,,,,,0,0,,,M,,M,,*4C
    $GPGSA,A,1,,,,,,,,,,,,,,,*1E
    $GPGSV,1,1,00*79
    $GPRMC,001929.799,V,,,,,0.00,0.00,060180,,,N*46
    $GPGGA,001930.799,,,,,0,0,,,M,,M,,*44
    $GPGSA,A,1,,,,,,,,,,,,,,,*1E
    '''
'''
    from network import LoRa
    import socket
    import time
    import ubinascii

    # Initialise LoRa in LORAWAN mode.
    # Please pick the region that matches where you are using the device:
    # Asia = LoRa.AS923
    # Australia = LoRa.AU915
    # Europe = LoRa.EU868
    # United States = LoRa.US915
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

    # LoRa MAC (dev_eui): 70B3D54998C7FB74
    # create an OTAA authentication parameters
    app_eui = ubinascii.unhexlify('70B3D57ED00157A3')
    app_key = ubinascii.unhexlify('4EEE1610A5CB82390ED42D172BBE9EFD')

    # join a network using OTAA (Over the Air Activation)
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

    # wait until the module has joined the network
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

    # send some data
    s.send(BBZ)

    print(BBZ)
    # make the socket non-blocking
    # (because if there's no data received it will block forever...)
    s.setblocking(False)



    # get any data received (if any...)
    data = s.recv(64)
    print(data)
'''
