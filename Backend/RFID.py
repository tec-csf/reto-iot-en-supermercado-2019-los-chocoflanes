import RPi.GPIO as GPIO
from mfrc522 import *

reader = SimpleMFRC522()
try:
    text=input("New data")
    print("Place your tag")
    reader.write(text)
    print("Written")
finally:
    GPIO.cleanup()