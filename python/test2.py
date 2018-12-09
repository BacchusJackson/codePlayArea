#import RPi.GPIO as GPIO

pinRed = 11   #Set to appropriate GPIO
pinGreen = 15 #Should be set in the 
pinBlue = 13  #GPIO.BOARD format

class Light():
    def __init__(self):
        #GPIO.setwarnings = False
        self.status = ''
        self.colors = {
            'red':[pinRed], 'blue':[pinBlue], 
            'green':[pinGreen], 'yellow':[pinRed, pinGreen]
            }
        return None

    def setColor(self, color):
        #GPIO.setmode(GPIO.BOARD)
        for pin in self.colors[color]:
            print(pin)
            #GPIO.setup(pin, GPIO.OUT)
            #GPIO.output(pin, GPIO.HIGH)

light = Light()

print(len(light.colors['red']))



