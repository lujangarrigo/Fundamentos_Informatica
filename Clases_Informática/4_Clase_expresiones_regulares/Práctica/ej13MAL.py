#Ejercicio 13
#Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
import re
def reemplazo(string):
    patron = r"^[\W]{0,3}"
    return re.sub(patron, "_", string)
print(reemplazo("$$manzanas"))