#!/usr/bin/env python3
#Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

# Abrimos los dos archivos en modo lectura
with open('archivo2.txt', 'r') as archivo1, open('archivo3.txt', 'r') as archivo2:
    contenido1 = archivo1.read()
    contenido2 = archivo2.read()

# Abrimos un tercer archivo en modo escritura
with open('archivo_salida2.txt', 'w') as archivo_salida:

# Escribimos el contenido de ambos archivos en el archivo de salida
    archivo_salida.write(contenido1)
    archivo_salida.write(contenido2)