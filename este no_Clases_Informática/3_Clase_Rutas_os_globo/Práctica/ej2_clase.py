#!/usr/bin/env python3
#Escribí un programa que lea un archivo e imprima las primeras n líneas.

def read_n_lines(n,archivo):
    with open(archivo,"r") as file:
        for i in range(n): #range(a,b,c) a =inicio , b=fin, c=paso (de a cuantas lineas)
            print(file.readline())
read_n_lines(2,"archivo1.txt")