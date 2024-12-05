from .estrategia import EstrategiaDistribucion

class ContextoDeDistribucion:
    def __init__(self, estrategia: EstrategiaDistribucion = None):
        self._estrategia = estrategia

    def set_estrategia(self, estrategia: EstrategiaDistribucion):
        self._estrategia = estrategia

    def distribuir_pedido(self, pedido):
        if self._estrategia:
            return self._estrategia.distribuir(pedido)
        return "No se ha establecido una estrategia de distribución"
        