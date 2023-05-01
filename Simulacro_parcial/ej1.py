#a)
import re
def entre_X_Y_con_ab(string):
    return re.findall("X(\w?ab\w*?)Y",string)
print(entre_X_Y_con_ab("XbaaaYjXababYqXbabbbbaaYqXffeeeY"))


#b) 
def funcionDeExpresiones_Regulares():
    return re.findall("ag(\d.*?)cta")

#1. Incorrecta: El nombre no respeta las convenciones de python porque se utilizan "_" como espacios y no se suelen usar las mayusculas en codigo python, deberia ser asi: funcion_de_expresiones_regulares.
# Además, no se suele nombrar a las funciones con la palabra funcion porque ya se conoce que el def se utiliza para establecer funciones
# Y por último se puede corregir que el tema es Expresiones Regulares, pero la funcion sirve para buscar un determinado conjunto de caracteres, con lo cual, la funcion deberia indicar qué se está intentando buscar

#2: Incorrecta: La funcion al ser ejecutada no devuelve nada en la terminal porque no se ha utilizado, se deberia utilizar haciendo print(funcionDeExpresiones_Regulares) e igualmente no va a devolver nada porque le falta el string en el que va a buscar el patron

#3: Incorrecta: la función no tiene ningún error de "sintax", a pesar de que no funcione como se desea, está escrita corretamente, cuando se ejecuta no devuelve nada

def funcionDeExpresiones_Regulares(string):
    return re.findall("ag(\d.*?)cta",string)

print(funcionDeExpresiones_Regulares("aabocaggaaactazu4lggaasag24gra1ndecta"))

#4: Incorrecto: devuelve ['24gra1nde'] porque busca lo que está encerrado por ag y cta, pero con mínimo un digito luego de ag

#5: Correcto