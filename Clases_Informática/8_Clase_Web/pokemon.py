import requests

respuesta = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
contenido = respuesta.json() 
print(contenido.keys()) #obtenemos las claves(el nombres de los campos) de esos diccionarios

# ¿Cual es el dominio? : pokeapi.co

# ¿Que status_code devuelve el pedido a dicha URL?
print(f"El status code es: {respuesta.status_code}") # 200 

#¿Y qué Content-Type? 
print(f'el Content-Type es: {respuesta.headers["Content-Type"]}') # application/json; charset=utf-8

# Obtene la informacion correspondiente al campo "forms"
print(f'El campo forms contiene: {contenido["forms"]}')
# IMPRIME: [{'name': 'pikachu', 'url': 'https://pokeapi.co/api/v2/pokemon-form/25/'}]

# Averigüá cuántos pokemones almacena la API.
respuesta2 = requests.get('https://pokeapi.co/api/v2/pokemon')
contenido_cantidad_pokemones = respuesta2.json() 
print(f'hay {contenido_cantidad_pokemones["count"]} pokemones') #esto funciona como el len (no todas las APIS son iguales)


# ¿Cómo esperás que sea la URL para obtener las habilidades de los Pokemons (abilities)? 
respuesta_habilidades = requests.get('https://pokeapi.co/api/v2/ability')
habilidades = respuesta_habilidades.json()
print(habilidades)

# ¿y cómo será la url para obtener la información sobre la habilidad 2?
respuesta_habilidad_2 = requests.get('https://pokeapi.co/api/v2/ability/2') #otra opcion: ability2
habilidad_2 = respuesta_habilidad_2.json()
print(f'la habilidad 2 es: {habilidad_2}')


# Guardar los datos correspondientes a Pikachu y Sylveon en un archivo de nombre "ficha_tecnica_pokemon.txt".

#primero descargamos la informacion de sylveon y transformamos en string 
sylveon = requests.get('https://pokeapi.co/api/v2/pokemon/sylveon')
contenido_sylveon = sylveon.json()

pikachu = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
contenido_pikachu = pikachu.json()
print(contenido_pikachu.keys())


with open ("ficha_tecnica_pokemon.txt", "ab") as ficha_tecnica:
    ficha_tecnica.write(pikachu.content)
    ficha_tecnica.write(b"\n")
    ficha_tecnica.write(sylveon.content)