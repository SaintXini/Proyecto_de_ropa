from abc import ABC, abstractmethod

# Componente base
class ProcesoDeFabricacion(ABC):
    def __init__(self, nombre, duracion_estimada):
        self.nombre = nombre
        self.duracion_estimada = duracion_estimada
        self.fecha_inicio = None
        self.fecha_fin = None
        self.estado = "Pendiente"

    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def obtener_tiempo_total(self):
        pass

    @abstractmethod
    def obtener_estado(self):
        pass