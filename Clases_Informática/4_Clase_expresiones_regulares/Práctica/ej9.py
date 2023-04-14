#Ejercicio 9
#Escribí un programa que extraiga los caracteres que estén entre guiones en un
# string. (String de ejemplo: "Hoy estuvimos trabajando con re
# -regular expression- en python -con VSCode-")
import re
def entre_guiones(string):
    return re.findall(r"-(.*?)-",string) #devuelve una lista con los patrones
string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
print(entre_guiones(string))
#Cuando usamos el signo de pregunta así, favorecemos los matches internos, no ve solo lo global
#si no pongo el signo va a devolver: -regular expression- en python -con VSCode- porque no vería los guiones en el medio
#No devuelve el "en python" porque ya usó el guión del comienzo para cerrar el anterior.
