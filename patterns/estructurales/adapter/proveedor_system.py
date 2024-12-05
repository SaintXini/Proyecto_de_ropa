### esta siendo utilizado en el controlador de materia prima

class SistemaProveedor:
    def check_availability(self, product_id):
        # Simulamos la respuesta del sistema externo
        return {"product_id": product_id, "available": 100}

    def place_order(self, product_id, quantity):
        # Simulamos la respuesta del sistema externo
        return {"order_id": 12345, "status": "confirmed"}
