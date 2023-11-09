from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.database.core import Base


class CursoAcademicoGrupo(Base):
    __tablename__ = "curso_academico_grupo"

    id = Column(Integer, primary_key=True, index=True)
    curso_academico_id = Column(
        Integer, ForeignKey("curso_academico.id"), nullable=False
    )
    grupo_id = Column(Integer, ForeignKey("grupo.id"), nullable=False)

    grupo = relationship("Grupo", back_populates="cursos_academicos")

    # Definir la relación con la tabla "curso"
    curso = relationship("Curso", back_populates="curso_academico_grupo")
