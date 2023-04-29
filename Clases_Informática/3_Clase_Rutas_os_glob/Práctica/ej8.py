#!/usr/bin/env python3
#Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

def contenido_2_documentos_en_otro(documento_salida):
    with open('archivo2.txt', 'r') as archivo1, open('archivo3.txt', 'r') as archivo2:
        contenido1 = archivo1.read()
        contenido2 = archivo2.read()
    with open(documento_salida, 'w') as archivo_salida:
        archivo_salida.write(contenido1)
        archivo_salida.write(contenido2)

contenido_2_documentos_en_otro("archivo_salida2.txt")