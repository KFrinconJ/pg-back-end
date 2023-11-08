from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from src.database.core import Base


class Asignacion(Base):
    __tablename__ = "asignacion"

    id = Column(Integer, primary_key=True, index=True)
    docente = Column(String, ForeignKey("usuario.email"), index=True)
    periodo_academico = Column(Integer, ForeignKey("periodo_academico.id"))
    horas_disponibles = Column(Integer)

    docente_rel = relationship("Usuario", backref="asignacion")

    periodo_academico_rel = relationship("PeriodoAcademico", backref="asignacion")
    # curso_academico_grupos_rel = relationship(
    #     "AsignacionCursoAcademico", back_populates="asignacion_rel"
    # )
    # funciones_sustantivas_rel = relationship(
    #     "AsignacionFuncionSustantiva", back_populates="asignacion_rel"
    # )
