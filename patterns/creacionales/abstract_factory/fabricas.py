from abc import ABC, abstractmethod
from .productos import PantalonInvierno, CamisaInvierno, AccesorioInvierno, PantalonVerano, CamisaVerano, AccesorioVerano

# Fábrica abstracta
class FabricaDeConjuntos(ABC):
    @abstractmethod
    def crear_pantalon(self):
        pass

    @abstractmethod
    def crear_camisa(self):
        pass

    @abstractmethod
    def crear_accesorio(self):
        pass

# Fábricas concretas
class FabricaConjuntoInvierno(FabricaDeConjuntos):
    def crear_pantalon(self):
        return PantalonInvierno()

    def crear_camisa(self):
        return CamisaInvierno()

    def crear_accesorio(self):
        return AccesorioInvierno()

class FabricaConjuntoVerano(FabricaDeConjuntos):
    def crear_pantalon(self):
        return PantalonVerano()

    def crear_camisa(self):
        return CamisaVerano()

    def crear_accesorio(self):
        return AccesorioVerano()
    
def crear_conjunto(fabrica):
    pantalon = fabrica.crear_pantalon()
    camisa = fabrica.crear_camisa()
    accesorio = fabrica.crear_accesorio()
    return [pantalon, camisa, accesorio]