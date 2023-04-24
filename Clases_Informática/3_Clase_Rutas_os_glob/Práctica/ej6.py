#!/usr/bin/env python3
#Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

# Abrimos el archivo de entrada en modo lectura
with open('archivo1.txt', 'r') as archivo_entrada:
    # Leemos todo el contenido del archivo
    contenido = archivo_entrada.read()

# Eliminamos los saltos de línea utilizando el método replace
contenido_modificado = contenido.replace('\n',' ')

# Abrimos el archivo de salida en modo escritura
with open('archivo_salida2.txt', 'w') as archivo_salida:
    
   
# Escribimos el contenido modificado en el archivo de salida
    archivo_salida.write(contenido_modificado)