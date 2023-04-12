#Ejercicio 11
#Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra 
#P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
import re
def dos_P(lista):
    for elemento in lista:
        resultado = re.match("(P\w*)\W(P\w*)", elemento) #Puedo poner \W o \S (espacio). Puedo usar * o +.
        if resultado is not None:
            print(resultado.group())
lista = ["Práctica Python","Práctica C++", "Práctica Fortran"]
dos_P(lista)