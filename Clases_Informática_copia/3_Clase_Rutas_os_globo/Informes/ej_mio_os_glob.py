import os
import glob
"""Ej hecho por mi"""

# Movemos a la carpeta Informes
os.chdir("C:\Users\lujan\Downloads\WBDSLA_Camp\Fundamentos_Informatica\Clases_Informática\3_Clase_Rutas_os_globo\Informes")
# Obtenemos los archivos .txt en la carpeta
archivos_txt = glob.glob('*.txt')
# Inicializamos un diccionario para almacenar los resultados
resultados = {}   
# Iteramos sobre cada archivo_txt
for archivo in archivos_txt:
    # Abrimos el archivo
    with open(archivo, 'r') as archivo:
        # Leemos todas las líneas
        lineas = archivo.readlines()
        # Obtenemos la cantidad de líneas
        cantidad_lineas = len(lineas)
        # Obtenemos la cantidad de veces que aparece la palabra 'estado'
for linea in lineas:
			if 'estado' in linea:
				cantidad_estado = cantidad_estado + 1	


        # Guardamos los resultados en el diccionario
resultados[archivo] = (cantidad_lineas, cantidad_estado, lineas[0])
# Creamos la carpeta Apellidos (si no existe)
if not os.path.exists('Apellidos'):
    os.mkdir('Apellidos')
# Creamos el archivo Lista.txt y escribimos la primera línea de cada archivo
with open('Apellidos/Lista.txt', 'w') as f:
    for archivo, (cantidad_lineas, cantidad_estado, primera_linea) in resultados.items():
        f.write(primera_linea)
        f.write('\n')
