class Titan:
    def __init__(self,salud):
        self.salud = salud

    def salud_actual(self):
        return self.salud

    def esta_vivo(self):
        return self.salud > 0

    def recibir_ataque(self,puntos_daño):
        self.salud -= puntos_daño * 1.5

    def cuantas_casas(self):
        return self.salud *8/100

    def destruir_casas(self):
        if (self.cuantas_casas() > 1): # si puede destruir mas de 1 casa, no pongo >= pq se muere si tiene la energia justa solo para destruir 1
            if ((self.cuantas_casas() % 1) > 0): # Si tengo un numero con coma ej 4,25, destruye 4 y esos 0,25 van a ser la salud q le va a quedar
                self.salud -= (self.cuantas_casas() // 1) * 12.5 # le resto a la salud la cantidad de casas // 1 (la division entera), o sea el número entero * 12,5, que es lo q se le debe restar a la salud
            else:
                self.salud -= (self.cuantas_casas() - 1) * 12.5 # si no es numero con coma vamos a restarle 1 para que quede con energia
        else:
            print("No puede destruir ninguna casa") #El titan no puede morirse, por eso hacemos estos if
    
    def grito(self):
        return "¡Aaaarrrg!"

titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.salud_actual())
print(titan1.cuantas_casas())
print(titan1.grito())
titan1.destruir_casas()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())
