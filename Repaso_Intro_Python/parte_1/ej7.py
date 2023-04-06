#!/usr/bin/env python3
#Ejercicio 7: Reescribir la función del punto anterior considerando, además,
# que la longitud de onda no puede ser 314.5 porque ya está ocupada por otra radio (no se puede usar if).
def radio2(longitud):
   return 223 <= longitud <= 586.8 and longitud != 314.5
print(radio2(314.5))

