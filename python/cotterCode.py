import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

'''
The circuit:

Gnd to Rpi Board Pin 2
R   to Rpi Board Pin 11 (GPIO 17)
G   to Rpi Board Pin 13 (GPIO 27)
B   to Rpi Board Pin 15 (GPIO 22)
'''

RPin = 13
GPin = 11
BPin = 15

GPIO.setup(RPin, GPIO.OUT)
GPIO.setup(GPin, GPIO.OUT)
GPIO.setup(BPin, GPIO.OUT)
r = GPIO.PWM(RPin, 255)
r.start(0)
g = GPIO.PWM(GPin, 255)
g.start(0)
b = GPIO.PWM(BPin, 255)
b.start(0)


def pushColor(R, G, B):
    
    r.ChangeDutyCycle(float(R))
    g.ChangeDutyCycle(float(G))
    b.ChangeDutyCycle(float(B))

    time.sleep(.04)
    
userInput = ""

while userInput != "0":
    
    userInput = input("-------\nChoose a mode:  \n0) Exit\n1) Scan thru the colors\n2) Manual Mode\n")

    if userInput == "1":    
        for x in range (0, 100):
            
            pushColor(x, 0, 0)
            
        for x in range (0, 100):
            
            pushColor(100-x, 0, x)
            
        for x in range (0, 100):
            
            pushColor(0, x, 100-x)

        for x in range (0,100):
            
            pushColor(x, 100-x, 0)
            
        for x in range (0,100):
            
            pushColor(100-x, 0, 0)
    elif userInput == "2":
        redValue = input("Red Value (0-100):")
        greenValue = input("Green Value (0-100):")
        blueValue = input("Blue Value (0-100):")
        
        pushColor(redValue, greenValue, blueValue)

#pushColor(0, 0, 0)

GPIO.cleanup()
print("Completed Script")