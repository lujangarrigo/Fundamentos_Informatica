class Plato:
    def es_picante(self):
        pass

class Pasta(Plato):
    def __init__(self):
        self.ajies = 0
        
    def es_picante(self):
        return self.ajies > 10
    
    def picantear(self):
        if self.es_picante():
            raise Exception("El plato ya está demasiado picante")
        self.ajies += 5
        
    def suavizar(self):
        self.ajies -= 1

class Pizza(Plato):
    def __init__(self):
        self.condimento = "adobo"
        
    def es_picante(self):
        return self.condimento == "cayena"
    
    def picantear(self):
      if self.es_picante():
        raise Exception("El plato ya está demasiado picante")
      self.condimento = "cayena"
        
    def suavizar(self):
        self.condimento = "orégano"

class Chef:
    def __init__(self, plato):
        self.plato_del_dia = plato
        
    def picantear(self):
        self.plato_del_dia.picantear()

class AyudanteDeCocina:
    def suavizar(self, plato):
        plato.suavizar()