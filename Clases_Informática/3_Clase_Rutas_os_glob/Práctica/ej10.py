#!/usr/bin/env python3
#Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo
# dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.

import os,glob

def contenidos_txt_en__carpeta_resultado(carpeta1):
    os.chdir(carpeta1)
    archivos_txt = glob.glob("*.txt")
    for archivo in archivos_txt:
        with open(archivo,"r") as txt:
            contenido = txt.read()
            with open("archivo_salida1.txt","a") as file:
                file.write(contenido)

contenidos_txt_en__carpeta_resultado("../Práctica")