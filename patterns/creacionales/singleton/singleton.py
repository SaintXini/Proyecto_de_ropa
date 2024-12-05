# modules/inventory_manager.py
from modules.materia_prima.controller import controlar_inventario, generar_orden_compra, session
from modules.materia_prima.model import MateriaPrima
from modules.producto.controller import controlar_inventario_productos
from modules.producto.model import ProductoTerminado

class GestorDeInventario:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GestorDeInventario, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:  # Evita inicialización múltiple
            return
        self._initialized = True
        # Inicializa variables necesarias aquí

    @staticmethod
    def get_instance():
        if not GestorDeInventario._instance:
            GestorDeInventario()
        return GestorDeInventario._instance

    def obtener_inventario_materias_primas(self):
        return controlar_inventario()

    def obtener_inventario_productos(self):
        return controlar_inventario_productos()
