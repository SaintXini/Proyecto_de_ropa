from .prendas import Camisa, Pantalon, Abrigo

class ProductoFactory:
    @staticmethod
    def crear_producto(tipo_producto, nombre, descripcion, cantidad):
        if tipo_producto == 'camisa':
            return Camisa(nombre, descripcion, cantidad)
        elif tipo_producto == 'pantalon':
            return Pantalon(nombre, descripcion, cantidad)
        elif tipo_producto == 'abrigo':
            return Abrigo(nombre, descripcion, cantidad)
        else:
            raise ValueError(f"Tipo de producto desconocido: {tipo_producto}")
