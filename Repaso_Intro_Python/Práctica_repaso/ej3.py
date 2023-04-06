#!/usr/bin/env python3
#Escribí un programa que obtenga, a partir de una lista de strings, una lista con la longitud de esas strings e imprima
# la longitud de la lista de strings y los elementos de la lista de longitudes.
lista_strings = ["hola", "que tal", "cómo estás", "buen día"]

def longitud_strings(lista_strings):
    lista_longitud = []
    for i in lista_strings:
        longitud = len(i)
        lista_longitud.append(longitud)
    print("La lista de strigs es: ", lista_strings, "La lista de longitudes es: ", lista_longitud)
longitud_strings(lista_strings)