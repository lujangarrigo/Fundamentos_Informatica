class Gorrion:
  def __init__(self):
    self.kilometros_volados = []
    self.gramos_ingeridos = []

  def volar(self,km):
    self.kilometros_volados.append(km)

  def comer(self,gramos):
    self.gramos_ingeridos.append(gramos)

  def css(self):
    if self.gramos_ingeridos != []:
        return sum(self.kilometros_volados) / sum(self.gramos_ingeridos)
    else:
        return None

  def cssp(self):
    if self.gramos_ingeridos != []:
        return max(self.kilometros_volados)/max(self.gramos_ingeridos)
    else:
        return None

  def cssv(self):
    if self.gramos_ingeridos != []:
        return len(self.kilometros_volados)/len(self.gramos_ingeridos)
    else:
        return None
        
  def estaEnEquilibrio(self):
    return 0.5 < self.css() < 2

class Golondrina:
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

  def estaEnEquilibrio(self):
    return 150<self.energia<300
  

class Ornitologo:
  def __init__(self):
    self.aves = []

  def estudiarAve(self,ave):
    self.aves.append(ave)

  def avesEnEstudio(self):
    return self.aves
  
  def avesEnEquilibrio(self):
    return [self.aves[i].estaEnEquilibrio() for i in range(len(self.aves))]
  
  def realizarRutinaSobreAves(self):
    [self.aves[i].comer(80) for i in range(len(self.aves))]
    [self.aves[i].volar(70) for i in range(len(self.aves))]
    [self.aves[i].comer(10) for i in range(len(self.aves))]