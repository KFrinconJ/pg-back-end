from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.core import Base


class ProgramaAcademico(Base):
    __tablename__ = "programa_academico"

    id = Column(Integer, primary_key=True, index=True)
    codigo_snies = Column(Integer, unique=True)
    nombre = Column(String, unique=True)

    # Relacion entre tablas
    # Nombre del campo
    director = Column(String, ForeignKey("usuario.email"), nullable=False)
    director_ref = relationship("Usuario", backref="programa_academico")
