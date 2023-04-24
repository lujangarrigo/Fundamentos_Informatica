#Ejercicio 14
#Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.
import re
def reemplazo(string):
    patron = "\s{3}"
    return re.sub(patron, ";", string)
print(reemplazo("hola   Hernán   hft   "))