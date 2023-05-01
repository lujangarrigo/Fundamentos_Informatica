class Persona:
    def __init__(self, energia):
        self.energia = energia
        self.estado_de_animo = False

    def energia_actual(self):
        return self.energia

    def hacer_ejercicio(self,minutos):
        self.energia -= minutos / 30 * 25

    def comer(self):
        self.energia += 10

    def dormir(self,horas):
        self.energia += horas * 100 / 8

class Estudiante(Persona): 
    def estudiar(self, horas):
        self.energia -= horas * 20

    def aprobar(self):
        self.estado_de_animo=True
        return self.estado_de_animo


estudiante = Estudiante(100)
estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_actual())