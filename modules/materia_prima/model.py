from db.connection import Base
from sqlalchemy import Column, Integer, String, Date


class MateriaPrima(Base):
    __tablename__ = 'MateriaPrima'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255))
    cantidadDisponible = Column(Integer, nullable=False)
    puntoDeReorden = Column(Integer, nullable=False)
    proveedor = Column(String(100))
    fechaAdquisicion = Column(Date)