class Enterprise:
    def __init__(self):
        self.potencia = 50
        self.coraza = 5

    def potencia_actual(self):
        return self.potencia
    
    def coraza_actual(self):
        return self.coraza
    
    def encontrarPilaAtomica(self):
        potencia = min(self.potencia + 25,100) 
        self.potencia = potencia

    def encontrarEscudo(self):
        coraza = min(self.coraza + 10,50) 
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

    def fortalezaDefensiva(self):
        return self.coraza + self.potencia
    
    def necesitaFortalecerse(self):
        return self.coraza==0 and self.potencia<20
    
    def fortalezaOfensiva(self):
        if self.potencia<20:
            return 0
        else:
            return (self.potencia-20)/2


enterprise = Enterprise()
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()
print(enterprise.coraza_actual())
print(enterprise.potencia_actual())

print(enterprise.fortalezaDefensiva())
print(enterprise.necesitaFortalecerse())
print(enterprise.fortalezaOfensiva())