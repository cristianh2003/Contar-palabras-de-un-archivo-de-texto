# NOTA: solo funciona con un archivo .txt y 
# este tiene que estar alojado en la misma 
# ubicacion que el codigo

from itertools import count


name = input("Ingrese el nombre del archivo: ")
archivo = open(name)


cuenta = dict()
for line in archivo :
    palabras = line.split()
    for palabra in palabras:
        cuenta[palabra] = cuenta.get(palabra, 0) + 1

for i in cuenta.items() :
    print(i)