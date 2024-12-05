from .estrategia import EstrategiaDistribucion

class DistribucionRapida(EstrategiaDistribucion):
    def distribuir(self, pedido):
        return f"Distribución rápida para el pedido {pedido.id}: Entrega en 1-2 días hábiles"

class DistribucionEconomica(EstrategiaDistribucion):
    def distribuir(self, pedido):
        return f"Distribución económica para el pedido {pedido.id}: Entrega en 5-7 días hábiles"