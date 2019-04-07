#Created by JaX to Test servo fun

import RPi.GPIO as GPIO
import time

motionSensorPIN = 11
servoPIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(motionSensorPIN, GPIO.IN)

clawHand = GPIO.PWM(servoPIN, 50)
clawHand.start(3)

try:
    while True:
        motionInput = GPIO.input(motionSensorPIN)
        print(motionInput)
        if motionInput == 1:
            clawHand.ChangeDutyCycle(11)
        else:
            clawHand.ChangeDutyCycle(3)
except KeyboardInterrupt:
    GPIO.cleanup()
