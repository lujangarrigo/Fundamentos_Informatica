#Escribir una función que tome como parámetro una lista de enteros y devuelva una lista con valores booleanos 
#que indique si cada elemento es par o impar. Por ejemplo, para la lista [2, 45, 108, 12, 7], la función
#debería retornar [True, False, True, True, False]. Utilizar la función realizada en la práctica anterior.

lista = [2, 45, 108, 12, 7]
lista_vacia = []
def funcion(lista,lista_vacia):
    lista_vacia=[]
    for i in range(0,len(lista)):
        if lista[i] % 2 == 0:
            lista_vacia.append("True")
        else:
            lista_vacia.append("False")
    return lista_vacia
print(funcion(lista,lista_vacia))

