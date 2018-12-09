import RPi.GPIO as GPIO
import time
from datetime import datetime, timedelta
from random import randint

class LEDLight():
    #Set up the board
    def __init__(self):
        #set up pin constants
        self.R = 11
        self.G = 15
        self.B = 13
        self.PINS = [self.R,self.G,self.B]
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.R, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.G, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.B, GPIO.OUT, initial=GPIO.LOW)
        #set rgb default values
        self.r = GPIO.PWM(self.R, 1)
        self.g = GPIO.PWM(self.G, 1)
        self.b = GPIO.PWM(self.B, 1)
        #initialize the pins
        self.r.start(0)
        self.b.start(0)
        self.g.start(0)
        return None
    def setColor(self, red, green, blue):
        self.r.ChangeDutyCycle(float(red))
        self.g.ChangeDutyCycle(float(green))
        self.b.ChangeDutyCycle(float(blue))
        time.sleep(5)
    def turnOff(self):
        self.setColor(0, 0, 0)
    def flashRandomColors(self, inputSeconds):
        endTime = datetime.now() + timedelta(seconds=int(inputSeconds))
        while datetime.now() < endTime:
	        self.setColor(randint(0, 100), randint(0, 100), randint(0,100))
	        time.sleep(.01)
        self.cleanUp()
    def cleanUp(self):
        print('cleaning up...')
        GPIO.cleanup()

def main():
    menu = '\n1 - Enter RGB Values \n2 - Random Strobe \noff - Turn off light \nexit - exit program'
    print(menu)
    while True:
        usrInput = input('Menu Option --> ')
        if usrInput == '1':
            usrRed = input('Red (1 to 100): ')
            usrGreen = input('Green (1 to 100): ')
            usrBlue = input('Blue (1 to 100): ')
            light.setColor(usrRed, usrGreen, usrBlue)
        elif usrInput == '2':
            usrSeconds = input('How long? (seconds) --> ')
            light.flashRandomColors(usrSeconds)
        elif usrInput == 'off':
            light.turnOff
        elif usrInput == 'exit':
            light.cleanUp
            exit()
        else:
            print('Not a good input... Try again.')
            light.cleanUp


light = LEDLight()
main()

