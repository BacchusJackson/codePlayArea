import RPi.GPIO as GPIO
import time
from datetime import datetime, timedelta
from random import randint

#set up pin constants
R = 11
G = 15
B = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
#set rgb default values
r = GPIO.PWM(R, 255)
g = GPIO.PWM(G, 255)
b = GPIO.PWM(B, 255)
#initialize the pins
r.start(0)
g.start(0)
b.start(0)

class LEDLight():
    #Set up the board
    def __init__(self):
        print('initing..')

    def setColor(self, red, green, blue):
        r.ChangeDutyCycle(int(red))
        g.ChangeDutyCycle(int(green))
        b.ChangeDutyCycle(int(blue))
        time.sleep(.04)
        return

    def turnOff(self):
        self.setColor(0, 0, 0)
        return

    def flashRandomColors(self, inputSeconds):
        endTime = datetime.now() + timedelta(seconds=int(inputSeconds))
        while datetime.now() < endTime:
	        self.setColor(randint(0, 100), randint(0, 100), randint(0,100))
	        time.sleep(.01)
        return

    def cleanUp(self):
        print('cleaning up...')
        GPIO.cleanup()
        return

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
            light.turnOff()
        elif usrInput == 'exit':
            light.cleanUp()
            exit()
        else:
            print('Not a good input... Try again.')

light = LEDLight()
main()
