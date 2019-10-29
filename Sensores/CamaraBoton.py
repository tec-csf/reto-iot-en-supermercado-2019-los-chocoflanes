import RPi.GPIO as GPIO
import time
import subprocess

chanel = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(chanel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def callbackCamera(chanel):
    if GPIO.input(chanel) == GPIO.HIGH:
        print("Input detected")
        subprocess.call(['fswebcam -r 640x480 --no-banner /home/pi/Desktop/Semana\ i/tmma.jpg', '-1'], shell=True)

GPIO.add_event_detect(chanel, GPIO.BOTH, bouncetime=100)
GPIO.add_event_callback(chanel, callbackCamera)

print("\nI neva freeze\n")