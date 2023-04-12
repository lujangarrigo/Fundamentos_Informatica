#!/usr/bin/env python3
#Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo
# dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.

import os, glob

# Definimos la ruta de la carpeta que contiene los archivos de texto
carpeta1 = "Práctica"

# Definimos el nombre del archivo de salida y su ubicación en la carpeta "Resultado"
archivo_salida = os.path.join(carpeta1, "Resultado", "todos_los_archivos.txt")

# Creamos la carpeta "Resultado" si no existe
if not os.path.exists(os.path.join(carpeta1, "Resultado")):
    os.makedirs(os.path.join(carpeta1, "Resultado"))

# Abrimos el archivo de salida en modo escritura
with open(archivo_salida, "w") as archivo:
    
# Recorremos todos los archivos en la carpeta "Carpeta1"
    for archivo_nombre in os.listdir(carpeta1):
# Comprobamos si el archivo es un archivo de texto  
        if archivo_nombre.endswith(".txt"): 
                txt = glob.glob("*.txt")
# Leemos el contenido del archivo y lo escribimos en el archivo de salida 
                with open(os.path.join(carpeta1, archivo_nombre), "r") as archivo_lectura:
                    contenido = archivo_lectura.read()
                    archivo.write(contenido)