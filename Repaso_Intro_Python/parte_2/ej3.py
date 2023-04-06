#!/usr/bin/env python3
#Ej 3: Definir una función que dada una lista y un elemento devuelva la posición de este elemento en la lista.

def posición (lista, elemento):
   for i in range(0,len(lista)):
      if lista[i] == elemento:
        return lista.index(elemento)
      else:
         pass

lista=["hola", "chau"]

print(posición(lista,"hola"))