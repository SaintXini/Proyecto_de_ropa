from .proceso_simple import ProcesoSimple
from .proceso_compuesto import ProcesoCompuesto

### todo esto se manda al controlador de produccion

class ProcesoCorte(ProcesoSimple):
    def __init__(self):
        super().__init__("Corte", 30)  # 30 minutos estimados

class ProcesoTenido(ProcesoCompuesto):
    def __init__(self):
        super().__init__("Teñido", 120)  # 2 horas estimadas
        # Subprocesos del teñido
        self.agregar_proceso(ProcesoSimple("Preparación de tinte", 20))
        self.agregar_proceso(ProcesoSimple("Aplicación de tinte", 60))
        self.agregar_proceso(ProcesoSimple("Secado", 40))

class ProcesoEnsamblaje(ProcesoCompuesto):
    def __init__(self):
        super().__init__("Ensamblaje", 90)  # 1.5 horas estimadas
        # Subprocesos del ensamblaje
        self.agregar_proceso(ProcesoSimple("Unión de piezas", 45))
        self.agregar_proceso(ProcesoSimple("Costura", 30))
        self.agregar_proceso(ProcesoSimple("Control de calidad", 15))

class ProcesoAcabado(ProcesoSimple):
    def __init__(self):
        super().__init__("Acabado", 45) 