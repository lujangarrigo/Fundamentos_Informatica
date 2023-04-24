import os, glob, re
#a)

def ejercicio_mails():
    txt = glob.glob("*.txt")
    mails = [] 
    for archivo in txt: 
        with open(archivo,"r") as file: #abrimos los archivos
            file_complete = file.read 
            mails = re.findall('^[a-z0-9]+[.-]?[a-z0-9]+[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?$',file_complete)
    with open("base_de_datos.txt","w") as salida: #usamos salida cuando abrimos un archivo.txt que vamos a escribir
        for archivo in txt:
            with open(archivo,"r") as file:
                salida.write(file.readlines())
    return mails

lista = ejercicio_mails()
print(lista)
