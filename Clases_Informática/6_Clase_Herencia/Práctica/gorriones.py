"""
Definir una clase de gorriones, de los cuales nos interesa 
conocer dos medidas conocidas como CSS (coeficiente de 
serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico”
 y “veces”). El CSS resulta de dividir la cantidad total de
kilómetros que vuela desde que se lo comienza a estudiar,
por la cantidad total de gramos de comida que ingiere. 
El CSSP es la misma división pero considerando solamente
lo que voló la vez que más voló y lo que comió la vez 
que más comió. El CSSV es otra vez la misma idea, 
respecto de la cantidad de veces que voló y comió. 
Si un gorrión nunca comió, los coeficientes deben ser None. 
Un gorrión se considera en equilibrio si su CSS está entre 
0.5 y 2.
"""

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
        
    def esta_equilibrio(self):
        return 0.5 < self.css() < 2