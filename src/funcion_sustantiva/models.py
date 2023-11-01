from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.core import Base


class FuncionSustantiva(Base):
    __tablename__ = "funcion_sustantiva"

    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String, unique=True, nullable=False, index=True)
    cantidad_horas = Column(Integer, nullable=False)
    descripcion = Column(String, nullable=True)

    # Relaciones entre tablas
    # Nombre del campo segun la tabla segun el sgdb
    dependencia = Column(Integer, ForeignKey("dependencia.id"), nullable=False)

    dependencia_ref = relationship("Dependencia", backref="funcion_sustantiva")

    # TODO: Agregar el campo de la tabla de actividad
    actividad = Column(Integer, ForeignKey("actividad.id"), nullable=False)
    actividad_ref = relationship("Actividad", backref="funcion_sustantiva")
