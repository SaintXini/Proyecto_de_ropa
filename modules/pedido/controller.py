from db.connection import session
from modules.pedido.model import Pedido
from patterns.comportamentales.strategy.contexto import ContextoDeDistribucion
from patterns.comportamentales.strategy.distribuciones import DistribucionRapida, DistribucionEconomica

# aca se aplica en el codigo strategy

contexto_distribucion = ContextoDeDistribucion()

def recibir_pedido(cliente_name, fecha_pedido, estado, direccion_envio, tipo_distribucion, producto, cantidad):
    nuevo_pedido = Pedido(
        cliente_name=cliente_name,
        fechaPedido=fecha_pedido,
        estado=estado,
        direccionEnvio=direccion_envio,
        producto=producto,
        cantidad=cantidad
    )
    session.add(nuevo_pedido)
    session.commit()
    

def obtener_pedidos():
    pedidos = session.query(Pedido).all()
    lista_pedidos = []
    
    for pedido in pedidos:
        tipo_distribucion = "rápida" if pedido.estado == "pendiente" else "económica"
        lista_pedidos.append({
            'id': pedido.id,
            'cliente_name': pedido.cliente_name,
            'fechaPedido': str(pedido.fechaPedido),
            'fechaEnvio': str(pedido.fechaEnvio) if pedido.fechaEnvio else None,
            'estado': pedido.estado,
            'direccionEnvio': pedido.direccionEnvio,
            'producto': pedido.producto,
            'cantidad': pedido.cantidad,
            'tipo_distribucion':tipo_distribucion
        })
    
    return lista_pedidos

def monitorear_pedidos():
    pedidos = session.query(Pedido).all()
    for pedido in pedidos:
        print(f"Pedido {pedido.id}: Estado {pedido.estado}, Fecha de Pedido: {pedido.fechaPedido}")