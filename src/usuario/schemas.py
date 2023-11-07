from pydantic import BaseModel, conint
from pydantic import EmailStr
from typing import Optional, Any


class UsuarioBase(BaseModel):
    id: str | Any
    email: EmailStr
    email_verified: bool


class UsuarioCreate(UsuarioBase):
    password: str


class UsuarioRead(UsuarioBase):
    nombre: Optional[str]
    apellido: Optional[str]
    cedula: Optional[int]
    activo: Optional[bool]
    horas_laborales: Optional[int]
    programa: Optional[str]


class UsuarioUpdate(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    cedula: Optional[int]
    activo: Optional[bool]
    horas_laborales: Optional[int]
    programa: Optional[str]
