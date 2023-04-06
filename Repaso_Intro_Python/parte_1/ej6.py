#!/usr/bin/env python3

#Ejercicio 6: Escribir una función que determine si una longitud de onda de una radio está
# dentro o fuera del rango de recepción de una antena. La longitud de onda mínima que recibe
#  la antena es 223.0 y la máxima es 586.8 (no se puede usar if).
def radio(longitud):
   return 223 <= longitud <= 586.8
print(radio(20))