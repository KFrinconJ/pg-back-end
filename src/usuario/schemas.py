from pydantic import BaseModel, conint
from pydantic import EmailStr
from typing import Optional


class UsuarioBase(BaseModel):
    cedula: int
    correo: EmailStr
    nombre: str
    apellido: str
    activo: bool = True
    rol: str = "default"
    horas_laborales: int = 40


class UsuarioCreate(UsuarioBase):
    password: str
    perfil: Optional[str]


class UsuarioRead(UsuarioBase):
    perfil: Optional[str]


class UsuarioUpdate(UsuarioBase):
    perfil: Optional[str]
