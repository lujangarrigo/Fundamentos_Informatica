#!/usr/bin/env python3
# Ejercicio 14: Escribir una función que nos diga si un número es par, impar o cero.
def par(numero):
   if numero % 2 == 0:
      return "Es par"
   elif numero == 0:
      return "Es 0"
   else:
      return "Es impar"
print(par(0))
