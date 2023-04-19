#!/usr/bin/env python3
# Ejercicio 15: Escribir una función que tome como parámetro una frase y nos diga
# cuántas "a" (o "A") hay en la frase, utilizando for.

def contador_de_a(frase):
   contador = 0
   for caracter in frase:
      if caracter == "a" or caracter == "A":
         contador += 1
      else:
         pass
   return contador

print(contador_de_a("Ramiro esta tosiendo"))
