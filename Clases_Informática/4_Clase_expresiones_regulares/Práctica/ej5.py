#Ejercicio 5
#Escribí un programa que diga si un string empieza con un número específico.
import re
def empieza_con_numero(numero,string):
    patron = "^"+ str(numero)
    return bool(re.search(patron,string))

print(empieza_con_numero(2,"2 Bananas"))