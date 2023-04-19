#!/usr/bin/env python3
#ejercicio 5: Escribir una función llamada dia_de_la_semana_favorito que tome como parámetro
# un día de la semana y devuelve True si el día es "Sábado" o False si es cualquier otro (no se puede usar if).
# (Hecho en clase)

def dia_de_la_semana_favorito(dia):
   return dia == "Sábado"

print(dia_de_la_semana_favorito("Sábado"))
print(dia_de_la_semana_favorito("Viernes"))
