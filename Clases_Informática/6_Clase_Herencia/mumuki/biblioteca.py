class Biblioteca:
  def __init__(self):
    self.libros = set([])
    
  def agregar_libro(self,libro):
      self.libros.add(libro)
    
  def libros_largos(self):
    return [libro for libro in self.libros if libro.paginas>300]
  
  def titulos_disponibles(self):
    return ([libro.titulo for libro in self.libros])

class Libro(Biblioteca):
  
  def __init__(self,titulo,paginas,genero,autoria):
    self.titulo = titulo
    self.paginas=paginas
    self.genero=genero
    self.autoria = autoria
  
  def es_largo(self):
    return self.paginas > 300

  def nacionalidad(self):
    return self.autoria["nacionalidad"]

contacto = Libro("Contacto",400,"ciencia ficcion",{"nombre":"Carl","apellido":"Sagan","nacionalidad":"estados unidos"})
biblioteca_de_emma = Biblioteca()
biblioteca_de_emma.agregar_libro(contacto)

socorro = Libro("Socorro",250,"terror",{"nombre":"Elsa","apellido":"Bornemann","nacionalidad":"argentina"})
biblioteca_de_emma.agregar_libro(socorro)