import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.OUT)

try:
    time.sleep(2)
    while(True):
        if(GPIO.input(23)):
            GPIO.output(24, True)
            time.sleep(0.5)
            GPIO.output(24, False)
            print("motion detected")
            time.sleep(1)
        
        time.sleep(0.1)
    
except:
    GPIO.cleanup()