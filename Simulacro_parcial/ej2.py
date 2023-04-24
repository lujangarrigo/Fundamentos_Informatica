import os, glob, re
#a)

def ejercicio_mails():
    os.chdir('informes')
    txt = glob.glob("*.txt")
    mails = [] 
    for archivo in txt: 
        with open(archivo,"r") as file:
            file_complete = file.read 
            mails.append(re.findall('^[a-z0-9]+[.-]?[a-z0-9]+[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?$',file_complete))
    os.mkdir("Mails")
    with open("Mails/base_de_datos.txt","w") as salida:
        for archivo in txt:
            with open(archivo,"r") as file:
                salida.write(file.readlines())
    return mails

lista = ejercicio_mails()
print(lista)

