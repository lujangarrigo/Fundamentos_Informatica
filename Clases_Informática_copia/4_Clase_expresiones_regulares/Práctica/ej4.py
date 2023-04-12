#Ejercicio 4
#Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).
import re   
def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron, string) is not None:
        return "Patrón encontrado"
    else:
        return "Patrón no encontrado"
#cadena = input("ingresa una cadena: ")
