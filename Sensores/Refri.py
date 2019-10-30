import RPi.GPIO as GPIO
import sys
import time
import subprocess
import requests
from datetime import datetime
from pprint import pprint
sys.path.append("/home/pi/MFRC522-python")
from mfrc522 import SimpleMFRC522
from requests.exceptions import ConnectionError

GPIO.setwarnings(False)
chanel=10
#Declaración para funcionalidad del sensor de la puerta
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#inputs de la camara
GPIO.setup(chanel, GPIO.IN)
GPIO.add_event_detect(chanel, GPIO.BOTH, bouncetime=100)

#Inputs para sensor movimiento
inputMov=7
outputMov=11
GPIO.setup(inputMov, GPIO.IN)
GPIO.setup(outputMov, GPIO.OUT)

#Camara Azure
def callbackCamera(chanel):
    
    print("Input detected")
    subprocess.call(['fswebcam -r 640x480 --no-banner /home/pi/Desktop/Semana\ i/ytmmatambn.jpg', '-1'], shell=True)
    face_uri = "https://raspberrycp.cognitiveservices.azure.com/vision/v1.0/analyze?visualFeatures=Faces&language=en"
    pathToFileInDisc = r'/home/pi/Desktop/Semana i/tmma.jpg'
    with open( pathToFileInDisc, "rb") as f:
        data = f.read()
    headers = {"Content-Type": "application/octet-stream", 'Ocp-Apim-Subscription-Key': '7e9cfbb244204fb994babd6111235269'}
    try:
        response = requests.post(face_uri, headers = headers, data = data)
        faces = response.json()
        pprint(faces)
    except ConnectionError:
        pass
    GPIO.add_event_callback(chanel, callbackCamera)
    print("\nI neva freeze\n")

#Lector RFID
def Lector():
    reader=SimpleMFRC522()
    print("Acerque el tag al sensor")
    try:
        id,text = reader.read()
        print(id)
        print(text)
    except KeyboardInterrupt:
        pass

def Movimiento():
    cont=0
    try:
        while(True):
            time.sleep(2)
            print("YEET")
            if(GPIO.input(7)==False):
                cont=cont+1
                print("dentro cont")
            else:
                cont=0
                
            if(cont==3):
                GPIO.output(11,True)
                print("ALARMAAAA")
                time.sleep(5)
                GPIO.output(11,False)
                pass
                
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        pass

def Puertas():
    if GPIO.input(29):
        print("Doors open")
        time.sleep(2)
        callbackCamera(chanel)
        Lector()
        Movimiento()
    else:
        print("Doors closed")
        time.sleep(1)
try:
    while True:
        Puertas()
finally:
    GPIO.cleanup()