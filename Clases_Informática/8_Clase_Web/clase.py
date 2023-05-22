import requests
#permite hacer pedidos http

respuesta = requests.get("https://api.github.com/users/ajvelezrueda/orgs")
print(respuesta) #devuelve el status
#print(respuesta.json()) #devuelve la información del usuario (ana) de sus organizaciones
datos = respuesta.json() #json te devuelve los datos en forma de lista con diccionario adentro
#print(datos) #cuántas orgs tiene

#lista de nombres de las orgs en las que está involucrado
def lista_nombres_orgs(datos):
    lista_orgs = []
    for diccionario in datos:
        lista_orgs.append(diccionario['login'])
    return lista_orgs
print(lista_nombres_orgs(datos))

#print(respuesta.headers) #me da ifo sobre mi pedido, me dice el límite de rate, dice tmb format=json, tmb el content-type
#print(respuesta.status_code) #https://http.cat/
#código asociada a la respuesta es el status code (cómo funcionó el pedido)
#error común: 500, internal server error