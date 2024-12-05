from db.connection import session
from modules.producto.controller import ProductoTerminado
from .command import Command

class ActualizarProductoCommand(Command):
    def __init__(self, producto_id, nuevos_datos):
        self.producto_id = producto_id
        self.nuevos_datos = nuevos_datos
        self.datos_anteriores = None

    def execute(self):
        producto = session.query(ProductoTerminado).get(self.producto_id)
        if producto:
            self.datos_anteriores = {
                'nombre': producto.nombre,
                'descripcion': producto.descripcion,
                'cantidadDisponible': producto.cantidadDisponible,
                'fechaProduccion': producto.fechaProduccion,
                'idProduccion': producto.idProduccion
            }
            for key, value in self.nuevos_datos.items():
                setattr(producto, key, value)
            session.commit()
            return f"Producto {producto.nombre} actualizado exitosamente."
        return "Producto no encontrado."

    def undo(self):
        if self.datos_anteriores:
            producto = session.query(ProductoTerminado).get(self.producto_id)
            if producto:
                for key, value in self.datos_anteriores.items():
                    setattr(producto, key, value)
                session.commit()
                return f"Se deshizo la actualización del producto {producto.nombre}."
        return "No se pudo deshacer la operación."
