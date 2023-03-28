
#Ejercicio 3: Escribir funciones que obtengan el doble del anterior y el doble del siguiente de un número.
# (Hecho en clase)
def siguiente(numero):
   return numero + 1

def anterior(numero):
   return numero - 1

def doble(numero):
   return str(doble(anterior(numero))) + " y " + str(doble(siguiente(numero)))

print(doble(4))
