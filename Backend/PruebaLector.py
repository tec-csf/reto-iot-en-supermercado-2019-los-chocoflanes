#hecho para el demo
productSelect = 2

#Path al .CSV
almacen = "/mnt/c/Users/danie/Programacion/5to Semestre/Semana i/reto-iot-en-supermercado-2019-los-chocoflanes/Backend/Almacen.csv"

headers = []
id = []
cant = []
arrTemp = []
filedata = []

with open(almacen, "r") as file:
    header = file.readline()
    for line in file:
        if len(line) > 1:
            row = line.split(',')
            filedata.append(row)
            
            idProd = int(row[0])
            cantProd = int(row[-1])

            id.append(idProd)
            cant.append(cantProd)
            arrTemp.append(int(idProd))

try:
    arrTemp.index(productSelect)
    arrTemp.remove(productSelect)
    index = id.index(productSelect)
    if cant[index] > 0:
        cant[index] = cant[index]-1
except ValueError:
    arrTemp.append(productSelect)
    index = id.index(productSelect)
    cant[index] = cant[index]+1

filedata[index][2] = (str(cant[index]))

with open(almacen, 'w') as file:
    file.write(header)
    for line in filedata:
        file.write(",".join(line))
        file.write("\n")

file.close()