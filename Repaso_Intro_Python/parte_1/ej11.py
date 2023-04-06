#!/usr/bin/env python3
# Ejercicio 11: Escribir una función que tome como parámetro un string y que, si empieza con la letra "H",
#  nos devuelva la longitud del string.
# # (Hecho en clase)
def empieza_con_H (palabra):
   if palabra.startswith("H"): #también se puede usar str.startswith(palabra,"H")
      return  len(palabra)
   else:
      return ("La palabra no empieza con H")


print(empieza_con_H("Hola"))


# Otra forma
def empieza_con_H2 (palabra):
   if palabra[0] == "H":
      return  len(palabra)
   else:
      return "La palabra no empieza con H"
