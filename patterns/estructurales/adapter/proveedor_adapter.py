from .proveedor_interno import ProveedorInterno
from .proveedor_system import SistemaProveedor

### esta siendo utilizado en el controlador de materia prima

class ProveedorAdapter(ProveedorInterno):
    def __init__(self, sistema_proveedor):
        self.sistema_proveedor = sistema_proveedor

    def obtener_stock(self, id_producto):
        resultado = self.sistema_proveedor.check_availability(id_producto)
        return resultado["available"]

    def realizar_pedido(self, id_producto, cantidad):
        resultado = self.sistema_proveedor.place_order(id_producto, cantidad)
        return resultado["order_id"], resultado["status"]

# Terminal borrar Martín
sistema_externo = SistemaProveedor()
proveedor_adaptado = ProveedorAdapter(sistema_externo)

stock = proveedor_adaptado.obtener_stock("MP001")
print(f"Stock disponible: {stock}")

orden_id, estado = proveedor_adaptado.realizar_pedido("MP001", 50)
print(f"Pedido realizado. ID: {orden_id}, Estado: {estado}")