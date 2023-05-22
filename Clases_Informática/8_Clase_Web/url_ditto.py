import requests
#/ability es el recurso, si lo hago asi solo me da todos los items de ese recurso (las url de cada habilidad)
#accedo a cada item haciendo /recurso/id, en el ejemplo: /ability/numero. Son parámetros
#vienen de una base de datos con los ítems (1,2,3,etc)
respuesta = requests.get('https://pokeapi.co/api/v2/ability/')
print(respuesta.json())

respuesta_item = requests.get('https://pokeapi.co/api/v2/ability/1')
print(respuesta_item.json())
