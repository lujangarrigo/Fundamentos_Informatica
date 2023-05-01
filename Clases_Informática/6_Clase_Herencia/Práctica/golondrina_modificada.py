class Golondrina:
#El constructor: ponemos lo necesario para inicializar al objeto (ej energía)
#El estado del objeto se define con init (es el constructor del objeto)
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    if self.energia - (10 + kms) <= 0:
      return "No puede volar"
    else:
       self.energia -= (10 + kms)

  def esta_feliz(self):
    return self.energia > 50
  
  def entrenar(self):
    self.entrenar(0)

  def equilibrio(self):
    return 150<self.energia<300