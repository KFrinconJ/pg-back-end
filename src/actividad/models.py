from sqlalchemy import Column, Integer, String
from src.database.core import Base


class Actividad(Base):
    __tablename__ = "actividad"

    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String, unique=True, nullable=False, index=True)
    cantidad_horas = Column(Integer, nullable=False)
