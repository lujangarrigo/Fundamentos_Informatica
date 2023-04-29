class Enterprise:
    def __init__(self):
        self.potencia = 50
        self.coraza = 5

    def potencia(self):
        return self.potencia
    
    def coraza(self):
        return self.coraza
    
    def encontrarPilaAtomica(self):
        potencia = max(self.potencia + 25,100) 
        self.potencia = potencia

    def encontrarEscudo(self):
        coraza = max(self.coraza + 10,50) 
        self.coraza = coraza

    def recibirAtaque(self, puntos):
        if self.coraza > puntos:
            self.coraza -= puntos
        elif self.coraza == 0:
            if self.potencia > puntos:
                self.potencia -= puntos
            elif self.potencia <= puntos:
                self.potencia = 0
        elif 0<self.coraza<puntos:
            puntos_restantes = puntos - self.coraza
            self.coraza = 0
            if self.potencia > puntos_restantes:
                self.potencia -= puntos_restantes
            elif self.potencia <= puntos_restantes:
                self.ppotencia = 0

    