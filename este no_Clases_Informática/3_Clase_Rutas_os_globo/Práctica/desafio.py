#!/usr/bin/env python3
import os
"""
with open("vacio.txt", "w") as miarch:
    miarch.write("Este es el contenido del archivo")
"""
with open("manipulacion_arch.txt","r") as miarch:
    miarch = open("archivo1.txt", "r")
print(miarch.readlines())
print(miarch.read())
print(miarch.readline())
type(miarch.readlines())