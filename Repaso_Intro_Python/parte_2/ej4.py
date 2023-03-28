#4: Definir un procedimiento que tome como parámetros dos listas y un elemento, en la que se debe eliminar
#  el elemento de una lista y agregarlo a la otra. Realizar dos versiones del ejercicio, usando un método 
# distinto para eliminar el elemento en cada versión. ¿Qué problema/s tiene este procedimiento?
lista1 = ["hola", "control", "chau", "control"]
lista2 = ["buenas","saludos"]
elemento=input("Ingrese un elemento: ")
lista2.append(elemento)
lista1.remove(elemento)
print(lista1)
print(lista2)