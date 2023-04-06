#!/usr/bin/env python3
# Ejercicio 9: Escribir una función xor que tome como parámetro dos booleanos y
#  retorne el booleano correspondiente con la tabla.
def xor(booleano1, booleano2):
   if booleano1 == True and booleano2 == False:
      return True
   elif booleano1 == False and booleano2 == True:
      return True
   elif booleano1 == True and booleano2 == True:
      return False
   else:
      return False
   
print(xor(True,False))