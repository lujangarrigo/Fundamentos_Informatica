class Pacman:
    def __init__(self):
        self.vidas = 3
        self.puntos = 0
        self.velocidad = 1

    def comer_bolitas(self, cantidad):
        self.puntos += cantidad
        self.velocidad += 1

    def comer_fantasma(self,fantasma):
        self.velocidad += 5
        self.puntos += fantasma.puntos_color()

    def tocar_fantasma(self,fantasma):
        self.vidas -= fantasma.tocar_pacman()

class Fantasma:
    def __init__(self, tipo):
        self.tipo_fantasma = tipo
    
    def tocar_pacman(self):
        if self.tipo_fantasma == "Aterrador":
            return 2
        else:
            return 1

    def puntos_color(self):
        return self.puntos_fantasma()

class Rosa(Fantasma):
    def puntos_fantasma(self):
        return 8

class Verde(Fantasma):
    def puntos_fantasma(self):
        return 6

class Naranja(Fantasma):
    def puntos_fantasma(self):
        return 4
    
class Rojo(Fantasma):
    def puntos_fantasma(self):
        return 2
    

pacman = Pacman()
fantasma_rojo = Rojo("Aterrador")
pacman.comer_bolitas(20)
print("Puntos de pacman luego de comer 20 bolitas:", pacman.puntos)
print("Velocidad de pacman luego de comer 20 bolitas:",pacman.velocidad)
pacman.comer_fantasma(fantasma_rojo)
print("Puntos de pacman luego de comer un fantasma rojo:",pacman.puntos)
print("Velocidad de pacman luego de comer un fantasma rojo:",pacman.velocidad)
pacman.tocar_fantasma(fantasma_rojo)
print("Vidas de pacman luego de tocar al fantasma rojo aterrador:",pacman.vidas)