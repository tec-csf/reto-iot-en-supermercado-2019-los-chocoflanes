import RPi.GPIO as GPIO
import sys
sys.path.append("/home/pi/MFRC522-python")
from mfrc522 import SimpleMFRC522

reader=SimpleMFRC522()

try:
    while(True):
        text=input("Nombre del producto: ")
        print("Acerca el tag al sensor")
        id,text=reader.write(text)
        print("Se ha registrado exitosamente el producto")
        print(id)
        print(text)
        pass
finally:
    GPIO.cleanup()
