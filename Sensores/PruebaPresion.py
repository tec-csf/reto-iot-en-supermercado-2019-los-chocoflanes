import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
prev_input = 0
try:
    while(True):
        input = GPIO.input(4)
        print(input)
        if((not prev_input) and input):
            print("under pressure")
        
        prev_input = input
        time.sleep(0.10)
    
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
