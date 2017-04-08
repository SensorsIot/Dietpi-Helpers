#!/usr/bin/env python3
# Author: Andreas Spiess
import os
import time
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO


fanPin = 17 # The pin ID, edit here to change it
batterySensPin = 18

maxTMP = 50 # The maximum temperature in Celsius after which we trigger the fan

def Shutdown():  
    fanOFF()
    os.system("sudo shutdown -h 1")
    sleep(100)
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fanPin, GPIO.OUT)
    GPIO.setup(batterySensPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    #GPIO.add_event_detect(batterySensPin, GPIO.RISING, callback = Shutdown, bouncetime = 2000)
    GPIO.setwarnings(False)
    fanOFF()
    return()
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    #print("temp is {0}".format(temp)) #Uncomment here for testing
    return temp
def fanON():
    setPin(True)
    return()
def fanOFF():
    setPin(False)
    return()
def handleFan():
    CPU_temp = float(getCPUtemperature())
    if CPU_temp>maxTMP:
        fanON()
        #print("fan on")
    if CPU_temp<maxTMP-5:
        fanOFF()
        #print("fan off")
    return()
def handleBattery():
    print (GPIO.input(batterySensPin)) 
    if GPIO.input(batterySensPin)==0:
        print("Shutdown()")
        sleep(5)
        Shutdown()
    return()		
def setPin(mode): # A little redundant function but useful if you want to add logging
    GPIO.output(fanPin, mode)
    return()
try:
    setup() 
    while True:
        handleFan()
        handleBattery()
        sleep(5) # Read the temperature every 5 sec, increase or decrease this limit if you want
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
    fanOFF()
    #GPIO.cleanup() # resets all GPIO ports used by this program
