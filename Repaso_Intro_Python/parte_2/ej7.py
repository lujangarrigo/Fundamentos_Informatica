#Modificá la función anterior para que además imprima los caracteres que no aparecen en la cadena, 
#pero con el valor 0.
string = "Hola, te envío este mensaje para avisarte que el martes se recuperará la clase de Contabilidad, saludos."

def funcion(string):
    string_letras = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z"
    lista_letras = string_letras.split(" ")
    lista_caracteres=list(string)
    dict={}
    string_letras = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z"
    for i in lista_letras:
        if i in lista_caracteres:
            if i in dict:
              dict[i]+=1
            else:
             dict[i]=1
        else:
            dict[i]=0
    return dict
print(funcion(string))
