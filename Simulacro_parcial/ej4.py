#a)
class Pacman:
    def __init__(self, vidas):
        self.vida = vidas
        self.puntos = 0
        self.velocidad = 2

    def comer_bolitas(self,cantidad):
        self.puntos += cantidad
        self.velocidad += self.puntos

    def comer_fantasma(self,fantasma):
        self.puntos += fantasma.puntaje_que_otorga
        self.velocidad += fantasma.velocidad_que_otorga

    def tocar_fantasma(self,fantasma):
        self.vidas -= fantasma.toca_a_pacman()

class Fantasma:
    def __init__(self,aterrador):
        self.vida = 1
        self.aterrador = aterrador

    def toca_a_pacman(self):
        if self.aterrador == True:
            return 2
        else:
            return 1

class Rosa(Fantasma):
    def puntaje_que_otorga(self):
        return 8
    
    def velocidad_que_otorga(self):
        return 6

class Verde(Fantasma):
    def puntaje_que_otorga(self):
        return 6
    
    def velocidad_que_otorga(self):
        return 4

class Verde(Fantasma):
    def puntaje_que_otorga(self):
        return 2
    
    def velocidad_que_otorga(self):
        return 2

