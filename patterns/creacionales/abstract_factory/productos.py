from abc import ABC, abstractmethod

# Productos abstractos
class Pantalon(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

class Camisa(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

class Accesorio(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

# Productos concretos para invierno
class PantalonInvierno(Pantalon):
    def mostrar_info(self):
        return "Pantalón de invierno: abrigado y resistente al agua"

class CamisaInvierno(Camisa):
    def mostrar_info(self):
        return "Camisa de invierno: manga larga y térmica"

class AccesorioInvierno(Accesorio):
    def mostrar_info(self):
        return "Accesorio de invierno: bufanda y guantes"

# Productos concretos para verano
class PantalonVerano(Pantalon):
    def mostrar_info(self):
        return "Pantalón de verano: ligero y fresco"

class CamisaVerano(Camisa):
    def mostrar_info(self):
        return "Camisa de verano: manga corta y transpirable"

class AccesorioVerano(Accesorio):
    def mostrar_info(self):
        return "Accesorio de verano: sombrero y gafas de sol"