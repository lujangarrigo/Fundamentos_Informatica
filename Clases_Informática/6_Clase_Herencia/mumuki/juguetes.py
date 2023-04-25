class Jugueteria:
    def __init__(self):
        self.productos = []

    def adquirir_producto(self, juguete):
        self.productos.append(juguete)

    def catalogo_de_oferta(self):
        juguetes_baratos = []
        for juguete in self.productos:
            if juguete.es_barato():
                juguetes_baratos.append(juguete.nombre)
        return juguetes_baratos


class Juguete:
  def __init__(self, nombre, precio_minorista, precio_mayorista, partes):
    self.nombre = nombre
    self.precio_minorista = precio_minorista
    self.precio_mayorista = precio_mayorista
    self.partes = partes

  def es_barato(self):
    return self.precio_minorista < 1000 and self.precio_mayorista < 600
  
  def precios_con_iva(self):
    return (self.precio_minorista * 1.21 , self.precio_mayorista * 1.21)
  
  def es_electronico (self):
    return "batería" in self.partes