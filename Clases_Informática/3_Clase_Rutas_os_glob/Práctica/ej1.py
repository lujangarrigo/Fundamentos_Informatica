#!/usr/bin/env python3
#ej 1: Realizá un programa que lea un archivo e imprima con líneas de ese archivo no empiecen con una letra
# determinada (por ejemplo, que imprima líneas no empiecen con "P").
letra = "P"  # letra a excluir
nombre_archivo = "archivo1.txt"  # nombre del archivo a leer

# abrimos el archivo en modo lectura
with open(nombre_archivo, "r") as archivo:
    # leemos cada línea del archivo
    for linea in archivo:
        # comprobamos si la línea no comienza con la letra determinada
        if not linea.startswith(letra):
            # si la línea no comienza con la letra determinada, la imprimimos
            print(linea)
        else:
            pass