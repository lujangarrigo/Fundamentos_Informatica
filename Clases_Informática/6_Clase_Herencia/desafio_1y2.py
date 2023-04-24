"""Hace a hipo, entrenador de dragones: sabe aceptar a dragones, quienes son sus entrenados y hacerlos entrenar todos
 los dias, haciendoles dar 20 vueltas en circulos y luego comer su comida favorita hasta saciarse (3 peces)"""

class Entrenador:
  def __init__(self,animales):
      self.animales = animales

  def aceptar_animal(self,animal):
    self.animales.append(animal)

  def entrenar(self, animales): #Consigna 5 y 6
    for animal in animales:
      animal.volar_en_circulos(20)
      animal.comer(3)
    
  def entrenamiento_intensivo(self,animales): #Consigna 7
     for animal in animales:
      if not animal.esta_debil():
        animal.volar_en_circulos(50)
      else:
        raise Exception("Ya está débil")



class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def comer(self, gramos):
    self.comer_alpiste(gramos)

  def volar_en_circulos(self,vueltas):
    self.energia -= 1 * vueltas

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_feliz(self): #Consigna 4
    return self.energia > 50
  
  def entrenar(self):
    self.entrenar(0)

  def esta_debil(self): #Consigna 3
    return self.energia <= 10
  
  def recibir_entrenamiento(self): #Consigna 6
    return self.volar_en_circulos and self.comer_alpiste(200)
  
  def recibir_entrenamiento_intensivo(self): #Consigna 7
    while self.esta_debil==False:
        return self.volar_en_circulos 


class Dragon:     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer(self, unidades):
    self.comer_peces(unidades)

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self,vueltas):
    self.energia -= 1 * vueltas

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def esta_feliz(self): #Consigna 4
    return self.energia > 500
  
  def entrenar(self):
    self.entrenar(0)

  def esta_debil(self): #Consigna 3
    return self.energia <= 50
  
  def recibir_entrenamiento(self): #Consigna 5
    return self.volar_en_circulos * 20 and self.comer_peces(3)
  
  def recibir_entrenamiento_intensivo(self): #Consigna 7
    while self.esta_debil==False:
        return self.volar_en_circulos 

class AvesNoVoladoras:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def comer(self, gramos):
    self.comer_alpiste(gramos)

  def correr_en_circulos(self):
    self.energia -= 25

  def esta_feliz(self): #Consigna 4
    return self.energia > 500
  
  def esta_debil(self): #Consigna 3
    return self.energia <= 50

  def recibir_entrenamiento(self): #Desafio 2
    return self.correr_en_circulos and self.comer_alpiste(200)
  
  def recibir_entrenamiento_intensivo(self): #Desafio 2
    while self.esta_debil==False:
      return self.volar_en_circulos 


pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000) 
juanita = AvesNoVoladoras(300)
maria = Golondrina(42) #Consigna 1
chimuelo = Dragon(200,1000) #Consigna 2
hipo = Entrenador([])
hipo.aceptar_animal(chimuelo)
hipo.aceptar_animal(maria)