from .observer import Observador

class ResponsableDeCompras(Observador):
    def actualizar(self, mensaje):
        self.agregar_notificacion(f"Compras: {mensaje}")

class ResponsableDeProduccion(Observador):
    def actualizar(self, mensaje):
        self.agregar_notificacion(f"Producción: {mensaje}")