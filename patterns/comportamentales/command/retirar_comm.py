from db.connection import session
from modules.producto.controller import ProductoTerminado
from .command import Command

class RetirarProductoCommand(Command):
    def __init__(self, producto_id):
        self.producto_id = producto_id
        self.producto = None

    def execute(self):
        self.producto = session.query(ProductoTerminado).get(self.producto_id)
        if self.producto:
            session.delete(self.producto)
            session.commit()
            return f"Producto {self.producto.nombre} retirado exitosamente."
        return "Producto no encontrado."

    def undo(self):
        if self.producto:
            session.add(self.producto)
            session.commit()
            return f"Se deshizo el retiro del producto {self.producto.nombre}."
        return "No se pudo deshacer la operación."