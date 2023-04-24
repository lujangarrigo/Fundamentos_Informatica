#Ejercicio 13
#Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
import re
def reemplazo(string):
    patron = r"^[\W]{2}"
    return re.sub(patron, "__", string)
print(reemplazo("$$manzanas"))