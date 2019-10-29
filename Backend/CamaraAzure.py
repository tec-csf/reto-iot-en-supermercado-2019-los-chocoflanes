import RPi.GPIO as GPIO
import time
import subprocess
import requests
from datetime import datetime
from pprint import pprint
import sys

chanel = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(chanel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def callbackCamera(chanel):
    if GPIO.input(chanel) == GPIO.HIGH:
        print("Input detected")
        subprocess.call(['fswebcam -r 640x480 --no-banner /home/pi/Desktop/Semana\ i/tmma.jpg', '-1'], shell=True)
        face_uri = "https://raspberrycp.cognitiveservices.azure.com/vision/v1.0/analyze?visualFeatures=Faces&language=en"
        pathToFileInDisc = r'/home/pi/Desktop/Semana i/tmma.jpg'
        with open( pathToFileInDisc, "rb") as f:
            data = f.read()
        headers = {"Content-Type": "application/octet-stream", 'Ocp-Apim-Subscription-Key': '7e9cfbb244204fb994babd6111235269'}

        response = requests.post(face_uri, headers = headers, data = data)
        faces = response.json()
        pprint(faces)

GPIO.add_event_detect(chanel, GPIO.BOTH, bouncetime=100)
while(True):
    GPIO.add_event_callback(chanel, callbackCamera)

print("\nI neva freeze\n")