#!/usr/bin/env python3
#Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. 
#Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con 
#respecto a la cantidad total de palabras.

from collections import Counter
palabra = "Pero"
# Abrimos el archivo en modo lectura
with open('archivo1.txt', 'r') as archivo:
    contenido = archivo.read()
    palabras = contenido.split()
    cantidad_total_palabras = len(palabras)
    lista = []
    for palabra in palabras:
        frecuencia = palabras.count(palabra)
        frecuencia_real = frecuencia / cantidad_total_palabras
        lista.append(f"La palabra '{palabra}' aparece {frecuencia} veces, con una frecuencia relativa de {frecuencia_real:.2%}")
print(lista)
