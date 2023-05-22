import re
def entre_guiones(string):
    return re.findall("-([\w\s]*)-",string)

print(entre_guiones("Hola -que onda- como va"))