#Ejercicio 1
#Escribí un programa que verifique si un string tiene al menos un carácter permitido. 
#Estos caracteres son a-z, A-Z y 0-9.
import re
def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z]', string)) #Transformo el resultado en booleano (true o false) todo valor vacío es true
"""print(bool(4)) #Devuelve true
print(bool(None)) #Devuelve falso"""
print(caracteres_permitidos("ABCja578"))
print(re.search('[a-zA-Z]', "ABCja578"))