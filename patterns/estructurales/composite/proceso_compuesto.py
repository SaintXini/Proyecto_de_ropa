from datetime import datetime
from .procesos import ProcesoDeFabricacion

class ProcesoCompuesto(ProcesoDeFabricacion):
    def __init__(self, nombre, duracion_estimada):
        super().__init__(nombre, duracion_estimada)
        self.subprocesos = []
        self.estado = "Pendiente"  # Estado inicial
        self.estados_validos = {"Pendiente", "En Proceso", "Completado", "Pausado"}  # Estados iniciales

    def agregar_estado(self, nuevo_estado):
        """Permite agregar un nuevo estado personalizado."""
        self.estados_validos.add(nuevo_estado)

    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado actual si el estado nuevo es válido."""
        if nuevo_estado in self.estados_validos:
            self.estado = nuevo_estado
        else:
            raise ValueError(f"Estado '{nuevo_estado}' no es válido. Agregue el estado primero si es necesario.")

    def agregar_proceso(self, proceso):
        self.subprocesos.append(proceso)

    def remover_proceso(self, proceso):
        self.subprocesos.remove(proceso)

    def ejecutar(self):
        self.cambiar_estado("En Proceso")
        self.fecha_inicio = datetime.now()

        for proceso in self.subprocesos:
            proceso.ejecutar()

        self.cambiar_estado("Completado")
        self.fecha_fin = datetime.now()

    def pausar(self):
        self.cambiar_estado("Pausado")

    def reanudar(self):
        self.cambiar_estado("En Proceso")

    def obtener_tiempo_total(self):
        return sum(proceso.obtener_tiempo_total() for proceso in self.subprocesos)

    def obtener_estado(self):
        return {
            "nombre": self.nombre,
            "estado": self.estado,
            "duracion_estimada": self.duracion_estimada,
            "fecha_inicio": self.fecha_inicio,
            "fecha_fin": self.fecha_fin,
            "subprocesos": [proceso.obtener_estado() for proceso in self.subprocesos]
        }
