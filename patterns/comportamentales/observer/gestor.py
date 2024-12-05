from .sujeto import Sujeto

class GestorDeProduccion(Sujeto):
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def remover_observador(self, observador):
        self.observadores.remove(observador)

    def notificar(self, mensaje):
        for observador in self.observadores:
            observador.actualizar(mensaje)

class GestorDeInventario(Sujeto):
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def remover_observador(self, observador):
        self.observadores.remove(observador)

    def notificar(self, mensaje):
        for observador in self.observadores:
            observador.actualizar(mensaje)