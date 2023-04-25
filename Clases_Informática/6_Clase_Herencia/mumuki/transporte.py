class MedioDeTransporte:
  def __init__(self, combustible):
    self.combustible = combustible
    
  def cargar_combustible(self,cantidad):
    self.combustible += cantidad
    
  def entran_personas(self,cantidad):
    return cantidad <= self.maximo_personas()
    
class Auto(MedioDeTransporte):
  def recorrer(self,kilometros):
    self.combustible -= kilometros/2
    
  def maximo_personas(self):
    return 5
  
class Moto(MedioDeTransporte):
  def recorrer(self,kilometros):
    self.combustible -= kilometros
    
  def maximo_personas(self):
    return 2

class Colectivo(MedioDeTransporte):
  def __init__(self):
    super().__init__(100)
    self.pasajeros = 0
  
  def recorrer(self,kilometros):
    self.combustible -= kilometros*2

  def entran_personas(self,cantidad):
    return True

  def cargar_combustible(self,cantidad):
    super().cargar_combustible(cantidad)
    self.pasajeros = 0


