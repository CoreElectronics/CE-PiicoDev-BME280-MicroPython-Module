# PiicoDev Atmospheric Sensor BME280 minimal example code
# This program reads Temperature, Pressure and Relative Humididty
# from the PiicoDev Atmospheric Sensor. An altitude reading is also
# available

from PiicoDev_BME280 import PiicoDev_BME280
from time import sleep

sensor = PiicoDev_BME280()
zeroAlt = sensor.altitude()

while True:
    # Print data
    tempC, presPa, humRH = sensor.values()
    pres_hPa = presPa / 100
    print(str(tempC)+" °C  " + str(pres_hPa)+" hPa  " + str(humRH)+" %RH")
    
    # Altitude demo
#     print(sensor.altitude() - zeroAlt)
    sleep(0.1)
       