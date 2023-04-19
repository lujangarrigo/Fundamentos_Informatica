class Sobreviviente:
  def __init__(self,adrenalina):
    self.adrenalina = adrenalina

  def atacar(self, contrincante):
      if contrincante.es_un_peligro():
        raise Exception("Es peligroso atacar a este zombi")
      #La excepción no solo aborta el método en el cual se produce sino también la ejecución de todos los métodos de la
      #cadena de envío de mensajes y los posteriores, pero cuidado, porque no se descartan los cambios realizados
      #anteriormente en caso de que los hubiera.
      else:
        danio = self.adrenalina // 2
        contrincante.recibir_danio(danio)
        self.adrenalina += 20

class Zombi:
  def __init__(self,hambre):
    self.hambre = hambre
    
  def sabe_correr(self):
    return True
    
  def es_un_peligro(self):
    return self.hambre >50
    
  def recibir_danio(self, danio):
    self.hambre -= danio * 2
    
class SuperZombi:
  def __init__(self,hambre):
    self.hambre = hambre
    
  def sabe_correr(self):
    return True
    
  def es_un_peligro(self):
    return True
  
  def recibir_danio(self, danio):
    self.hambre -= danio
    
  def regenerarse(self):
    self.hambre = 100


class PlantaCarnivoraZombi:
  def __init__ (self,clorofila):
    self.clorofila = clorofila
    
  def es_un_peligro (self):
    return self.clorofila > 40
    
  def hacer_fotosintesis (self,minutos):
    self.clorofila += minutos
   
  def recibir_danio (self, clorofila):
    self.clorofila -= 10