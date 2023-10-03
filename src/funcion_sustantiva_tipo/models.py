from sqlalchemy import Column, Integer, String
from src.database.core import Base
from src.models import TimeStampMixin


class TipoFuncionSustantiva(Base):
    __tablename__ = "tipo_funcion_sustantiva"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    nombre = Column(Integer, unique=True, nullable=False)
