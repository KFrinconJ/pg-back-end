from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.database.core import Base
from src.models import TimeStampMixin


class FuncionSustantiva(Base):
    __tablename__ = "funcion_sustantiva"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    nombre = Column(String, unique=True, nullable=False)
    activo = Column(Boolean, default=False, nullable=False)

    # Relaciones entre tablas
    tipo = Column(Integer, ForeignKey("tipo_funcion_sustantiva.id"), nullable=False)
    tipo_id = relationship("TipoFuncionSustantiva", backref="funcion_sustantiva")
