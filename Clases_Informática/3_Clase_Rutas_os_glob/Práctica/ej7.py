#!/usr/bin/env python3
#Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y 
#decir cuantos caracteres tiene.
def palabra_mas_larga(archivo):
    with open(archivo,"r") as arch_entrada:
        palabras = arch_entrada.read().split()
        palabra_mas_larga = []
        for palabra in palabras:
            if len(palabra)>len(palabra_mas_larga):
                palabra_mas_larga = palabra
            cantidad_caracteres = len(palabra_mas_larga)
        print(f"La palabra más larga es {palabra_mas_larga}, tiene {cantidad_caracteres} caracteres")
palabra_mas_larga("archivo1.txt")