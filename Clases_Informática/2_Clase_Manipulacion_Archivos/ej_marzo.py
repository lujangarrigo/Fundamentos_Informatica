"""Definir un procedimiento que lea los archivos .txt que estan en la carpeta marzo, y copie la primera linea de cada uno
 en un archivo dentro de la carpeta resultados (que debe estar dentro de datos, que esta dentro de new)"""
import os, glob, sys

def primeras_lineas(path_a_txt,path_resultado, salida):
    os.chdir(path_a_txt)
    textos = glob.glob("*.txt")
    primer_linea = []
    for txt in textos:
        with open(txt, 'r') as texto:
            primer_linea.append(texto.readline())
    os.chdir("../..")
    os.mkdir(path_resultado)
    os.chdir(path_resultado)
    with open(salida,"a") as final_txt:
        for linea in primer_linea:
            final_txt.write(linea)

primeras_lineas("datos/marzo", "resultado", "salida.txt")

#movernos a marzo
#extraemos los txt
#leemos las primeras lineas
#hacemos la carpeta de salida
#hacer el archivo
#poner lineas en el archivo nuevo