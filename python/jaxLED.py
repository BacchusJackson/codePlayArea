import RPi.GPIO as GPIO

R = 11
G = 15
B = 13
 
PINS = [R,G,B]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(R, GPIO.OUT)
GPIO.PWM(R, 100)
