from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database.core import Base


class Grupo(Base):
    __tablename__ = "grupo"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    # Otras columnas de Grupo

    # # Define la relación entre Grupo y CursoAcademicoGrupo
    # cursos_academicos = relationship("CursoAcademicoGrupo", uselist=False, back_populates="grupo")
