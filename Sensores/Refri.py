import RPi.GPIO as GPIO
import sys
import json
import time
import subprocess
import datetime
import threading
import requests
import jwt
import Adafruit_DHT
import paho.mqtt.client as mqtt
from pprint import pprint
sys.path.append("/home/pi/MFRC522-python")
from mfrc522 import SimpleMFRC522
from requests.exceptions import ConnectionError

GPIO.setwarnings(False)

#Declaración para funcionalidad del sensor de la puerta
GPIO.setmode(GPIO.BOARD)
inputPuerta=7
GPIO.setup(inputPuerta, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Inputs para sensor movimiento
inputMov=12
outputMov=16
GPIO.setup(inputMov, GPIO.IN)
GPIO.setup(outputMov, GPIO.OUT)

chanel=10

#pin y tipo de sensor temperatura
temperature_pin=24 #tiene que ser modo bcm, no board (este es pin 16)
sensor = Adafruit_DHT.DHT11
hot_pin=15
cold_pin=11
normal_pin=13
GPIO.setup(hot_pin, GPIO.OUT)
GPIO.setup(cold_pin, GPIO.OUT)
GPIO.setup(normal_pin, GPIO.OUT)
#Camara Azure
def callbackCamera(chanel):
    
    
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
        ssl_private_key_filepath = '/home/pi/Desktop/Semana i/reto-iot-en-supermercado-2019-los-chocoflanes/Datasets/KeyControlUsuarios/demo_private.pem'
        root_cert_filepath = '/home/pi/Desktop/Semana i/reto-iot-en-supermercado-2019-los-chocoflanes/Datasets/KeyControlUsuarios/roots.pem'
        device_id = 'ControlUsuarios'
        if(faces_list):
            usertoCloud(ssl_private_key_filepath,root_cert_filepath,device_id,faces_list=faces_list)

    except IndexError:
        print("Face not found")
        pass


#Lector RFID
def Lector():
    reader=SimpleMFRC522()
    print("Acerque el tag al sensor")
    try:
        id,text = reader.read()
        print(text)
            
    except KeyboardInterrupt:
        pass

#Sensor de movimiento para checar si la puerta se quedó abierta
def Movimiento():
    cont=0
    try:
        while(GPIO.input(inputPuerta)):
            time.sleep(4)
            
            if(GPIO.input(inputMov)==False):
                cont=cont+1
            else:
                cont=0
                
            if(cont==3):
                GPIO.output(outputMov,True)
                print("Pélenme!!!!!")
                time.sleep(5)
                GPIO.output(outputMov,False)
                break
                
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        pass

#Medición de temperatura constante
def Temperatura():
    ssl_private_key_filepath = '/home/pi/Desktop/Semana i/reto-iot-en-supermercado-2019-los-chocoflanes/Datasets/KeyControlRefri/demo_private.pem'
    root_cert_filepath = '/home/pi/Desktop/Semana i/reto-iot-en-supermercado-2019-los-chocoflanes/Datasets/KeyControlRefri/roots.pem'
    device_id = 'ControlRefri'
    temper_list=[]
    try:
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, temperature_pin)
        temper_list.append(temperatura)
        temper_list.append(humedad)
        # time.sleep(10)
        if(temper_list):
            usertoCloud(ssl_private_key_filepath,root_cert_filepath,device_id,temper_list=temper_list)
        
        if(temperatura>30):
            print("entro a 1")
            GPIO.output(hot_pin,True)
            GPIO.output(cold_pin,False)
            GPIO.output(normal_pin,False)
        elif(temperatura<17):
            print("entro a 2")
            GPIO.output(cold_pin,True)
            GPIO.output(hot_pin,False)
            GPIO.output(normal_pin,False)
        else:
            print("entro a 3")
            GPIO.output(normal_pin,True)
            GPIO.output(cold_pin,False)
            GPIO.output(hot_pin,False)
            
    except IndexError:
        print("sensor de temperatura desconectado")
        pass

#Detectar si la puerta esta abierta
def Puertas():
    if GPIO.input(inputPuerta):
        print("Doors open")
        GPIO.output(normal_pin,False)
        GPIO.output(cold_pin,False)
        GPIO.output(hot_pin,False)
        
        time.sleep(2)
        callbackCamera(chanel)
        Lector()
        Movimiento()
    else:
        print("Doors closed")
        while (not GPIO.input(inputPuerta)):
            Temperatura()
            time.sleep(1)
        
        

def error_str(rc):
    return '{}: {}'.format(rc, mqtt.error_string(rc))


def on_connect(unusued_client, unused_userdata, unused_flags, rc):
    print('on_connect', error_str(rc))


def on_publish(unused_client, unused_userdata, unused_mid):
    print('on_publish')


def usertoCloud(ssl_private_key_filepath,root_cert_filepath,device_id, faces_list=[], temper_list=[], product_list=[]):
    
    ssl_algorithm = 'RS256'  # Either RS256 or ES256
    project_id = 'semanai-257408'
    gcp_location = 'us-central1'
    registry_id = 'semanai'
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

    def publishUsuario(faces_list):
         client.loop_start()
         facesload = '{{ "ts": {}, "age": {}, "gender": "{}" }}'.format(int(time.time()), faces_list[0],faces_list[1])
         print("{}\n".format(facesload))
         client.publish(_MQTT_TOPIC, facesload, qos=1)
         client.loop_stop()
         
    def publishTemperatura(temper_list):
         client.loop_start()
         tempload = '{{ "ts": {}, "temperature": {}, "humidity": {} }}'.format(int(time.time()), temper_list[0],temper_list[1])
         print("{}\n".format(tempload))
         client.publish(_MQTT_TOPIC, tempload, qos=1)
         client.loop_stop()
         
    def publishAlmacen(product_list):
         client.loop_start()
         prodload = '{{ "updated": {},"id": {}, "producto": "{}", "cantidad": {} }}'.format(int(time.time()), product_list[0],product_list[1],product_list[2])
         print("{}\n".format(prodload))
         client.publish(_MQTT_TOPIC, prodload, qos=1)
         client.loop_stop()
         
    try:    
        client.on_connect = on_connect
        client.on_publish = on_publish

        # Replace this with 3rd party cert if that was used when creating registry
        client.tls_set(ca_certs=root_cert_filepath)
        client.connect('mqtt.googleapis.com', 443)
        
        if(faces_list):
            publishUsuario(faces_list)
        elif(temper_list):
            publishTemperatura(temper_list)
    except ConnectionError:
        print("No hay conexion a la nube")
        pass
  
  

if __name__=="__main__":   
    try:
            #Temperatura()
        Puertas()
    except KeyboardInterrupt:
        pass