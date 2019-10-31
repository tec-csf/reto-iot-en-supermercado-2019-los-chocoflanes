import RPi.GPIO as GPIO
import sys
import json
import time
import subprocess
import datetime
import requests
import jwt
import paho.mqtt.client as mqtt
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

#Arreglo para RFID
products = []

#Camara Azure
def callbackCamera(chanel):
    
    print("Input detected")
    subprocess.call(['fswebcam -r 640x480 --no-banner /home/pi/Desktop/Semana\ i/ytmmatambn.jpg', '-1'], shell=True)
    face_uri = "https://raspberrycp.cognitiveservices.azure.com/vision/v1.0/analyze?visualFeatures=Faces&language=en"
    pathToFileInDisc = r'/home/pi/Desktop/Semana i/ytmmatambn.jpg'
    with open( pathToFileInDisc, "rb") as f:
        data = f.read()
    headers = {"Content-Type": "application/octet-stream", 'Ocp-Apim-Subscription-Key': '7e9cfbb244204fb994babd6111235269'}
    try:
        response = requests.post(face_uri, headers = headers, data = data)
        faces = response.json()

        f= faces['faces']
        
        faces_list = []
        faces_list.append(f[0]['age'])
        faces_list.append(f[0]['gender'])
        usertoCloud(faces_list)

    except IndexError:
        print("Face not found")
        pass


#Lector RFID
def Lector(products):
    reader=SimpleMFRC522()
    print("Acerque el tag al sensor")
    try:
        id,text = reader.read()
        print(id)
        print(text)
        try:
            products.index(id)
            products.remove(id)
        except ValueError:
            products.append(id)
    except KeyboardInterrupt:
        pass

    return products

def Movimiento():
    cont=0
    try:
        while(True):
            time.sleep(2)
            
            if(GPIO.input(7)==False):
                cont=cont+1
            else:
                cont=0
                
            if(cont==3):
                GPIO.output(11,True)
                print("Pélenme!!!!!")
                time.sleep(5)
                GPIO.output(11,False)
                break
                
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        pass

def Puertas():
    if GPIO.input(29):
        print("Doors open")
        time.sleep(2)
        callbackCamera(chanel)
        products = Lector(products)
        Movimiento()
    else:
        print("Doors closed")
        time.sleep(1)
        
        

def error_str(rc):
    return '{}: {}'.format(rc, mqtt.error_string(rc))


def on_connect(unusued_client, unused_userdata, unused_flags, rc):
    print('on_connect', error_str(rc))


def on_publish(unused_client, unused_userdata, unused_mid):
    print('on_publish')


def usertoCloud(faces_list):
    ssl_private_key_filepath = '/home/pi/Desktop/Semana i/reto-iot-en-supermercado-2019-los-chocoflanes/Datasets/KeyControlUsuarios/demo_private.pem'
    ssl_algorithm = 'RS256'  # Either RS256 or ES256
    root_cert_filepath = '/home/pi/Desktop/Semana i/reto-iot-en-supermercado-2019-los-chocoflanes/Datasets/KeyControlUsuarios/roots.pem'
    project_id = 'semanai-257408'
    gcp_location = 'us-central1'
    registry_id = 'semanai'
    device_id = 'ControlUsuarios'
    # Get current time

    cur_time = datetime.datetime.utcnow()

    # Create a JWT

    def create_jwt():
        token = {
        'iat': cur_time,
        'exp': cur_time + datetime.timedelta(minutes=60),
        'aud': project_id
        }

        with open(ssl_private_key_filepath, 'r') as f:
            private_key = f.read()

        return jwt.encode(token, private_key, ssl_algorithm)


    _CLIENT_ID = 'projects/{}/locations/{}/registries/{}/devices/{}'.format(
    project_id, gcp_location, registry_id, device_id)
    _MQTT_TOPIC = '/devices/{}/events'.format(device_id)

    client = mqtt.Client(client_id=_CLIENT_ID)
    # authorization is handled purely with JWT, no user/pass, so username can be whatever
    client.username_pw_set(
    username='unused',
    password=create_jwt())


    def error_str(rc):
        return '{}: {}'.format(rc, mqtt.error_string(rc))


    def on_connect(unusued_client, unused_userdata, unused_flags, rc):
        print('on_connect', error_str(rc))


    def on_publish(unused_client, unused_userdata, unused_mid):
        print('on_publish')


    client.on_connect = on_connect
    client.on_publish = on_publish

    # Replace this with 3rd party cert if that was used when creating registry
    client.tls_set(ca_certs=root_cert_filepath)
    client.connect('mqtt.googleapis.com', 443)
    client.loop_start()
    facesload = '{{ "ts": {}, "age": {}, "gender": "{}" }}'.format(
        int(time.time()), faces_list[0],faces_list[1])
    # Uncomment following line when ready to publish
    print("{}\n".format(facesload))
    client.publish(_MQTT_TOPIC, facesload, qos=1)
    client.loop_stop()
    
for i in range(15):    
    try:
        Puertas()
    except KeyboardInterrupt:
        pass