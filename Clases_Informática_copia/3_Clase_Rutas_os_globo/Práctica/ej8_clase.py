#!/usr/bin/env python3
#Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

def join_files(file1, file2, file3):
    with open(file1,"r") as f1, open(file2, "r") as f2, open(file3,"a") as f3:
        f3.write(f1.read()+f2.read())
join_files("archivo1.txt","archivo2.txt","archivos_unidos.txt")