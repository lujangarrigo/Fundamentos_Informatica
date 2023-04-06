#!/usr/bin/env python3
#Realizá un programa que imprima la suma de todos los valores de un diccionario de números.

def suma_valores(diccionario):
    suma = 0
    for i in diccionario.values():
        suma += i
    print(suma)
diccionario = {1:20, 2:39, 3:49, 4:21}
suma_valores(diccionario)