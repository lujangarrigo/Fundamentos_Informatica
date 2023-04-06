#!/usr/bin/env python3
#Definir una función que dada una palabra, nos diga si el palíndromo o no.
cadena = input("Introduzca palabra: ")
def palindromo(cadena):
    inicio = 0
    fin = len(cadena) - 1
    while cadena[inicio] == cadena[fin]:
        if inicio >= fin:
            return "La palabra es palíndromo"
        inicio += 1
        fin -= 1
    return "La palabra no es palíndromo"
print(palindromo(cadena))