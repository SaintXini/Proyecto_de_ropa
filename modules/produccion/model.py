from db.connection import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float

class Produccion(Base):
    __tablename__ = 'Produccion'
    id = Column(Integer, primary_key=True)
    fechaInicio = Column(Date, nullable=False)
    fechaFin = Column(Date)
    estado = Column(String(50), nullable=False)
    idMateriaPrima = Column(Integer, ForeignKey('MateriaPrima.id'))
    tipoProducto = Column(String(50))
    cantidadProducida = Column(Integer)
    tiempo_estimado = Column(Float)