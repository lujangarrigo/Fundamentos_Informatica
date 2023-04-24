
#Libreria para leer de linea de comando
import sys
import os

#Se leen las variable de consola
#sys.argv es un array de strings, elijo el indice del elemento que quiero
#Si el parametro tiene espacio lo encierro en comillas ''
file_path1 = sys.argv[1]
file_path2 = sys.argv[2]

 
#Abrir archivo con read
with open(file_path1) as f1:
   #readLines lee el archivo y lo guarda en array
   content_file1 = f1.readlines()
with open(file_path2) as f2:
   content_file2 = f2.readlines()


#Abrir archivo con write
with open(file_path1, 'w') as f1:
   #writeLines escribe el archivo
   f1.writelines(content_file2)
with open(file_path2, 'w') as f2:
   f2.writelines(content_file1)


print("Files successfully swapped.")
#En la terminal de bash poner:
#python desafio.py 'ARCHIVO GATITO.txt' 'ARCHIVO PERRITO.txt'

#Otra forma:
"""os.rename(sys.argv[1],"temporal")
os.rename(sys.argv[2], sys.argv[1])
os.rename("temporal", sys.argv[2])"""