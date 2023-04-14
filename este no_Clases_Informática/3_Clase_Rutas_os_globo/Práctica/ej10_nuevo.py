#Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo
#dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.

import os, glob
os.chdir("Práctica")
txt = glob.glob("*.txt")
for archivo in txt:
    with open(archivo,"r") as file:
        contenido = file.read()
os.mkdir("Resultado2")
with open("Resultado/Todos_los_archivos.txt", "w") as salida:
    for archivo in txt:
        with open(archivo, "r") as file:
            salida.write(file.readline())