from modules.materia_prima.model import MateriaPrima
from db.connection import session
from patterns.estructurales.adapter.proveedor_adapter import SistemaProveedor
from patterns.estructurales.adapter.proveedor_adapter import ProveedorAdapter
from patterns.comportamentales.observer.gestor import GestorDeInventario
from patterns.comportamentales.observer.responsables import ResponsableDeCompras

# Instancia del adapter
sistema_externo = SistemaProveedor()
proveedor_adaptado = ProveedorAdapter(sistema_externo)

# Instancia del gestor de inventario y observador
gestor_inventario = GestorDeInventario()
responsable_compras = ResponsableDeCompras()
gestor_inventario.agregar_observador(responsable_compras)

#Registrar o actualizar información de materia prima uso de observer
def registrar_materia_prima(nombre, descripcion, cantidad, punto_reorden, proveedor, fecha_adquisicion):
    nueva_materia = MateriaPrima(
        nombre=nombre,
        descripcion=descripcion,
        cantidadDisponible=cantidad,
        puntoDeReorden=punto_reorden,
        proveedor=proveedor,
        fechaAdquisicion=fecha_adquisicion
    )
    session.add(nueva_materia)
    session.commit()
    print("Materia prima registrada exitosamente.")
    
    # Verificar si la cantidad está por debajo del punto de reorden
    if cantidad <= punto_reorden:
        gestor_inventario.notificar(f"Alerta: La materia prima {nombre} está por debajo del punto de reorden.")

# Controlar el inventario uso de observer
def controlar_inventario():
    materias = session.query(MateriaPrima).all()
    inventario = []
    for materia in materias:
        inventario.append({
            'id':materia.id,
            'nombre': materia.nombre,
            'descripcion': materia.descripcion,
            'cantidad': materia.cantidadDisponible,
            'punto_reorden': materia.puntoDeReorden,
            'proveedor': materia.proveedor,
            'fecha_adquisicion': materia.fechaAdquisicion

        })
        
        # Verificar si la cantidad está por debajo del punto de reorden
        if materia.cantidadDisponible <= materia.puntoDeReorden:
            gestor_inventario.notificar(f"Alerta: La materia prima {materia.nombre} está por debajo del punto de reorden.")
    
    return inventario

# Generar orden de compra si inventario es bajo
def generar_orden_compra():
    materias = session.query(MateriaPrima).all()
    for materia in materias:
        if materia.cantidadDisponible < materia.puntoDeReorden:
            # Verificar stock del proveedor usando el adapter
            stock_proveedor = proveedor_adaptado.obtener_stock(materia.id)
            if stock_proveedor > 0:
                cantidad_pedido = materia.puntoDeReorden - materia.cantidadDisponible
                orden_id, estado = proveedor_adaptado.realizar_pedido(materia.id, cantidad_pedido)
                print(f"Orden de compra generada para {materia.nombre}. ID: {orden_id}, Estado: {estado}")
            else:
                print(f"No hay stock disponible del proveedor para {materia.nombre}")

# Nueva función para actualizar stock desde proveedor
def actualizar_stock_desde_proveedor(id_materia_prima):
    materia = session.query(MateriaPrima).get(id_materia_prima)
    if materia:
        stock_proveedor = proveedor_adaptado.obtener_stock(materia.id)
        materia.cantidadDisponible += stock_proveedor
        session.commit()
        print(f"Stock de {materia.nombre} actualizado. Nuevo stock: {materia.cantidadDisponible}")
    else:
        print("Materia prima no encontrada")