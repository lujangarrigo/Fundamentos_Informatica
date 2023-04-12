#!/usr/bin/env python3
#Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima
#las n últimas.

def read_n_back_lines(n, archivo):
    texto = open(archivo, "r").readlines()
    for i in range((len(texto)-n), len(texto)): # estructura: range(inicio,fin)
        print(texto[i]) #imprimimos esa linea del texto

read_n_back_lines(2,"archivo1.txt")