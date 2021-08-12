# PiicoDev® BME280 MicroPython Module

This is the firmware repo for the Core Electronics [PiicoDev® Atmospheric Sensor BME280](https://core-electronics.com.au/catalog/product/view/sku/CE07503).

This module depends on the [PiicoDev Unified Library](https://github.com/CoreElectronics/CE-PiicoDev-Unified).

See the Quickstart Guides:
- [Micro:bit v2](https://core-electronics.com.au/tutorials/piicodev-atmospheric-sensor-bme280-quickstart-guide-for-microbit.html)
- [Raspberry Pi Pico](https://core-electronics.com.au/tutorials/piicodev-atmospheric-sensor-bme280-quickstart-guide-for-rpi-pico.html)
- [Raspberry Pi](https://core-electronics.com.au/tutorials/piicodev-raspberrypi/piicodev-atmospheric-sensor-bme280-raspberry-pi-guide.html)

# Usage
## Simple Example
[main.py](https://github.com/CoreElectronics/CE-PiicoDev-BME280-MicroPython-Module/blob/main/main.py) is a simple example to get started.
```
from PiicoDev_BME280 import PiicoDev_BME280
from time import sleep
sensor = PiicoDev_BME280()
while True:
    tempC, presPa, humRH = sensor.values()
    pres_hPa = presPa / 100
    print(str(tempC)+" °C  " + str(pres_hPa)+" hPa  " + str(humRH)+" %RH")
    sleep(0.1)
```
## Advanced Example
```
from PiicoDev_BME280 import PiicoDev_BME280
from time import sleep
sdaPin=machine.Pin(6)
sclPin=machine.Pin(7)
sensor = PiicoDev_BME280(bus=1, freq=100000, sda=sdaPin, scl=sclPin, t_mode=2, p_mode=5, h_mode=1,iir=2, address=0x77)
zeroAlt = sensor.altitude(pressure_sea_level=1013.25)
while True:
    tempC, presPa, humRH = sensor.values()
    pres_hPa = presPa / 100
    print(str(tempC)+" °C  " + str(pres_hPa)+" hPa  " + str(humRH)+" %RH")
    print(sensor.altitude() - zeroAlt)
    sleep(0.1)
```
## Details
### PiicoDev_BME280(bus=, freq=, sda=, scl=, t_mode=2, p_mode=5, h_mode=1,iir=1, address=0x77)

Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
bus | int | 0,1 | Raspberry Pi Pico: 0, Raspberry Pi: 1 | I2C Bus.  Ignored on Micro:bit
freq | int | 100-1000000 | Device dependent | I2C Bus frequency (Hz).  Ignored on Raspberry Pi
sda | Pin | Device Dependent | Device Dependent | I2C SDA Pin. Implemented on Raspberry Pi Pico only
scl | Pin | Device Dependent | Device Dependent | I2C SCL Pin. Implemented on Raspberry Pi Pico only
t_mode | int | 1-5 | 2 | Controls the oversampling of temperature data
p_mode | int | 1-5 | 5 | Controls the oversampling of pressure data
h_mode | int | 1-5 | 1 | Controls the oversampling of humidity data
iir | int | 0-7 | 1 | Controls the time constant of the IIR filter
address | int | 0x76, 0x77 | 0x77 | This address needs to match the PiicoDev Atmospheric Sensor BME280 hardware address configured by the jumper or ADR pin

### PiicoDev_BME280.altitude(pressure_sea_level=1013.25)

Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
pressure_sea_level | float | any | 1013.25 | Enter the current sea level pressure.  This value is available from your favourite weather service (hPa).
returned | float | | | Altitude (m)


### PiicoDev_BME280.values()

Parameter | Type | Description
--- | --- | ---
returned 1st | float | Temperature (degC)
returned 2nd | float | Pressure (Pa)
returned 3rd | float | Relative humidity (%)

# License
This project is open source - please review the LICENSE.md file for further licensing information.

# Attribution
Code in this repo has been ported from a repo by [neliogodoi](https://github.com/neliogodoi/MicroPython-BME280/blob/master/bme280.py) to include RPi Pico functionality.

If you have any technical questions, or concerns about licensing, please contact technical support on the [Core Electronics forums](https://forum.core-electronics.com.au/).

*\"PiicoDev\" and the PiicoDev logo are trademarks of Core Electronics Pty Ltd.*
