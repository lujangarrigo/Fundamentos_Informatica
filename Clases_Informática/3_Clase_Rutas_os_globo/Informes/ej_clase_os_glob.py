#!/usr/bin/env python3
"""El shebang le dice a la computadora con qué ejecutar el script"""
#Ej hecho por el profesor
"""Escribir un script en el que debemos movernos a la carpeta Informes y obtener los archivos *.txt 
que hayan allí. Por cada archivo hay que obtener, por un lado, cuantas veces aparece la palabra "estado" 
y por otro lado la cantidad de líneas. Por último, hay que crear una carpeta que se llame Apellidos, donde
 hay que crear un archivo llamado Lista.txt que contenga en cada línea la primera línea de cada archivo .txt 
 obtenida anteriormente."""
import os, glob, sys

def ejercicio_rutas():
    os.chdir("Informes") #Suponemos que estamos en la carpeta, si está carpetas arriba se hace ../../
    txt = glob.glob("*.txt")
    cantidad_estado = [] #va a contar la cantidad que hay "estado" en cada archivo
    cantidad_lineas = [] #cuenta la cantidad de lineas de cada archivo
    for archivo in txt: 
        with open(archivo,"r") as file: #abrimos los archivos
            file_completa = file.read() #readline se usa en for pq lee una linea y pasa a la otra, va a contar si estado está dos veces en una linea (readlines no)
            cantidad_estado.append(file_completa.count("estado"))
            cantidad_lineas.append(file_completa.count("\n"))
    os.mkidr("Apellido")
    with open("Apellido/Lista.txt","w") as salida: #usamos salida cuando abrimos un archivo.txt que vamos a escribir
        for archivo in txt:
            with open(archivo,"r") as file: #file es la variable q usamos al abrir un archivo.txt q vamos a leer
                salida.write(file.readline())
    return cantidad_estado , cantidad_lineas
#Se ejecuta desde bash poniendo python ej1 + tab
c1, c2 = ejercicio_rutas()
