#!/usr/bin/env python3
#Escribí un programa de python que imprima un diccionario cuyas claves sean los números de 1 a 15 y cuyos valores 
#sean las potencias al cuadrado de estos números.


def diccionario_potencias():
    diccionario = {}
    for i in range(1, 16):
        diccionario[i] = i ** 2
    print(diccionario)
diccionario_potencias()