import time
import RPi.GPIO as GPIO

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

print('started set color')
r.ChangeDutyCycle(float(50))
g.ChangeDutyCycle(float(50))
b.ChangeDutyCycle(float(50))
time.sleep(10)

usrInput = ""

while usrInput != '0':
    usrInput = input('--> ')

