
# Ejercicio 13: Escribir una función llamada es_multiplo que reciba dos números
# y diga si el segundo es múltiplo del primero


def es_múltiplo(num1,num2):
   if num2 % num1 == 0:
      return "El segundo es múltiplo del primero"
   else:
      return "El segundo NO es múltiplo del primero"
print(es_múltiplo(3,7))

