#Program asks for user input to determine color to shine.

import RPi.GPIO as GPIO

pinRed = 11   #Set to appropriate GPIO
pinGreen = 15 #Should be set in the 
pinBlue = 13  #GPIO.BOARD format

# def blink(pin):
#     GPIO.setmode(GPIO.BOARD)
    
#     GPIO.setup(pin, GPIO.OUT)
#     GPIO.output(pin, GPIO.HIGH)
    
# def turnOff(pin):
#     GPIO.setmode(GPIO.BOARD)
#     GPIO.setup(pin, GPIO.OUT)
#     GPIO.output(pin, GPIO.LOW)

class Light():
    def __init__(self):
        GPIO.setwarnings = False
        self.status = ''
        self.colors = {
            'red':[pinRed], 'blue':[pinBlue], 
            'green':[pinGreen], 'yellow':[pinRed, pinGreen]
            }
        return None

    def setColor(self, color):
        GPIO.setmode(GPIO.BOARD)
        for pin in self.colors[color]:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)

    def off(self):
        for color in self.colors:
            for pin in self.colors[color]:
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.LOW)
        self.status = 'off'

light1 = Light()
light1.setColor('blue')
