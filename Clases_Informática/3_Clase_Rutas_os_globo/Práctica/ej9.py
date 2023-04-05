#!/usr/bin/env python3
#Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. 
#Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con 
#respecto a la cantidad total de palabras.

from collections import Counter
palabra = "Pero"
# Abrimos el archivo en modo lectura
with open('archivo1.txt', 'r') as archivo:
    
# Leemos todo el contenido del archivo y lo almacenamos en una variable
    contenido = archivo.read()

# Separamos el contenido en palabras utilizando el método split
palabras = contenido.split()

# Contamos la frecuencia de cada palabra utilizando Counter
frecuencias = Counter(palabras)

# Calculamos la cantidad total de palabras
cantidad_total_palabras = len(palabras)

# Iteramos sobre las frecuencias para imprimir la frecuencia de cada palabra
for palabra, frecuencia in frecuencias.items():
    # Calculamos la frecuencia como la relación entre la cantidad de veces que aparece la palabra y la cantidad total de palabras
    frecuencia_real = frecuencia / cantidad_total_palabras
   
# Imprimimos la palabra, su frecuencia y su frecuencia relativa
    
print(f"La palabra '{palabra}' aparece {frecuencia} veces, con una frecuencia relativa de {frecuencia_real:.2%}")