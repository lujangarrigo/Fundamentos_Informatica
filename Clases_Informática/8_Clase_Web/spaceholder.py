import requests, json
""" 
Desafío II Dado el siguiente enlace "https://jsonplaceholder.typicode.com/todos", realizar las siguientes actividades adjuntando los archivos resultantes y el código utilizado para la realización de cada paso:

a) ¿Cuál es el dominio al que estamos consultando?

b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type?

c) Agregar un contenido cuyo userId es 11 y su id es 2 con un nuevo título e indicando que está completo (completed).

d) En la arquitectura cliente-servidor ¿Qué características tiene el cliente?

a. jsonplaceholder.typicode.com
b. 
"""

respuesta = requests.get("https://jsonplaceholder.typicode.com/todos")
contenido = respuesta.json() #me da todos los contenidos asociados al recurso ditto, con los detalles de las habilidades, base de experiencia, forma, peso, etc. 

print("El status code es: ",respuesta.status_code)
print("El headers contiene:",respuesta.headers)
print("El content type es:",respuesta.headers["Content-Type"])
type(respuesta.json()) #es lista
len(respuesta.json()) #cantidad de elementos de la api
respuesta.json()[0] #se accede a los elementos con sus posiciones
data = {'userId':11,'id':2,'title':'quis ut nam facilis et oficial qui','completed':True}
headers = {'Content-Type':'application/json;charset=utf-8'}
#cuando hacemos post no modificamos la api original
#cuando hacemos post, se actualiza el id, se agrega un elemento con el numero del ultimo id + 1, por eso agregamos el elemento 201
a = requests.post("https://jsonplaceholder.typicode.com/todos", data = json.dumps(data),headers = headers)
print(a.json())