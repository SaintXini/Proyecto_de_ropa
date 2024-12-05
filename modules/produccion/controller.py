from db.connection import session
from modules.produccion.model import Produccion
from patterns.creacionales.factory.factory import ProductoFactory
from patterns.estructurales.facade.facade_produccion import FacadeDeProduccion
from patterns.estructurales.composite.proceso_especificos import ProcesoCorte, ProcesoTenido, ProcesoEnsamblaje, ProcesoAcabado, ProcesoCompuesto
from patterns.comportamentales.observer.gestor import GestorDeProduccion
from patterns.comportamentales.observer.responsables import ResponsableDeProduccion
from datetime import datetime

# Instancia del gestor de producción y observador
gestor_produccion = GestorDeProduccion()
responsable_produccion = ResponsableDeProduccion()
gestor_produccion.agregar_observador(responsable_produccion)

### composite
def crear_proceso_produccion(tipo_producto):
    proceso_principal = ProcesoCompuesto(f"Producción de {tipo_producto}", 0)
    
    # Agregar los procesos básicos
    proceso_principal.agregar_proceso(ProcesoCorte())
    
    # Si el producto requiere teñido
    if tipo_producto in ['camisa', 'pantalon','abrigo']:
        proceso_principal.agregar_proceso(ProcesoTenido())
    
    proceso_principal.agregar_proceso(ProcesoEnsamblaje())
    proceso_principal.agregar_proceso(ProcesoAcabado())
    
    return proceso_principal

def planificar_produccion(fecha_inicio, id_materia_prima, tipo_producto, cantidad_producida, estado_inicial):
    # Estados permitidos
    estados_validos = {'Pendiente', 'En proceso', 'Completado'}
    
    # Validar el estado inicial
    if estado_inicial not in estados_validos:
        raise ValueError(f"Estado '{estado_inicial}' no es válido. Los estados permitidos son: {estados_validos}")

    # Crear el proceso de producción usando el patrón Composite
    proceso = crear_proceso_produccion(tipo_producto)
    
    # Agregar los estados permitidos al proceso
    for estado in estados_validos:
        proceso.agregar_estado(estado)
    
    # Establecer el estado inicial
    proceso.cambiar_estado(estado_inicial)
    
    nueva_produccion = Produccion(
        fechaInicio=fecha_inicio,
        idMateriaPrima=id_materia_prima,
        tipoProducto=tipo_producto,
        cantidadProducida=cantidad_producida,
        estado=estado_inicial,
        tiempo_estimado=proceso.obtener_tiempo_total()
    )
    
    session.add(nueva_produccion)
    session.commit()

    # Si el estado inicial es "En proceso", ejecutar el proceso inmediatamente
    if estado_inicial == 'En proceso':
        proceso.ejecutar()
        proceso.cambiar_estado('Completado')  # Cambia el estado a 'Completado' después de ejecutar
        nueva_produccion.estado = proceso.estado
        session.commit()
    
    # Notificar el inicio de la producción
    gestor_produccion.notificar(f"Producción iniciada: {tipo_producto}, Cantidad: {cantidad_producida}, Estado: {estado_inicial}")
    
    return proceso.obtener_estado()


def finalizar_produccion(id_produccion, nombre_producto, descripcion, cantidad):
    produccion = session.query(Produccion).get(id_produccion)
    if produccion:
        produccion.cantidadProducida = cantidad  # Guardar la cantidad final
        produccion.estado = 'Completado'
        produccion.fechaFin = datetime.now()  # Registrar la fecha de finalización
        session.commit()
        
    gestor_produccion.notificar(f"Producción finalizada: {nombre_producto}, Cantidad final: {cantidad}")
    
    return "Producción finalizada y registrada con éxito."

def iniciar_nueva_produccion(tipo_producto, cantidad, estado, fecha_inicio):
    # Crear el proceso de producción
    proceso = crear_proceso_produccion(tipo_producto)
    tiempo_total = proceso.obtener_tiempo_total()

    # Guardar en la base de datos
    nueva_produccion = Produccion(
        fechaInicio=fecha_inicio,
        tipoProducto=tipo_producto,
        cantidadProducida=cantidad,
        estado=estado,
        tiempo_estimado=tiempo_total
    )
    session.add(nueva_produccion)
    session.commit()

    return f"Producción iniciada con el estado: {estado}"


def monitorear_progreso():
    producciones = session.query(Produccion).all()
    return [
        {
            'id': prod.id,
            'tipo_producto': prod.tipoProducto,
            'cantidad': prod.cantidadProducida,
            'estado': prod.estado,
            'tiempo_estimado': prod.tiempo_estimado,
            'fecha_inicio': prod.fechaInicio,
            'fecha_fin': prod.fechaFin
        }
        for prod in producciones
    ]

def iniciar_nueva_produccion(tipo_producto, cantidad):
    return FacadeDeProduccion.iniciar_produccion(tipo_producto, cantidad)

def obtener_estado_produccion():
    return FacadeDeProduccion.verificar_estado_produccion()

def generar_informe_produccion():
    return FacadeDeProduccion.generar_informe_produccion()

def finalizar_produccion(id_produccion, nombre_producto, descripcion, cantidad):
    return FacadeDeProduccion.registrar_producto_terminado(nombre_producto, descripcion, cantidad, id_produccion)