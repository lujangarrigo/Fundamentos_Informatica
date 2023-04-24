#a)
import re
def caracteres_permitidos(string):
    return bool(re.search('X*ab*Y', string)) 
print(re.search("X*Y", "YabhdkabX"))
print(caracteres_permitidos("YabhdkabX"))
