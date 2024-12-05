from db.connection import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey

class ProductoTerminado(Base):
    __tablename__ = 'ProductoTerminado'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255))
    cantidadDisponible = Column(Integer, nullable=False)
    fechaProduccion = Column(Date, nullable=False)
    idProduccion = Column(Integer, ForeignKey('Produccion.id'))

