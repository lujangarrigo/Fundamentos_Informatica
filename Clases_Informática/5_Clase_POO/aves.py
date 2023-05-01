#Los nombres de clases siempre van en mayúscula

class Golondrina:
#El constructor: ponemos lo necesario para inicializar al objeto (ej energía)
#El estado del objeto se define con init (es el constructor del objeto)
  def __init__(self, energia):
    self.energia = energia

#self (uno mismo), representa al objeto en sí
  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_feliz(self):
    return self.energia > 50

  def entrenar(self):
    self.entrenar(0)


class Dragon:     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def esta_feliz(self):
    return self.energia > 500
  
  def entrenar(self):
    self.entrenar(0)

class AvesNoVoladoras:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def correr_en_circulos(self):
    self.energia -= 25


#Instanciación del objeto:
pepita = Golondrina(100) #100 es la energía inicial
anastasia = Golondrina(200)
roberta = Dragon(10, 1000) #10 es la cantidad de dientes
juanita = AvesNoVoladoras(300)