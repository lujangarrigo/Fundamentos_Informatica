#!/usr/bin/env python3
#Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y 
#decir cuantos caracteres tiene.
# Abrimos el archivo en modo lectura
with open('archivo1.txt', 'r') as archivo:

# Leemos todo el contenido del archivo y lo almacenamos en una variable
    contenido = archivo.read()

# Separamos el contenido en palabras utilizando el método split
palabras = contenido.split()

# Inicializamos una variable para almacenar la palabra más larga
palabra_mas_larga = []

# Iteramos sobre todas las palabras para encontrar la más larga
for palabra in palabras:
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra

# Imprimimos la palabra más larga y su longitud
print("La palabra más larga es:", palabra_mas_larga)
print("Tiene", len(palabra_mas_larga), "caracteres")