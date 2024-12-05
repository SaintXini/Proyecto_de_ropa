from db.connection import session
from modules.producto.model import ProductoTerminado
from patterns.comportamentales.command.agregar_comm import AgregarProductoCommand
from patterns.comportamentales.command.retirar_comm import RetirarProductoCommand
from patterns.comportamentales.command.actualizar_comm import ActualizarProductoCommand
from patterns.comportamentales.command.invoker import Invoker

# Función para registrar productos terminados
invoker = Invoker()

def registrar_producto(nombre, descripcion, cantidad, fecha_produccion, id_produccion):
    command = AgregarProductoCommand(nombre, descripcion, cantidad, fecha_produccion, id_produccion)
    return invoker.execute_command(command)

def retirar_producto(producto_id):
    command = RetirarProductoCommand(producto_id)
    return invoker.execute_command(command)

def actualizar_producto(producto_id, nuevos_datos):
    command = ActualizarProductoCommand(producto_id, nuevos_datos)
    return invoker.execute_command(command)

def deshacer_ultima_accion():
    return invoker.undo_last_command()

def controlar_inventario_productos():
    return session.query(ProductoTerminado).all()