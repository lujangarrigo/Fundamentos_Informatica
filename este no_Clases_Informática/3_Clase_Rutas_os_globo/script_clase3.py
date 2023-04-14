arch = open("hola.txt","r")
print(arch) #Si no pongo read, no me va a imprimir el contenido
"""print(arch.read())""" #Solo si pongo read me va a imprimir el contenido del archivo
#Para ejecutar tengo q poner en la terminal "Python scr + tab"
#Read lee todo el archivo como si fuese un unico string
print(arch.readlines())#Con readlines() lee linea a linea el archivo. Te lo devuelve como lista
#El \n significa salto de linea
#Puedo iterar linea a linea el texto

#Si el archivo no esta en mi directorio (ej el de hola.txt) tengo que copiar el path entero: "hola/user/doc/hola.txt"
#home/user es "~"
