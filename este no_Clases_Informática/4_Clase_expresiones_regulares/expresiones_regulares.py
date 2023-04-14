#!/usr/bin/env python3
import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "[a-z]{3}"
print(re.search(patron, texto).group()) #Busca la primera aparición que hay
print(texto[22:26])
print(re.match(patron, texto)) #Busca coincidencias solo al principio del texto
#Como no está al principio del texto, me devuelve none
print(re.findall(patron, texto)) #Devuelve una lista con todas las apariciones del patrón
