#Ej 1: Definir un procedimiento que tome como parámetro una lista, 
# verifique si tiene el elemento "control" y le agregue el string 
# "revisado" y le quite el elemento "control"

lista_hola =["control","asd"]
print(lista_hola)
for i in range(0,len(lista_hola)):
      if lista_hola[i]=="control":
        lista_hola[i]="revisado"
print(lista_hola)