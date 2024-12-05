from datetime import datetime
from .procesos import ProcesoDeFabricacion

class ProcesoSimple(ProcesoDeFabricacion):
    def ejecutar(self):
        self.fecha_inicio = datetime.now()
        self.estado = "En Proceso"
        # Aquí iría la lógica específica de cada proceso
        print(f"Ejecutando proceso: {self.nombre}")
        self.estado = "Completado"
        self.fecha_fin = datetime.now()

    def obtener_tiempo_total(self):
        return self.duracion_estimada

    def obtener_estado(self):
        return {
            "nombre": self.nombre,
            "estado": self.estado,
            "duracion_estimada": self.duracion_estimada,
            "fecha_inicio": self.fecha_inicio,
            "fecha_fin": self.fecha_fin
        }