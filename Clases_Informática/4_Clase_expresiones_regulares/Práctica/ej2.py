#Ejercicio 2
#Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son
# a-z, A-Z y 0-9
import re
def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z0-9]+', string)) 
print(caracteres_permitidos("Hola"))

print(re.search('[a-zA-Z0-9]+', "Hola23"))
