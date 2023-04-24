#a)
import re
def caracteres_permitidos(string):
    return bool(re.search('X*ab*Y', string)) 
print(re.search("X*Y", "YabhdkabX"))
print(caracteres_permitidos("YabhdkabX"))

#b) 
def funcionDeExpresiones_Regulares():
    return re.findall("ag(\d.*?)cta")

# El nombre no respeta las convenciones de python porque se utilizan "_" como espacios y no se suelen usar las mayusculas en codigo python, deberia ser asi: funcion_de_expresiones_regulares.
# Además, no se suele nombrar a las funciones con la palabra funcion porque ya se conoce que el def se utiliza para establecer funciones
# Y por último se puede corregir que el tema es Expresiones Regulares, pero la funcion sirve para buscar un determinado conjunto de caracteres, con lo cual, la funcion deberia indicar qué se está intentando buscar

#