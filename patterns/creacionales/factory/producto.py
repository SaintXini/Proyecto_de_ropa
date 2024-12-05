from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, descripcion, cantidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad

    @abstractmethod
    def mostrar_informacion(self):
        pass