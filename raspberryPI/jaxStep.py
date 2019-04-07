import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
control_pins = [7,11,13,15]
buttonPIN = 12
GPIO.setup(buttonPIN, GPIO.IN)

def rotateStepper(degrees):
    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
        halfstep_seq = [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
        ]
    bin = int(degrees*1.42222)
    for i in range(bin):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)

while True:
    try:
        #usrInput = input("Degrees to Rotate: ")
        #rotateStepper(float(usrInput))
        button = GPIO.input(buttonPIN)
        if button == 0:
            randDegree = random.randint(1,9)
            print(randDegree)
            rotateStepper(randDegree * 45)
    except KeyboardInterrupt:
            GPIO.cleanup()
