from .producto import  Producto

class Camisa(Producto):
    def mostrar_informacion(self):
        return f"Camisa: {self.nombre}, Descripción: {self.descripcion}, Cantidad: {self.cantidad}"

class Pantalon(Producto):
    def mostrar_informacion(self):
        return f"Pantalón: {self.nombre}, Descripción: {self.descripcion}, Cantidad: {self.cantidad}"

class Abrigo(Producto):
    def mostrar_informacion(self):
        return f"Abrigo: {self.nombre}, Descripción: {self.descripcion}, Cantidad: {self.cantidad}"
