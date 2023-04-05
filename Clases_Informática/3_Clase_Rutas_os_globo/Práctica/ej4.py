#!/usr/bin/env python3
#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

# Abre el archivo en modo lectura
with open('archivo1.txt', 'r') as archivo:
# Lee el contenido del archivo y conviértelo en una sola cadena
    contenido = archivo.read()

# Divide el contenido en palabras y cuenta la cantidad de palabras
palabras = contenido.split()
cantidad_palabras = len(palabras)

# Imprime la cantidad de palabras del archivo
print(f"El archivo contiene {cantidad_palabras} palabras.")