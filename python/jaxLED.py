import RPi.GPIO as GPIO

R = 11
G = 15
B = 13
 
PINS = [R,G,B]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(R, GPIO.OUT, inital=GPIO.LOW)

p = GPIO.PWM(R, 100)
p.start(0)
