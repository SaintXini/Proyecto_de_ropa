### se utiliza un nuevo html donde se clasifica por tipos de ropas que se desean

from .productos import (
    PantalonInvierno,
    CamisaInvierno,
    AccesorioInvierno,
    PantalonVerano,
    CamisaVerano,
    AccesorioVerano,
)

from .fabricas import FabricaConjuntoInvierno, FabricaConjuntoVerano

__all__ = [
    "PantalonInvierno",
    "CamisaInvierno",
    "AccesorioInvierno",
    "PantalonVerano",
    "CamisaVerano",
    "AccesorioVerano",
    "FabricaConjuntoInvierno",
    "FabricaConjuntoVerano",
]