from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.core import Base


class Dependencia(Base):
    __tablename__ = "dependencia"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    nombre = Column(String, unique=True, nullable=False)

    # Definir la relación uno a uno con Usuario
    encargado = Column(Integer, ForeignKey("usuario.cedula"), nullable=False)
    usuario = relationship("Usuario", back_populates="dependencia")
