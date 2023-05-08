#!/usr/bin/env python3
#Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.
def eliminar_saltos_de_linea(archivo_entrada,archivo_salida):
    with open (archivo_entrada,"r") as arch_entrada:
        contenido = arch_entrada.read()
        contenido_modificado = contenido.replace("\n","")
        with open (archivo_salida,"w") as arch_salida:
            arch_salida.write(contenido_modificado)
eliminar_saltos_de_linea("archivo1.txt","archivo_ej6.txt")