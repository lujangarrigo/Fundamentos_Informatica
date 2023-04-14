#Ejercicio 8
#Escribí un programa que separe y devuelva los caracteres númericos de un string.
import re
def extraer_numeros(string):
    resultado = re.split("\D+", string)
    for elemento in resultado:
        print(elemento)
string = "Hoy movimos 10 cajas de lugar, en 3 edificios distintos para llevar a 12 casas"
print(extraer_numeros(string))