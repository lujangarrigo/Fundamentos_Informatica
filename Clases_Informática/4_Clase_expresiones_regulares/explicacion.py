import re
string2 = "X123qddhqw3YdhuY"
#123qddhqw3
#favorecer matches internos --> agregamos un ? al final del grupo
#favorecer matches externos --> no agrego nada

print(re.search("X(.*?)Y",string2).group(1))
print(re.findall("X(.*?)Y", string2))


def reemplazar (string):
    return re.sub("Rama","Blas", string)

print(reemplazar("Hola Rama"))