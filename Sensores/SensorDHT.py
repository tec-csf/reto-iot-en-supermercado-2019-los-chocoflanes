import RPi.GPIO as GPIO
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
  #humedad
pin = 31

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

def humCallback(pin):
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
    print(temperatura)
    #if temperatura >21:
     #   GPIO.output(led_pin, GPIO.HIGH)
    #else:
     #   GPIO.output(led_pin, GPIO.LOW)

while True:
    humCallback(pin)