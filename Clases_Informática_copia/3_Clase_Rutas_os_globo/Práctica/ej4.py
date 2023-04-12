#!/usr/bin/env python3
#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

def contador_palabras(archivo):
    with open(archivo, 'r') as file:
        contenido = file.read() # Lee el contenido del archivo y lo convierte en una sola cadena
        palabras = contenido.split() # Divide el contenido en palabras (split divide por espacios en blanco)
        cantidad_palabras = len(palabras) #Cuenta la cantidad de palabras
        print(f"El archivo contiene {cantidad_palabras} palabras.")

contador_palabras("archivo1.txt")