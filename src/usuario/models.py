from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from src.database.core import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(String, nullable=False, unique=True)
    email = Column(String, primary_key=True, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email_verified = Column(Boolean, nullable=True, default=False)
    nombre = Column(String, nullable=True)
    apellido = Column(String, nullable=True)
    cedula = Column(Integer, nullable=True, unique=True)
    activo = Column(Boolean, nullable=True)
    programa = Column(String, nullable=True)
    horas_laborales = Column(Integer, nullable=True)

    # Definir la relación uno a uno con Dependencia
    dependencia = relationship("Dependencia", uselist=False, back_populates="usuario")
