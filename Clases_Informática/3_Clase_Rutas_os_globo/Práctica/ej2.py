#!/usr/bin/env python3
#Escribí un programa que lea un archivo e imprima las primeras n líneas.

def imprimir_primeras_n_lineas(archivo, n):
    with open(archivo, 'r') as f:
        for i in range(n):
            linea = f.readline().strip() #strip () elimina el renglon en blanco que separa c/linea
            print(linea)

imprimir_primeras_n_lineas('archivo1.txt', 2)