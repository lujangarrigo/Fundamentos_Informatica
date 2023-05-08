"""
Entrar a la carpeta Datos que esta dentro de Informes, tiene archivos de los cuales debemos extraer los numeros 
de celular y escribirlos en una lista en un archivo llamado Celulares, que esté dentro de la carpeta Resultado
"""
import os, glob, re

def extraer_celulares(ruta_a_txt, ruta_a_resultado, archivo_de_salida):
    os.chdir(ruta_a_txt)
    lista_txt = glob.glob("*.txt")
    for txt in lista_txt:
        with open (txt,"r") as archivo_entrada:
            contenido = archivo_entrada.read()
            print(contenido)
            lista_celulares = re.findall("11[-\s]?\d{4}[-\s]?\d{4}",contenido)
    os.chdir("../../")
    os.mkdir(ruta_a_resultado)   
    os.chdir(ruta_a_resultado)

    with open (archivo_de_salida, "a") as archivo_salida:
        for celular in lista_celulares:
            archivo_salida.write(celular + "\n")

extraer_celulares("Informes/Datos","Resultado","Celulares.txt")
