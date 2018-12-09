import RPi.GPIO as GPIO
import time
from random import randint

#set up pin constants
R = 11
G = 15
B = 13
 
PINS = [R,G,B]

#Set up the board
GPIO.setmode(GPIO.BOARD)
GPIO.setup(R, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(G, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(B, GPIO.OUT, initial=GPIO.LOW)

#set rgb default values
r = GPIO.PWM(R, 1)
g = GPIO.PWM(G, 1)
b = GPIO.PWM(B, 1)

#initialize the pins
r.start(0)
b.start(0)
g.start(0)

def setColor(red, green, blue):
	r.ChangeDutyCycle(red)
	g.ChangeDutyCycle(green)
	b.ChangeDutyCycle(blue)

def turnOff():
	setColor(0, 0, 0)


counter = 0
while counter < 1000:
	setColor(randint(0, 100), randint(0, 100), randint(0,100))
	time.sleep(.01)
	counter = counter + 1

turnOff()

print('cleaning up...')
GPIO.cleanup()


