#!/usr/bin/env python3
#Ejercicio 3: Escribir funciones que obtengan el doble del anterior y el doble del siguiente de un número.
# (Hecho en clase)
def siguiente(numero):
   return numero + 1

def anterior(numero):
   return numero - 1

def doble1(numero):
   return numero * 2


def doble2(numero):
   return str(doble1(anterior(numero))) + " y " + str(doble1(siguiente(numero))) 
#str se usa para convertir el número en string y poder concatenar strings con el +

print(doble2(4))

