from flask import Flask
from markupsafe import escape

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
@app.get("/") #decorador, generamos el /home
def home():
    return "<p>Te damos la bienvenida a MacoWins</p>" #<p> etiqueta de html que se usa para poner texto en una pág web

@app.get("/prendas/") #decorador, generamos el /home
def prendas():
    return productos

@app.get("/prendas/<id>")
def get_prenda(id):
    return f"<p>Mostrando la prenda {escape(id)}</p>"

#como dominio vamos a usar un puerto/ip
#Para ver el front hacemos ctrl + click en el link (todo esto en la terminal)