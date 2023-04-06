#!/usr/bin/env python3
# Ejercicio 15: Escribir una función que tome como parámetro una frase y nos diga
# cuántas "a" (o "A") hay en la frase, utilizando for.

def contar(frase):
   cantidad = 0
   for i in frase:
      if i == "a" or i == "A":
        cantidad = cantidad + 1
        return cantidad

#No me dio bien
print(contar("Hola como estas Ana?"))

