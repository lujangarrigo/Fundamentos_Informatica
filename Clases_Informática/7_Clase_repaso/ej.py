#Definir un procedimiento que lea los archivos .txt que 
# estan en la carpeta marzo, y copie la primera linea de 
# cada uno en un archivo dentro de la carpeta resultados 
#(que debe estar dentro de new)

#!/usr/bin/env python3
import os,glob,sys

#rutas_a_txt : nos va a servir para movernos a cualq carpeta
#ruta_resultado : nos sirve para la carpeta donde queremos q este el archivo salida
# salida es el archivo de salida que va a estar dentro de la carpeta de Resultado

def primeras_lineas(ruta_a_txt,ruta_resultado, salida):
    
    # Nos movemos a marzo
    os.chdir(ruta_a_txt)
    
    # Extraemos los .txt
    lista_txt = glob.glob("*.txt")
    # generamos una lista donde guardar la primer linea
    primer_linea = []
    
    # Leemos las primeras lineas de los arch.txt
    for archivo in lista_txt:
        with open (archivo,"r") as archivo_entrada:
            # en este punto tenemos la primer linea de cda arch.txt en una lista
            primer_linea.append(archivo_entrada.readline())
            
    
    # Nos movemos 2 carpetas mas arribas
    os.chdir("../../")
    
    # Creeamos carpeta de salida (Resultados)
    os.mkdir(ruta_resultado)    
    # nos movemos a esa carpeta REsultado
    os.chdir(ruta_resultado)
    # Abrimos archivo  dentro de la carpeta resultado (va a ser el archivo resultado)
    with open (salida, "a") as archivo_salida:
        # lo transformamos en string
        # linea: la primer linea de cada archivo dentro de lista: primer_linea 
        for linea in primer_linea:
            archivo_salida.write(linea) 
            
primeras_lineas("datos/marzo","resultado","salida.txt")