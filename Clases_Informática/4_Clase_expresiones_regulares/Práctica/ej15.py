#Ejercicio 15
#Realizá un programa que valide si una cuenta de mail está escrita correctamente.


import re
def mail(string):
    patron = "^.+@gmail\.com$"
    return bool(re.search(patron, string))
print(mail("lujan_garrigo@gmail.com"))