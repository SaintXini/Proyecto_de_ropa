from abc import ABC, abstractmethod

# Interfaz que usa TextilSmart internamente
class ProveedorInterno(ABC):
    @abstractmethod
    def obtener_stock(self, id_producto):
        pass

    @abstractmethod
    def realizar_pedido(self, id_producto, cantidad):
        pass