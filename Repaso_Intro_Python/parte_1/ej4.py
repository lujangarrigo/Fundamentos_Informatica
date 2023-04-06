#!/usr/bin/env python3
#  Ejercicio 4: Escribir una función llamada retirar_dinero, que tenga como parámetros el saldo y el monto
#  a retirar y que devuelva cuánto saldo queda luego de la extracción.
# Si retira más dinero que lo que tiene en el saldo debe devolver 0 (no se puede usar if).
# (Hecho en clase)
def retirar_dinero (saldo, monto):
   return max(saldo-monto, 0) #va a devolver el mayor de esos dos


print(retirar_dinero(4,6))

