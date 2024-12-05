from abc import ABC, abstractmethod
from datetime import datetime
## posteriormente a esto gestor y responsable se aplican a materia prima  y apodruccion

class Observador(ABC):
    def __init__(self):
        self.notificaciones = []

    @abstractmethod
    def actualizar(self, mensaje):
        pass

    def agregar_notificacion(self, mensaje):
        self.notificaciones.append({
            'mensaje': mensaje,
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def obtener_notificaciones(self):
        return self.notificaciones

    def limpiar_notificaciones(self):
        self.notificaciones = []