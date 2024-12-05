from db.connection import session
from modules.producto.controller import ProductoTerminado
from .command import Command

class AgregarProductoCommand(Command):
    def __init__(self, nombre, descripcion, cantidad, fecha_produccion, id_produccion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.fecha_produccion = fecha_produccion
        self.id_produccion = id_produccion
        self.producto_id = None

    def execute(self):
        nuevo_producto = ProductoTerminado(
            nombre=self.nombre,
            descripcion=self.descripcion,
            cantidadDisponible=self.cantidad,
            fechaProduccion=self.fecha_produccion,
            idProduccion=self.id_produccion
        )
        session.add(nuevo_producto)
        session.commit()
        self.producto_id = nuevo_producto.id
        return f"Producto {self.nombre} agregado exitosamente."

    def undo(self):
        if self.producto_id:
            producto = session.query(ProductoTerminado).get(self.producto_id)
            if producto:
                session.delete(producto)
                session.commit()
                return f"Se deshizo la adición del producto {self.nombre}."
        return "No se pudo deshacer la operación."