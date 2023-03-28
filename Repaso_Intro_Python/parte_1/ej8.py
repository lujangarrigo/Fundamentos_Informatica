
# Ejercicio 8: Escribir una función llamada tiene_descuento que tome como parámetro una edad y
# devuelva True en caso de que la edad sea menor o igual a 12 o mayor o igual a 60.
# En caso contrario tiene que devolver False (no se puede usar if).


def tiene_descuento(edad):
   return edad <= 12 or edad >= 60
print(tiene_descuento(12))

