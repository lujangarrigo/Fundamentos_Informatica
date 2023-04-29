import os, glob, re


def filtrar ():
     lista_txt = glob.glob("*.txt")

     with open("base_de_datos.txt", 'a') as arch: 
            for archivo in lista_txt: 
                with open(archivo, 'r') as archivo_secreto: 
                    texto = archivo_secreto.read()
                    lista = re.findall('\w+[-_\.]*\w+@gmail.com', texto)
                    for email in lista: 
                        arch.write(email + '\n')
print(filtrar())

#[\w]+[-_\.]*[\w]+@gmail.com
