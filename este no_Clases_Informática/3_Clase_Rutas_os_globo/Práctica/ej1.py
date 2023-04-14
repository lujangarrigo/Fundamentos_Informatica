#!/usr/bin/env python3
#ej 1: Realizá un programa que lea un archivo e imprima con líneas de ese archivo no empiecen con una letra
# determinada (por ejemplo, que imprima líneas no empiecen con "P").

def no_empieza_con(letra, archivo):
   with open(archivo, "r") as file:
        for linea in file:
            if not linea.startswith(letra): # comprobamos si la línea no comienza con la letra determinada
                print(linea) #imprimimos la linea
no_empieza_con("P","archivo1.txt")