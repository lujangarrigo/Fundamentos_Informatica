#!/usr/bin/env python3
#Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y 
#decir cuantos caracteres tiene.

def palabra_mas_larga(archivo):
    with open('archivo1.txt', 'r') as file:
        contenido = file.read() # Lee todo el contenido del archivo y lo almacena en una variable
    palabras = contenido.split() # Separa el contenido en palabras usando el método split
    palabra_mas_larga = [] # Lista para almacenar la palabra más larga
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    print("La palabra más larga es:", palabra_mas_larga, "Tiene", len(palabra_mas_larga), "caracteres.")

palabra_mas_larga("archivo1.txt")