from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.database.core import Base


class PeriodoAcademico(Base):
    __tablename__ = "periodo_academico"

    id = Column(Integer, primary_key="id")
    nombre = Column()