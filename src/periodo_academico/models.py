from sqlalchemy import Column, Integer, String, Date, Boolean
from src.database.core import Base


class PeriodoAcademico(Base):
    __tablename__ = "periodo_academico"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    activo = Column(Boolean, default=True)
