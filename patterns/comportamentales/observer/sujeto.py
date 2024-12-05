from abc import ABC, abstractmethod

class Sujeto(ABC):
    @abstractmethod
    def agregar_observador(self, observador):
        pass

    @abstractmethod
    def remover_observador(self, observador):
        pass

    @abstractmethod
    def notificar(self, mensaje):
        pass