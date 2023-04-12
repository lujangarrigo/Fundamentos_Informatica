#!/usr/bin/env python3
#Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y
#lo guarde en otro archivo.

def remplazo(letra, archivo):
    with open(archivo, 'r') as file:
        contenido = file.read() #lee todo el contenido del archivo
    contenido_modificado = contenido.replace(letra, letra + "\n")
    with open('archivo_salida_remplazo.txt', 'w') as archivo_salida:
        archivo_salida.write(contenido_modificado) # Escribimos el contenido modificado en el archivo de salida

remplazo("a", "archivo1.txt")