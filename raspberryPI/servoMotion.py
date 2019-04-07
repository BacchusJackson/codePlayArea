#Created by JaX to Test servo fun

import RPi.GPIO as GPIO
import time

servoPIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

pin = GPIO.PWM(servoPIN, 50)
pin.start(3)

try:
    while True:
        inNum = input("To Duty Cycle(3-12): ")
        pin.ChangeDutyCycle(float(inNum))
except KeyboardInterrupt:
    pin.stop()
    GPIO.cleanup()
