#!/usr/bin/env python3
# Author: Edoardo Paolo Scalafiotti <edoardo849@gmail.com>
import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO
pin = 18 # The pin ID, edit here to change it
maxTMP = 40 # The maximum temperature in Celsius after which we trigger the fan
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setwarnings(False)
    return()
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    print("temp is {0}".format(temp)) #Uncomment here for testing
    return temp
def fanON():
    setPin(True)
    return()
def fanOFF():
    setPin(False)
    return()
def getTEMP():
    CPU_temp = float(getCPUtemperature())
    if CPU_temp>maxTMP:
        fanON()
    else:
        fanOFF()
    return()
def setPin(mode): # A little redundant function but useful if you want to add logging
    GPIO.output(pin, mode)
    return()
try:
    setup() 
    while True:
        getTEMP()
    sleep(5) # Read the temperature every 5 sec, increase or decrease this limit if you want
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
    GPIO.cleanup() # resets all GPIO ports used by this program
