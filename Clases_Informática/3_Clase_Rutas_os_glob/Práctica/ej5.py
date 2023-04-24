#!/usr/bin/env python3
#Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y
#lo guarde en otro archivo.

# Abrimos el archivo de entrada en modo lectura
with open('archivo1.txt', 'r') as archivo:
    # Leemos todo el contenido del archivo
    contenido = archivo.read()

# Reemplazamos la letra 'a' por 'a\n'
contenido_modificado = contenido.replace('a', 'a\n')

# Abrimos el archivo de salida en modo escritura
with open('archivo_salida.txt', 'w') as archivo_salida:
    # Escribimos el contenido modificado en el archivo de salida
    archivo_salida.write(contenido_modificado)