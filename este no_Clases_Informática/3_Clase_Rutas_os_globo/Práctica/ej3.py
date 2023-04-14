#!/usr/bin/env python3
#Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima
#las n últimas.

def ultimas_n_lineas(n,archivo):
    with open(archivo, 'r') as file:
        lineas = file.readlines() #Guarda todas las lineas en una lista
        print("Las últimas", n, "líneas del archivo son:")
        for linea in lineas[-n:]:
            print(linea.strip())  # Imprime las últimas n líneas de la lista

ultimas_n_lineas(2,"archivo1.txt")