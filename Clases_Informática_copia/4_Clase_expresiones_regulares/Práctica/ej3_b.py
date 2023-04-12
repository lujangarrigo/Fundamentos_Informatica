#si un string dado tiene una h seguida de una o más e.

import re
#b)
def encontrar_patron(string):
    patron = "he+"
    if re.search(patron,string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"
#Lo que estpa 0 o más veces es la "e"
print(encontrar_patron("a"))
print(encontrar_patron("h"))
print(encontrar_patron("he"))
print(encontrar_patron("heeeee"))