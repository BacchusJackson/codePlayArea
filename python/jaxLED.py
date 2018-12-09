import RPi.GPIO as GPIO
import time
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
        r = GPIO.PWM(self.R, 1)
        g = GPIO.PWM(self.G, 1)
        b = GPIO.PWM(self.B, 1)
        #initialize the pins
        r.start(0)
        b.start(0)
        g.start(0)
        return None
    def setColor(self, red, green, blue):
	    self.r.ChangeDutyCycle(red)
	    self.g.ChangeDutyCycle(green)
	    self.b.ChangeDutyCycle(blue)
    def turnOff(self):
	    self.setColor(0, 0, 0)
    def flashRandomColors(self, inputSeconds):
        counter = 0
        while counter < 100 * inputSeconds:
	        self.setColor(randint(0, 100), randint(0, 100), randint(0,100))
	        time.sleep(.01)
	        counter = counter + 1
        self.cleanUp()
    def cleanUp(self):
        print('cleaning up...')
        GPIO.cleanup()

def main():
    light = LEDLight()
    menu = '1 - Enter RGB Values \n 2 - Random Strobe \n, off - Turn off light \n, exit - exit program'
    print(menu)
    usrInput = input('Menu Option --> ')
    if usrInput == '1':
        usrRed = input('Red (1 to 100): ')
        usrGreen = input('Green (1 to 100): ')
        usrBlue = input('Blue (1 to 100): ')
        light.setColor(usrRed, usrGreen, usrBlue)
    if usrInput == '2':
        usrSeconds = input('How long? (seconds) --> ')
        light.flashRandomColors(usrSeconds)
    if usrInput == 'off':
        light.turnOff
    if usrInput == 'exit':
        light.cleanUp
        exit()
    else:
        light.cleanUp
        exit()

main()
