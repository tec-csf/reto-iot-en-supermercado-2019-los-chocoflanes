import RPi.GPIO as GPIO
import sys
sys.path.append("/home/pi/MFRC522-python")
from mfrc522 import SimpleMFRC522

reader=SimpleMFRC522()

print("Acerque el tag al sensor")

try:
    id,text = reader.read()
    print(id)
    print(text)

finally:
    GPIO.cleanup()