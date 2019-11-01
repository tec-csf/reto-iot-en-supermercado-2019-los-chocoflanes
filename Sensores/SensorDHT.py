import RPi.GPIO as GPIO
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11

pin = 24 #tiene que ser modo bcm, no board (este es pin 16)

GPIO.setwarnings(False) # Ignore warning for now


def humCallback(pin):

    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
    print (humedad)
    print(temperatura)
    #if temperatura >21:
     #   GPIO.output(led_pin, GPIO.HIGH)
    #else:
     #   GPIO.output(led_pin, GPIO.LOW)

while True:
    humCallback(pin)