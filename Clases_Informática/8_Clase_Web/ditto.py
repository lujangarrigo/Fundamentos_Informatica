import requests
"""
1. Escribir las partes de la URL 
2. Qué respuesta obtenes al hacer un get en esa URL?
3. Cuál es el content type de esa respuesta?
4. Cuál es el status code de la respuesta?
5. Cuántas habilidades tiene ese pokemon?

1. 
https:// --> protocolo
pokeapi.co --> dominio
/api/v2/pokemon/ditto --> recurso
"""
#partes de la URL
#https:// es el protocolo
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
contenido = respuesta.json() #me da todos los contenidos asociados al recurso ditto, con los detalles de las habilidades, base de experiencia, forma, peso, etc. 
print(contenido.keys())

print(respuesta) #devuelve el status
print("El status code es: ",respuesta.status_code)
print(respuesta.headers) #devuelve datos del pedido (entre esos está en content-type)
print("El content type es:",respuesta.headers["Content-Type"]) #devuelve el content type, es un dato tipo json

#conseguir las habilidades
print(contenido["abilities"])
print("ditto tiene:",len(contenido["abilities"]),"habilidades")
