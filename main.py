# PiicoDev Atmospheric Sensor BME280 minimal example code
# This program reads Temperature, Pressure and Relative Humididty
# from the PiicoDev Atmospheric Sensor. An altitude reading is also
# available

from PiicoDev_BME280 import PiicoDev_BME280
from utime import sleep_ms

sensor = PiicoDev_BME280()
zeroAlt = sensor.altitude()

while True:
    # Print data
    tempC, presPa, humRH = sensor.values()
    pres_hPa = presPa / 100
    print("{}C, {}hPa, {}%RH".format(tempC, pres_hPa, humRH))
    
    # Altitude demo
#     print(sensor.altitude() - zeroAlt)
    sleep_ms(200)
       