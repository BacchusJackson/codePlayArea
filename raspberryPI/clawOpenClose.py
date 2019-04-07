#Created by JaX to Test servo fun

import RPi.GPIO as GPIO
import time

motionSensorPIN = 11
servoPIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

pin = GPIO.PWM(servoPIN, 50)
pin.start(3)

try:
    while True:
        usrInput = input("open or close: ")
        if usrInput == "open" or usrInput == "Open":
            inNum = 11
        elif usrInput == "close" or usrInput == "Close":
            inNum = 1
        else:
            inNum = 11

        pin.ChangeDutyCycle(float(inNum))
except KeyboardInterrupt:
    pin.stop()
    GPIO.cleanup()
