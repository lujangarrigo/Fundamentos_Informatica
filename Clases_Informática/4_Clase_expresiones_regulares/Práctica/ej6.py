#Ejercicio 6
#Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada

import re
def lista_en_frase(lista, frase):
    for palabra in lista:
        if bool(re.search(palabra, frase)):
            print(f'"{palabra}" se encuentra en la frase.')
        else:
            print(f'"{palabra}" no se encuentra en la frase.')

print(lista_en_frase(["hola","chau"], "hola Alejandra"))