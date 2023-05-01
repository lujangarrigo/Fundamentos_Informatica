class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def descuento(self,porcentaje):
        self.precio = self.precio - self.precio*porcentaje/100
        return self.precio
    
LenovoYoga = Notebook("Lenovo","Yoga",700000)
Hp = Notebook("Hp","Pavilion",500000)

print(LenovoYoga.descuento(10))
print(Hp.descuento(15))