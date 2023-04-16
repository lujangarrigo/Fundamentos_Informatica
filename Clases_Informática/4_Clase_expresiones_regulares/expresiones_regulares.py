#!/usr/bin/env python3
import re
texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*)sit" #prioriza los matches externos
#print(re.search(patron, texto).group()) #Busca la primera aparición que hay
#print(re.match(patron, texto)) #Busca coincidencias solo al principio del texto
#Como no está al principio del texto, me devuelve none
#print(re.findall(patron, texto)) #Devuelve una lista con todas las apariciones del patrón
#print(re.search(patron, texto), "\n")
print(re.search(patron, texto).group()) #es lo mismo dejar el paréntesis vacío o un 0
print(re.search(patron, texto).group(0))
print(re.search(patron, texto).group(1)) #nos quedamos con lo que está entre ipsum y sit
