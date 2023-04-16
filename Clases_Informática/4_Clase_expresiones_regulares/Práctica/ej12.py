#Ejercicio 12
#Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).

import re
def reemplazo(string):
    patron = "[\s_:]"
    return re.sub(patron, "|", string)
print(reemplazo("Nuestro _main_ es así:"))