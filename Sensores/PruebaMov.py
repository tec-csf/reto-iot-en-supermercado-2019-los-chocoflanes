import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.OUT)

try:
    time.sleep(2)
    while(True):
        if( GPIO.input(7)):
            GPIO.output(11, True)
            time.sleep(0.5)
            GPIO.output(11, False)
            print("motion detected")
            time.sleep(2)


        time.sleep(0.1)

except:
    GPIO.cleanup()