#Ejercicio 7
#Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.

import re
def minusc_mayusc_espacios_num(string):
    patron = "[a-zA-Z0-9 ]+"
    return bool(re.search(patron,string))

print(minusc_mayusc_espacios_num("Para la persona numero 3"))