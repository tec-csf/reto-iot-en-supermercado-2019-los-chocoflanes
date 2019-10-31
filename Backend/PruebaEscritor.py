import RPi.GPIO as GPIO
import sys
sys.path.append("/home/pi/MFRC522-python")
from mfrc522 import SimpleMFRC522

almacen = "/mnt/c/Users/danie/Programacion/5to Semestre/Semana i/reto-iot-en-supermercado-2019-los-chocoflanes/Sensores/Almacen.csv"

reader=SimpleMFRC522()

headers = []
id = []
cant = []
filedata = []

idNovo=int(input("Id del producto: "))
id,idNovo=reader.write(idNovo)
nomProd = input("Nombre del producto: ")
print("Acerca el tag al sensor")
print(idNovo)
print(nomProd)

with open(almacen, "r") as file:
    header = file.readline()
    for line in file:
        if len(line) > 1:
            row = line.strip().split(',')
            filedata.append(row)
            
            idProd = int(row[0])
            cantProd = int(row[-1])

            id.append(idProd)
            cant.append(cantProd)
    print(id)

if idNovo in id:
    print("Se ingresará un alimento nuevo")
    #id.index(idProd)
    id.index(idNovo)
    index = id.index(idNovo)
    cant[index] = cant[index]+1
    filedata[index][2] = (str(cant[index]))
    print("Salida try 2")
    
    with open(almacen, 'w') as file:
        file.write(header)
        for line in filedata:
            file.write(",".join(line)+"\n")
            #file.write("\n")

else:
    print("Entra al try")
    #print(id)
    print(idNovo)
    id.append(idNovo)
    index = id.index(idNovo)
    #cant[index] = 1
    with open(almacen, 'a') as file:
        file.write("\n"+(str(idNovo))+","+nomProd +",1\n")

print(filedata)
