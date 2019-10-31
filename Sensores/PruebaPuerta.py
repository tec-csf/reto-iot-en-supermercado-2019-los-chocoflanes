import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while (True):
    if GPIO.input(7):
        print("Doors open")
        time.sleep(2)
    else:
        print("Doors closed")
        time.sleep(2)