import os, glob, re
#a)

def ejercicio_mails():
    txt = glob.glob("*.txt")
    mails = [] 
    for archivo in txt: 
        with open(archivo,"r") as file:
            file_complete = file.read 
            mails = re.findall('^[a-z0-9]+[.-]?[a-z0-9]+[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?$',file_complete)
    with open("base_de_datos.txt","w") as salida:
        for archivo in txt:
            with open(archivo,"r") as file:
                salida.write(file.readlines())
    return mails

lista = ejercicio_mails()
print(lista)

"""txt = glob.glob("*.txt")
print(txt)
for archivo in txt:
    with open(archivo,"r") as file:
        file_complete = file.read()
        print(file_complete)
        print(re.findall('^[a-z0-9]+[.-]?[a-z0-9]+[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?$',file_complete))
"""
