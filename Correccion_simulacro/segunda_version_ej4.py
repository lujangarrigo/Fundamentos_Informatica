#class PacMan:
#...

class Fantasma:
    def __init__(self):
        self.fantasmas = {"rosa":8, "verde":6,"naranja":4,"rojo":2}
    def puntos_color (self,color):
        return self.fantasmas[color]
    
fantasma = Fantasma()
