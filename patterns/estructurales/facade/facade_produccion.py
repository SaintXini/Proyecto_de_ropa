from db.connection import session
from modules.produccion.model import Produccion
from modules.materia_prima.controller import controlar_inventario
from modules.producto.controller import registrar_producto
from datetime import datetime

class FacadeDeProduccion:
    @staticmethod
    def iniciar_produccion(tipo_producto, cantidad):
        # Verificar inventario de materia prima
        inventario = controlar_inventario()
        materia_prima_suficiente = any(item['cantidad'] >= cantidad for item in inventario)
        
        if not materia_prima_suficiente:
            return "No hay suficiente materia prima para iniciar la producción."
        
        # Iniciar la producción
        fecha_inicio = datetime.now().strftime("%Y-%m-%d")
        id_materia_prima = inventario[0]['id']  # Usamos la primera materia prima disponible como ejemplo
        
        nueva_produccion = Produccion(
            fechaInicio=fecha_inicio,
            idMateriaPrima=id_materia_prima,
            tipoProducto=tipo_producto,
            cantidadProducida=cantidad,
            estado='En proceso'
        )
        session.add(nueva_produccion)
        session.commit()
        
        return "Producción iniciada con éxito."

    @staticmethod
    def verificar_estado_produccion():
        producciones = session.query(Produccion).all()
        return [
            {
                'id': produccion.id,
                'fechaInicio': produccion.fechaInicio.strftime("%Y-%m-%d") if produccion.fechaInicio else None,
                'estado': produccion.estado,
                'tipo_producto': produccion.tipoProducto,
                'cantidad': produccion.cantidadProducida,
                'fecha_fin': produccion.fechaFin.strftime("%Y-%m-%d") if produccion.fechaFin else None
            }
            for produccion in producciones
        ]


    @staticmethod
    def generar_informe_produccion():
        producciones = FacadeDeProduccion.verificar_estado_produccion()
        total_producciones = len(producciones)
        producciones_en_proceso = sum(1 for p in producciones if p['estado'] == 'En proceso')
        producciones_completadas = total_producciones - producciones_en_proceso
        
        return {
            "total_producciones": total_producciones,
            "producciones_en_proceso": producciones_en_proceso,
            "producciones_completadas": producciones_completadas
        }

    @staticmethod
    def registrar_producto_terminado(nombre, descripcion, cantidad, id_produccion):
        fecha_produccion = datetime.now().strftime("%Y-%m-%d")
        registrar_producto(nombre, descripcion, cantidad, fecha_produccion, id_produccion)
        
        # Actualizar el estado de la producción
        produccion = session.query(Produccion).get(id_produccion)
        if produccion:
            produccion.estado = 'Completado'
            session.commit()
        
        return "Producto terminado registrado con éxito."