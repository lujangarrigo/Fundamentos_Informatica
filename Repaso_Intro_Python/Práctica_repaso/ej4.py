#!/usr/bin/env python3
#Realizá un programa que a partir de una lista mixta (que contiene distintos tipos de datos) imprima cuántos enteros
#tiene y además en el caso de los elementos que sean strings hay que crear una nueva lista con estos strings pero 
#reemplazando al A por la U (tanto mayúscula como minúscula) y luego imprimir estos elementos.

lista_mixta = ["hola", 26, "chau", 39, 2, "buenas"]
def strings_numeros(lista):
    numeros = []
    strings = []
    for elemento in lista:
        if isinstance(elemento, int):
            numeros.append(elemento)
        else:
            nuevo_string = elemento.replace("a", "u").replace("A", "U")
            strings.append(nuevo_string)
    print(numeros,strings)
strings_numeros(lista_mixta)