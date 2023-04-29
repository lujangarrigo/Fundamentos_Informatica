#a)
class PacMan:
    def __init__(self):
        self.vida = 3
        self.puntos = 0

    def comer_bolitas(self,cantidad):
        self.puntos += (cantidad *2)

    def velocidad(self):
        return 2 + self.puntos/100

    def perder_vida(self):
        self.puntos = 0
        self.vidas -= 1
        if self.vidas == 0:
            print("GAME OVER")

    def comer_fantasma(self,fantasma):
        if fantasma == "rosa":
            self.puntos += 8
        elif fantasma == "verde":
            self.puntos += 6
        elif fantasma == "rojo":
            self.puntos += 2
#No está mal pero se puede hacer de otra forma, que es mejor

pacman = PacMan()
print(pacman.puntos)
pacman.comer_bolitas(10)
print(pacman.puntos)
pacman.comer_fantasma("verde")



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

