from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from src.database.core import Base

class Asignacion(Base):
    __tablename__ = "asignacion"

    id = Column(Integer, primary_key=True, index=True)
    docente = Column(String, ForeignKey("usuario.email"), index=True)
    periodo_academico = Column(Integer, ForeignKey("periodo_academico.id"))
    horas_disponibles = Column(Integer)
    cursos = Column(JSON)
    funciones_sustantivas = Column(JSON)

    docente_rel = relationship("Usuario", backref="asignacion")
    periodo_academico_rel = relationship("PeriodoAcademico", backref="asignacion")
