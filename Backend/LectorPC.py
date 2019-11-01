import RPi.GPIO as GPIO
import sys
sys.path.append("/home/pi/MFRC522-python")
from mfrc522 import SimpleMFRC522

#Path al .CSV
almacen = "/home/pi/Desktop/Semana i/reto-iot-en-supermercado-2019-los-chocoflanes/Backend/Almacen.csv"

headers = []
ids = []
cant = []
arrTemp = []
filedata = []

id, productSelect = reader.read()
print(productSelect + "a")

with open(almacen, "r") as file:
    header = file.readline()
    for line in file:
        if len(line) > 1:
            row = line.split(',')
            filedata.append(row)
            
            idProd = int(row[0])
            cantProd = int(row[-1])

            ids.append(idProd)
            cant.append(cantProd)
            arrTemp.append(int(idProd))

try:
    arrTemp.index(productSelect)
    arrTemp.remove(productSelect)
    index = ids.index(productSelect)
    if cant[index] > 0:
        cant[index] = cant[index]-1
except ValueError:
    arrTemp.append(productSelect)
    index = ids.index(productSelect)
    cant[index] = cant[index]+1

filedata[index][2] = (str(cant[index]))

with open(almacen, 'w') as file:
    file.write(header)
    for line in filedata:
        file.write(",".join(line))
        file.write("\n")

file.close()