from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.database.core import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, nullable=False)
    cedula = Column(Integer, primary_key=True, nullable=False, unique=True, index=True)
    correo = Column(String, primary_key=True, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    perfil = Column(String, nullable=True)
    activo = Column(Boolean, nullable=False, default=True)
    rol = Column(String, nullable=False, default='DEFAULT')
    horas_laborales = Column(Integer, nullable=False, default=40)

