import RPi.GPIO as GPIO
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
  #humedad
pin = 26

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering



while True:
    print("entra")
    humedad, temperatura = Adafruit_DHT.read(sensor, pin)
    print(temperatura)