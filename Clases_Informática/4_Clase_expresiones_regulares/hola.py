import re

patron = "(\d{2}[\s-]*\d{4}[\s-]*\d{4})"
string = "Hola, mi celular es: 11 6630 3425, y el de mi tia es 11-2838-2930"

print(re.search(patron, string).group(1))
print(re.findall(patron,string))
print(re.match(patron,string)) #encuentra al patron solo si está al inicio de la línea