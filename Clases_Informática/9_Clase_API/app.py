from flask import Flask

app = Flask(__name__)

productos = [
    {"id": 1,"tipo": "pantalon","talle": 35},
    {"id": 2,"tipo": "pantalon","talle": 36},
    {"id": 3,"tipo": "pantalon","talle": 37},
    {"id": 4,"tipo": "pantalon","talle": 38},
    {"id": 18,"tipo": "saco","talle": "M"},
    {"id": 19,"tipo": "saco","talle": "L"},
    {"id": 20,"tipo": "saco","talle": "XL"}]

#Primer endpoint de la app:
@app.get("/home") #decorador, generamos el /home
def home():
    return "Te damos la bienvenida a MacoWins" #<p> etiqueta de html que se usa para poner texto en una pág web

@app.get("/prendas") #decorador, generamos el /home
def prendas():
    return productos

if __name__ == "__main__":
    app.run(debug=True,port=5000)

#como dominio vamos a usar un puerto/ip
#Para ver el front hacemos ctrl + click en el link (todo esto en la terminal)
"""
@app.get("/prendas")
def get_all_prendas():
    return f"<p>Mostrando todas las prendas:{prendas}</p>"

prendas = [{"id": 1,"tipo": "pantalon","talle": 35},{"id": 2,"tipo": "pantalon","talle": 36},{"id": 3,"tipo": "pantalon","talle": 37},{"id": 4,"tipo": "pantalon","talle": 38},{"id": 18,"tipo": "saco","talle": "M"},{"id": 19,"tipo": "saco","talle": "L"},{"id": 20,"tipo": "saco","talle": "XL"}]
"""

"""
Tarea:
Armar la ruta /prendas que muestre todos los ítems de prendas
prendas = [{"id":1,"tipo":"pantalon","talle":42},{"id":2,"tipo":"pantalon","talle":42}"etc"]
"""