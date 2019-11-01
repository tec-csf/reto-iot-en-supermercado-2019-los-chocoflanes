#
# IoT en el Supermercado

#### Equipo Los Chocoflanes**

#### Integrantes:

1. Luis Daniel Roa González - A01021960 - Santa Fe
2. Juan Francisco Gortarez Ricardez - A01021926 - Santa Fe
3. Gabriel Schlam Huber - A01024122 - Santa Fe
4. Luis Armando Ortiz Revilla - A01022320 - Santa Fe
5. Simón Metta Grego - A01377925 - Santa Fe

## 1. Aspectos generales

### 1.1 Requerimientos técnicos

A continuación se mencionan los requerimientos técnicos mínimos del proyecto, favor de tenerlos presente para que cumpla con todos.

* Todo el código de la solución debe estar desarrollado en Python 3.7 utilizando módulos y Programación Orientada a Objetos.
* Las lecturas de los sensores debe programarse de manera asíncrona.
* Todo el código debe incluir el manejo de excepciones y validación de errores.
* El equipo tiene la libertad de elegir los servicios cognitivos y de nube que desee utilizar, sin embargo, debe tener presente que la solución final se deberá ejecutar en una Raspberry Pi y en una de las siguientes plataformas en la nube:[Amazon Web Services](https://aws.amazon.com/),[Google Cloud Platform](https://cloud.google.com/?hl=es) o[Microsoft Azure](https://azure.microsoft.com/es-mx/).
* El proyecto debe utilizar algunos de los servicios de reconocimiento de imágenes como:[Azure Computer Vision API](https://azure.microsoft.com/es-mx/services/cognitive-services/computer-vision/),[Google Vision AI](https://cloud.google.com/vision/),[Amazon Rekognition](https://aws.amazon.com/rekognition/).
* El proyecto debe utilizar algún servicio de IoT en la nube como:[Azure IoT Hub](https://azure.microsoft.com/es-mx/services/iot-hub/),[Google IoT Core](https://cloud.google.com/iot-core/?hl=es),[Amazon IoT Core](https://aws.amazon.com/es/iot-core/).
* Para la ingesta de datos, se debe utilizar un servicio de mensajería asíncrono como[Azure Service Bus](https://azure.microsoft.com/es-mx/services/service-bus/),[Google Cloud Pub/Sub](https://cloud.google.com/pubsub/?hl=es-419),[Amazon SNS](https://aws.amazon.com/sns/).
* Para el procesamiento de los paquetes de IoT se debe utilizar un servicio como[Azure Functions](https://azure.microsoft.com/es-mx/services/functions/),[Cloud Functions](https://cloud.google.com/functions/),[Amazon Lambda](https://aws.amazon.com/lambda/).
* Para el almacenamiento de la información se debe utilizar un servicio como[Azure SQL Datawarehouse](https://azure.microsoft.com/es-mx/services/sql-data-warehouse/),[Google BigQuery](https://cloud.google.com/bigquery/?hl=es),[Amazon Redshift](https://aws.amazon.com/es/redshift/). 
Para la visualización de los datos se debe utilizar un servicio como[Azure Power BI](https://powerbi.microsoft.com/es-es/),[Google Data Studio](https://datastudio.google.com),[Amazon Quicksight](https://aws.amazon.com/quicksight/).
* La conexión entre la Raspberry Pi y el servicio de nube de IoT debe realizarse utilizando el protocolo MQTT y llaves criptográficas para la autenticación.
* La solución debe utilizar una arquitectura de microservicios. Si no tiene conocimiento sobre este tema, le recomendamos la lectura[_Microservices_](https://martinfowler.com/articles/microservices.html) de[Martin Fowler](https://martinfowler.com).
* La arquitectura debe ser modular, escalable, con redundancia y alta disponibilidad.
* La arquitectura deberá estar separada claramente por capas (_frontend_, _backend_, _API RESTful_, datos y almacenamiento).
* Los diferentes componentes del proyecto (_frontend_, _backend_, _API RESTful_, bases de datos, entre otros) pueden ejecutarse, opcionalmente, sobre contenedores[Docker](https://www.docker.com/) y utilizar[Kubernetes](https://kubernetes.io/) como orquestador.
* Todo el código, _datasets_ y la documentación del proyecto debe alojarse en este repositorio de GitHub. Favor de mantener la estructura de carpetas generada.

### 1.2 Estructura del repositorio

El proyecto debe seguir la siguiente estructura de carpetas, la cual generamos por usted:
```
- /                     # Raíz de todo el proyecto
	- README.md         # Archivo con los datos del proyecto (este archivo)
	- frontend          # Carpeta con la solución del frontend (Web app, dashboards, etc.)
	- backend           # Carpeta con la solución del backend (CMS, API, Funciones, etc.)
	- sensors           # Carpeta con los códigos que se ejecutan en el RPi
	- datasets          # Carpeta con los datasets y recursos utilizados (csv, json, audio, videos, entre otros)
	- dbs               # Carpeta con los modelos, catálogos y scripts necesarios para generar las bases de datos
	- docs              # Carpeta con la documentación del proyecto
```

### 1.3 Documentación del reto

Como parte de la entrega final del reto, se debe incluir la siguiente información:

* Justificación del modelo o servicio de _Machine Learning_ que seleccionaron.
* Descripción del o los _datasets_ y las fuentes de información utilizadas.
* Guía de configuración, instalación y despliegue de la solución tanto en la Raspberry Pi como en la plataforma en la nube seleccionada.
* El código debe estar documentado siguiendo los estándares definidos para el lenguaje de programación seleccionado.

## 2. Descripción del proyecto

Desarrollar un modelo de IoT para supermercados, específicamente para la sección de refrigeradores del mismo, que permita optimizar el manejo de los inventarios y analizar los diferentes tipos de usuarios frecuentes y sus compras, para poder tomar decisiones rápidas y adecuadas para el mercado.

Esto se realizará por medio de sensores de movimiento, apertura / cierre de puertas, temperatura, lectores de tags RFID, cámara web y leds, además del uso de Machine Learning.

## 3. Solución

A continuación aparecen descritos los diferentes elementos que forman parte de la solución del proyecto.

### 3.1 Modelos o servicios de *Machine Learning* utilizados

Nuestra solución utiliza los servicios de reconocimiento facial de Microsoft Azure para detectar la edad y el género de los compradores. Consideramos que una utilización mínima es la más adecuada para nuestras necesidades, ya que únicamente usamos estos datos para detectar tendencias de compra entre grupos de personas, e incrementar la granularidad usando elementos como raza nos pareció falto de ética.

### 3.2 Arquitectura de la solución

*[Incluya imágenes del circuito armado con los sensores conectados.]*

### 3.3 Frontend

*[Incluya aquí una explicación de la solución utilizada para el frontend del proyecto. No olvide incluir las ligas o referencias donde se puede encontrar información de los lenguajes de programación, frameworks y librerías utilizadas.]*

#### 3.3.1 Lenguaje de programación

El programa realizado fue elaborado usando _Python_ versión 3.6.8.
Para más información sobre _Python_ y sus usos, a continuación se encuentra la página web: [https://docs.python.org/3/](https://docs.python.org/3/)

#### 3.3.2 Framework

Utilizamos los frameworks de MQTT con Google Cloud Services (principalmente Data Studio) para el manejo de los datos de los sensores y su presentación.

#### 3.3.3 Librerías de funciones o dependencias

* Se usaron las siguientes librerías
	* RPi.GPIO:
		* Librería que se utiliza para controlar el GPIO en una Raspberry Pi, además de asignar los pines utilizados en el circuito.
	* sys
	* json
	* time
	* subprocess
	* datetime
	* requests
	* jwt
		* Librería que permite la comunicación del Raspberry Pi con un servicio que mande/reciba información dentro de un documento de tipo _json_. jwt significa _json web token_.
	* Adafruit\_DHT
		* Librería utilizada para poder manejar la información enviada desde el sensor de temperatura y humedad con el nombre _DHT11_ y poder manipularlo a nuestro gusto.
	* paho.mqtt.client
		* Librería utilizada para poder mandar mensajes utilizando el protocolo **MQTT** , este es un protocolo utilizado especialmente para poder conectar dispositivos que pertenezcan a una red de IoT (Internet of Things)
	* pprint
		* Librería enfocada en poder imprimir de manera correcta y eficiente la información que requerimos para poder mandarla a nuestro servicio de _Google Cloud_.
	* mfrc522
		* Librería utilizada para poder manejar los datos de cualquier tag RFID, esta librería está enfocada para que el sensor _RFID-RC522_ pueda funcionar con el Raspberry Pi 3 B+.
	* requests.exceptions

### 3.4 Backend

Se utilizaron los servicios de Azure para el análisis de las imágenes de los usuarios, para poder determinar la edad y género, y poder enviarlo a la nube.

Además, se utilizó un mismo programa en Python para la compilación de todos los sensores usados como para el envío de datos a la nube, en Google Cloud Services.

Nuestro sistema manda tres tipos de tablas diferentes:

* Usuarios, enviando la fecha y hora, edad y género.
* Temperatura del refrigerador, enviando la fecha y hora, temperatura y humedad.
* Inventario y ventas, enviando el id del producto, el nombre y la cantidad.

#### 3.4.1 Lenguaje de programación

El lenguaje de programación usado fue _Python_ versión 3.6.8.
Para más información sobre _Python_ y sus usos, a continuación se encuentra la página web: [https://docs.python.org/3/](https://docs.python.org/3/)

#### 3.4.2 Framework

Utilizamos los frameworks de Azure Cognitive Services para el reconocimiento facial, y MQTT con Google Cloud Services (Cloud Functions, IoT Core, PubSub, Data Studio) para el manejo de los datos de los sensores, almacenamiento de los mismos y su presentación.

#### 3.4.3 Librerías de funciones o dependencias

* Se usaron las siguientes librerías
	* RPi.GPIO:
		* Librería que se utiliza para controlar el GPIO en una Raspberry Pi, además de asignar los pines utilizados en el circuito.
	* sys
	* json
	* time
	* subprocess
	* datetime
	* requests
	* jwt
		* Librería que permite la comunicación del Raspberry Pi con un servicio que mande/reciba información dentro de un documento de tipo _json_. jwt significa _json web token_.
	* Adafruit\_DHT
		* Librería utilizada para poder manejar la información enviada desde el sensor de temperatura y humedad con el nombre _DHT11_ y poder manipularlo a nuestro gusto.
	* paho.mqtt.client
		* Librería utilizada para poder mandar mensajes utilizando el protocolo **MQTT** , este es un protocolo utilizado especialmente para poder conectar dispositivos que pertenezcan a una red de IoT (Internet of Things)
	* pprint
		* Librería enfocada en poder imprimir de manera correcta y eficiente la información que requerimos para poder mandarla a nuestro servicio de _Google Cloud_.
	* mfrc522
		* Librería utilizada para poder manejar los datos de cualquier tag RFID, esta librería está enfocada para que el sensor _RFID-RC522_ pueda funcionar con el Raspberry Pi 3 B+.
	* requests.exceptions

Nosotros tenemos cuatro endpoints que se conectan con la nube:

* **Azure Cognitive Services (Reconocimiento Facial):**
	* **Descripción**:
		* Se envía una solicitud con una imagen para recibir los datos característicos de la misma, como edad, tamaño de la cara, género y el formato.
	* **URL**:
		* 
	* **Headers**:
		* {&quot;Content-Type&quot;: &quot;application/octet-stream&quot;, &#39;Ocp-Apim-Subscription-Key&#39;: &#39;7e9cfbb244204fb994babd6111235269&#39;}
	* **Formato JSON del cuerpo de la solicitud**:
		* face\_uri, headers, data
		* Donde:
			* face\_uri = &quot;https://raspberrycp.cognitiveservices.azure.com/vision/v1.0/analyze?visualFeatures=Faces&amp;language=en&quot;
			* data = imagen tomada
	* **Formato JSON de la respuesta**:
		*	{'faces': [{'age': *age*,
									'faceRectangle': {'height': *height*,
																		'left': *left*,
																		'top': *top*,
																		'width': *width*},
									'gender': *'gender'*}],
			 'metadata': {'format': *'format'*, 'height': *'height'*, 'width': *'width'*},
			 'requestId': *'requestId'*}

* **Google Cloud Services #1 (Usuarios):**
	* **Descripción**:
		* Se toman los datos importantes regresados por Azure para nuestro registro y se envían a Google Cloud, junto con la fecha y hora.
	* **URL**:
		* 
	* **Formato JSON del cuerpo de la solicitud**:
		* '{{ "ts": {}, "age": {}, "gender": "{}" }}';.format(int(time.time()), faces\_list[0],faces\_list[1])
	* **Formato JSON de la respuesta**:
		*

* **Google Cloud Services #2 (Estatus Refrigerador):**
	* **Descripción**:
		* Se envían a Google Cloud los datos recibidos del sensor de temperatura, siendo la temperatura y la humedad, junto con la fecha y hora.
	* **URL**:
		* 
	* **Formato JSON del cuerpo de la solicitud**:
		* '{{ "ts": {}, "temperature": {}, "humidity": "{}" }}';.format(int(time.time()), temper\_list[0],temper\_list[1])
	* **Formato JSON de la respuesta**:
		* 

* **Google Cloud Services #3 (Estatus Almacén):**
	* **Descripción**:
		* Se envían a Google Cloud los datos del inventario en ese momento, siendo el ID de producto, el nombre del producto y la cantidad en existencia.
	* **URL**:
		*
	* **Formato JSON del cuerpo de la solicitud**:
		*
	* **Formato JSON de la respuesta**:
		* 

### 3.5 Sensores

Todos los sensores menos uno fueron consolidados en un solo programa de Python, e implementados de una manera selectivamente asíncrona. Lo que esto significa es que, en un caso de uso normal, al inicio solamente se tienen dos sensores funcionando: el detector magnético de apertura y el de temperatura. Esto prosigue hasta que se detecte una apertura de puerta: a partir de este momento, se toma una foto usando la webcam, y se empieza a detectar (asíncronamente) si la persona que abrió la puerta dejó o ingresó un producto, y también si la puerta se ha dejado abierta después que el usuario se ha ido.

Los sensores utilizados ( y la liga de donde obtuvimos su información) fueron los siguientes:
* **Temperatura/Humedad:** [https://github.com/adafruit/Adafruit\_Python\_DHT](https://github.com/adafruit/Adafruit_Python_DHT)
* **Movimiento:** [https://www.internetdelascosas.cl/2013/05/13/sensor-de-presencia-en-raspberry-pi/](https://www.internetdelascosas.cl/2013/05/13/sensor-de-presencia-en-raspberry-pi/)
* **Apertura Magnética:** [https://www.alexisabarca.com/2016/01/usar-un-sensor-de-puerta-magnetico-en-un-raspberry-pi/](https://www.alexisabarca.com/2016/01/usar-un-sensor-de-puerta-magnetico-en-un-raspberry-pi/)
* **Webcam:** [https://github.com/vcubells/iot\_supermercado/blob/master/demo\_02/01\_Sensors.py](https://github.com/vcubells/iot_supermercado/blob/master/demo_02/01_Sensors.py)
* **Lectoescritor de RFID:** [https://medium.com/coinmonks/for-beginners-how-to-set-up-a-raspberry-pi-rfid-rc522-reader-and-record-data-on-iota-865f67843a2d](https://medium.com/coinmonks/for-beginners-how-to-set-up-a-raspberry-pi-rfid-rc522-reader-and-record-data-on-iota-865f67843a2d)

#### 3.5.1 Lenguaje de programación**

El lenguaje de programación usado fue _Python_ versión 3.6.8.
Para más información sobre _Python_ y sus usos, a continuación se encuentra la página web: [https://docs.python.org/3/](https://docs.python.org/3/)

#### 3.5.2 Framework

Para los sensores no utilizamos ningún framework para su funcionamiento óptimo.

#### 3.5.3 Librerías de funciones o dependencias

Para el funcionamiento de los sensores se usaron tres librerías importantes:
	* RPi.GPIO, la cual es la librería para la utilización de los pines en la Rpi
	* mfrc522, la cual es la librería/API para la escritura y lectura de chips RFID a partir de un sensor conectado por pines
	* Adafruit, la cual es una librería general de I/O, que en este proyecto fue utilizada para el input del sensor de temperatura y humedad

### 3.6 Pasos a seguir para utilizar el proyecto

*[Incluya aquí una guía paso a paso para poder utilizar el proyecto, desde la clonación de este repositorio hasta el despliegue de la solución en una Raspberry Pi y en una plataforma en la nube.]*

## 4. Referencias
* Librería de Python
	* [https://docs.python.org/3/](https://docs.python.org/3/)
* Librería de RPi.GPIO
	* [https://pypi.org/project/RPi.GPIO/](https://pypi.org/project/RPi.GPIO/)
* Librería de jwt (_Jason Web Token_)
	* [https://pypi.org/project/jwt/](https://pypi.org/project/jwt/)
* Librería de Adafruit\_DHT
	* [https://circuitpython.readthedocs.io/projects/dht/en/latest/](https://circuitpython.readthedocs.io/projects/dht/en/latest/)
* Librería de _paho.mqtt.client_
	* [https://pypi.org/project/paho-mqtt/](https://pypi.org/project/paho-mqtt/)
* Librería de _pprint_ (_pretty print_)
	* [https://docs.python.org/3/library/pprint.html](https://docs.python.org/3/library/pprint.html)
* Librería de MFRC522
	* [https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf](https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf)
* Documentación de _Microsoft Azure Cognitive Services_
	* [https://docs.microsoft.com/en-us/azure/cognitive-services/](https://docs.microsoft.com/en-us/azure/cognitive-services/)