import re
def buscar_subsecuencias(string):
    return re.findall("hola(\w*ab\w*?)lol",string)

print(buscar_subsecuencias("holalknabqlolj3bdki23qubYlol"))