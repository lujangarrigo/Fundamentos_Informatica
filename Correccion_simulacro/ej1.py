import re
#a)
def entre_X_Y_con_ab(string):
    patron = "X(\w*ab\w*?)Y"
    return re.findall(patron,string)

print(entre_X_Y_con_ab("XbaaaYjXababYqXbabbbbaaYqXffeeeY"))

#abab   babbbaa


#Si no se puede: "X[^XY]*ab[^XY]Y"

#"X(\w*?ab\w*?)Y" ESTA BIEN
#XacXlabclY


#b) 
def funcionDeExpresiones_Regulares():
    return re.findal("ag(\d.*?)cta")

"""
i. Falso, le falta un parámetro, y el nombre deberia ser: funcion_de_expresiones_regulares (convencion de python) 
o funcionDeExpresiones_regulares- Además el nombre debe expresar qué va a hacer, no se debe especificar que es funcion
Deberia ser entre_ag_y_cta

ii. Es error es AtributeError porque tiene una sola l

iii. Falso porque debería haber ag y un número, seguido de cualquier cosa. (no va a devolver eso pq no hay números).
Para que de eso debemos escribir así a la función:
"""

def funcionDeExpresiones_Regulares1(string):
    return re.findall("ag([^\d]*)cta",string) # o "ag(\D*)cta"

print(funcionDeExpresiones_Regulares1("aabocaggaaactazu4lggaasag24gra1ndecta"))
"""
iv. Verdadero, devuelve eso porque busca ag + un caracter numérico + cualquier cosa 0 o más veces.
"""

def funcionDeExpresiones_Regulares2(string):
    return re.findall("ag(\d.*?)cta",string)

print(funcionDeExpresiones_Regulares2("aabocaggaaactazu4lggaasag24gra1ndecta"))