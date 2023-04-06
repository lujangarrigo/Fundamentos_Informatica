#!/usr/bin/env python3
#Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. 
#Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con 
#respecto a la cantidad total de palabras.

from collections import Counter
palabra = "Pero"
with open('archivo1.txt', 'r') as archivo:
    contenido = archivo.read()
palabras = contenido.split()
frecuencias = Counter(palabras) # Contamos la frecuencia de cada palabra utilizando Counter
cantidad_total_palabras = len(palabras)
for palabra, frecuencia in frecuencias.items(): # Iteramos sobre las frecuencias para imprimir la frecuencia de cada palabra
    frecuencia_real = frecuencia / cantidad_total_palabras #Calculamos la frecuencia real

print(f"La palabra '{palabra}' aparece {frecuencia} veces, con una frecuencia relativa de {frecuencia_real}")