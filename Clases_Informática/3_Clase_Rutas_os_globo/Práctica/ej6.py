#!/usr/bin/env python3
#Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

def eliminar_saltos_linea(archivo):
    with open(archivo, 'r') as archivo_entrada:
        contenido = archivo_entrada.read()
    contenido_modificado = contenido.replace('\n',' ') # Elimina los saltos de línea utilizando el método replace
    with open('archivo_salida_eliminar_saltos_linea.txt', 'w') as archivo_salida: 
        archivo_salida.write(contenido_modificado) # Escribe el contenido modificado en el archivo de salida
eliminar_saltos_linea("archivo1.txt")