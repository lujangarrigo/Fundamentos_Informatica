#Escribir una función que lea un string y devuelva un diccionario con la cantidad de apariciones de cada 
#carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string 
#es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).
string = "Hola, te envío este mensaje para avisarte que el martes se recuperará la clase de Contabilidad, saludos."
lista_caracteres=list(string)
print(lista_caracteres)
def funcion(string):
    lista_caracteres=list(string)
    dict={}
    for i in lista_caracteres:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict

print(funcion(string))
