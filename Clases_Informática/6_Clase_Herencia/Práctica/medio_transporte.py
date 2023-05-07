class MedioDeTransporte:
    def __init__(self,combustible):
        self.combustible = combustible

    def cargarCombustible(self,litros):
        self.combustible += litros

    def entranPasajeros(self,cantidad):
        return self.cantidadPasajerosMax() >= cantidad

class Auto(MedioDeTransporte):
    def cantidadPasajerosMax(self):
        return  5
    
    def manejar(self,kms):
        self.combustible -= kms/2

class Moto(MedioDeTransporte):
    def cantidadPasajerosMax(self):
        return 2
    
    def manejar(self,kms):
        self.combustible -= kms

auto_ford = Auto(20)
print(auto_ford.entranPasajeros(5))

