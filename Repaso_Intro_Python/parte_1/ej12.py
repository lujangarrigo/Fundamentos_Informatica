
# Ejercicio 12: Escribir una función que reciba como parámetro un string y nos diga si el string
# empieza con "Buenos" o "Buenas".
# (Hecho en clase)
def funcion_12 (palabra):
   if palabra.startswith("Buenos"):
      return "La palabra empieza con Buenos"
   elif palabra.startswith("Buenas"):
      return "La palabra empieza con Buenas"
print(funcion_12("Buenosdias"))


def empieza(palabra2):
   return palabra2.starstwith("Buenos") or palabra2.startswith ("Buenas")

