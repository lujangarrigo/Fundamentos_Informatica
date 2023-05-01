class Contador:
    def __init__(self,numero):
        self.numero = numero
        self.ultimo_comando = None

    def valorActual(self):
        print(self.numero)
        self.ultimo_comando = "actualización"

    def inc(self):
        self.numero += 1
        self.ultimo_comando = "incremento"
        return self.numero
    
    def dis(self):
        self.numero -= 1
        self.ultimo_comando = "disminución"
        return self.numero

    def valorNuevo(self,numero_nuevo):
        self.numero = numero_nuevo
        self.ultimo_comando = "actualización"
        return self.numero

    def reset(self):
        self.numero = 0
        self.ultimo_comando = "reset"
        return self.numero
    
    def ultimoComando(self):
        if self.ultimo_comando is None:
            return "Ningún comando ha sido ejecutado aún."
        else:
            return self.ultimo_comando

contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.valorActual()