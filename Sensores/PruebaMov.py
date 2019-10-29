import RPi.GPIO as GPIO
import time

<<<<<<< HEAD
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.OUT)
=======
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
>>>>>>> 18ff3325b01d0f0af4b75cbfb0e4e874b2efc5aa

try:
    time.sleep(2)
    while(True):
<<<<<<< HEAD
        if(not GPIO.input(7)):
            GPIO.output(11, True)
            time.sleep(0.5)
            GPIO.output(11, False)
            print("motion detected")
            time.sleep(1)
            
=======
        if(GPIO.input(23)):
            GPIO.output(24, True)
            time.sleep(0.5)
            GPIO.output(24, False)
            print("motion detected")
            time.sleep(1)
>>>>>>> 18ff3325b01d0f0af4b75cbfb0e4e874b2efc5aa
        
        time.sleep(0.1)
    
except:
    GPIO.cleanup()