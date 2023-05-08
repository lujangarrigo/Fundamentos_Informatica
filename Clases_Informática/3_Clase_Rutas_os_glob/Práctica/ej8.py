#!/usr/bin/env python3
#Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

def contenido_2_documentos_en_otro(archivo_entrada1, archivo_entrada2,documento_salida):
    with open(archivo_entrada1, 'r') as archivo1, open(archivo_entrada2, 'r') as archivo2:
        contenido1 = archivo1.read()
        contenido2 = archivo2.read()
    with open(documento_salida, 'w') as archivo_salida:
        archivo_salida.write(contenido1)
        archivo_salida.write(contenido2)

contenido_2_documentos_en_otro("archivo1.txt","archivo2.txt","archivo_ej8.txt")