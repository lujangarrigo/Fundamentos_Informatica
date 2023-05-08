#!/usr/bin/env python3
#ej 1: Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiecen con una letra
# determinada 

def cantidad_lineas_que_no_empiezan_con_la_letra(letra,nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        contador = 0
        for linea in archivo:
            if not linea.startswith(letra):
                contador += 1
        else:
            pass
        return contador
print(cantidad_lineas_que_no_empiezan_con_la_letra("P","archivo1.txt"))