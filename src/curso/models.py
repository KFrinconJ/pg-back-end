from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database.core import Base


class CursoAcademico(Base):
    __tablename__ = "curso_academico"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True, nullable=False)
    codigo = Column(String, unique=True, nullable=False)
    cantidad_horas = Column(Integer, nullable=False)

    # curso_academico_grupo = relationship("CursoAcademicoGrupo", back_populates="curso")
