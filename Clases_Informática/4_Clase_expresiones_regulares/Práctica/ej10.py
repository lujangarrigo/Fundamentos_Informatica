#Ejercicio 10
#Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por 
#los caracteres @ o &.
import re
def get_substr(string):
    return re.findall("[@|$](.*?)[@|&]", string)
string = "cdaf@dsfe% ad @ sd"
print(get_substr(string))