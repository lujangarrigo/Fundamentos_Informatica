#!/usr/bin/env python3
#Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima
#las n últimas.

# Abre el archivo en modo lectura
with open('archivo1.txt', 'r') as archivo:
    # Lee todas las líneas del archivo y guárdalas en una lista
    lineas = archivo.readlines()
    print(lineas)

# Imprime las últimas 5 líneas de la lista
    print("Las últimas 5 líneas del archivo son:")
# 0, 1, 2   neg: -5, -4, -3, -2, -1
    for linea in lineas[-5:-1]:
        print(linea.strip())