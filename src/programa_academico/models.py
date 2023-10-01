from sqlalchemy import Column, Integer, String
from src.database.core import Base
from src.models import TimeStampMixin


class ProgramaAcademico(Base):
    __tablename__ = "programa_academico"

    id = Column(Integer, primary_key=True, index=True)
    codigo_snies = Column(Integer, unique=True)
    nombre = Column(String)
    descripcion = Column(String)
