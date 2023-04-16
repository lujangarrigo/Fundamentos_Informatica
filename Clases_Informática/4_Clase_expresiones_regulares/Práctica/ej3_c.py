#si un string dado tiene una h seguida de cero o una e.
import re   
def encontrar_patron(string):
    patron = "he?"
    if re.search(patron,string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"

print(encontrar_patron("a"))
print(encontrar_patron("h"))
print(encontrar_patron("he"))
print(encontrar_patron("heeeee"))

#Después de la e puede haber cualquier cosa