#!/usr/bin/env python3
#Definir una función llamada productoria que toma como parámetro una lista de números y los multiplica a todos.
lista=[1,4,7,3,9]
producto=1
def productoria(lista,producto):
    for i in lista:
        producto = producto * i
    return producto
print(productoria(lista,producto))