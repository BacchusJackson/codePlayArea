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
        self.off()
        for pin in self.colors[color]:
            print(pin)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)
        self.status = 'on'
    
    def isColor(self, color):
        if color in self.colors.keys():
            return True
        else:
            return False

    def off(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pinRed, GPIO.OUT)
        GPIO.output(pinRed, GPIO.LOW)
        GPIO.setup(pinBlue, GPIO.OUT)
        GPIO.output(pinBlue, GPIO.LOW)
        GPIO.setup(pinGreen, GPIO.OUT)
        GPIO.output(pinGreen, GPIO.LOW)
        GPIO.cleanup()
        self.status = 'off'


def main():
    light1 = Light()
    while True:
        usrInput = input('--> ')
        if usrInput == 'off':
            light1.off()
            print('light off')
        elif usrInput == 'exit':
            print('.....exiting program')
            GPIO.cleanup()
            exit()
        else:
            if light1.isColor(usrInput) == False:
                print(usrInput + ' is not a color... Try again silly.')
                continue
            print(usrInput + " light on")
            light1.setColor(usrInput)

main()
