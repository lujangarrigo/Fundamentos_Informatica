import os, glob, re
#a)

os.chdir('informes')
txt = glob.glob("*.txt")
with open("base_de_datos.txt", 'a') as arch: 
        for f in txt: 
            with open(f, 'r') as archivo_secreto: 
                texto = archivo_secreto.read()
                lista = re.findall('[a-z0-9]+[.-]?[a-z0-9]+[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?', texto)
                for email in lista: 
                    arch.write(email + ', ')