#!/usr/bin/env python3
#ej 1: Realizá un programa que lea un archivo e imprima con líneas de ese archivo no empiecen con una letra
# determinada (por ejemplo, que imprima líneas no empiecen con "P").
def start_with(letra,archivo):
    count=0
    with open(archivo,"r") as archivo:
        for linea in archivo:
            if (linea[0] != letra.lower() or linea[0] != letra.upper()):
                count += 1
    print("El número de líneas que no empiezan con", letra, "es", count)

start_with("H","archivo1.txt")