from abc import ABC, abstractmethod

class EstrategiaDistribucion(ABC):
    @abstractmethod
    def distribuir(self, pedido):
        pass