#!/usr/bin/env python3
#Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y
#lo guarde en otro archivo.

def reemplazo_letra_por_letra_con_salto_linea(letra,archivo_entrada,archivo_salida):
    with open (archivo_entrada,"r") as arch_entrada:
        contenido = arch_entrada.read()
        contenido_modificado = contenido.replace(letra,letra+"\n")
        with open (archivo_salida,"w") as arch_salida:
            arch_salida.write(contenido_modificado)
reemplazo_letra_por_letra_con_salto_linea("a","archivo1.txt","archivo_ej5.txt")