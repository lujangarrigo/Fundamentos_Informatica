#!/usr/bin/env python3
#Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

def concatenar_archivos(archivo1, archivo2):
    with open(archivo1, 'r') as file1, open(archivo2, 'r') as file2:
        contenido1 = file1.read()
        contenido2 = file2.read()
    with open('archivo_salida_concatenar.txt', 'w') as archivo_salida:
        archivo_salida.write(contenido1)
        archivo_salida.write(contenido2)
concatenar_archivos("archivo1.txt","archivo2.txt")