from pydantic import BaseModel, conint
from pydantic import EmailStr
from typing import Optional


class UsuarioBase(BaseModel):
    cedula: conint(strict=True, gt=9999999, lt=10000000000)
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
    id: int
    perfil: Optional[str]


class UsuarioUpdate(UsuarioBase):
    perfil: Optional[str]


print(UsuarioBase.schema())


# usuario = UsuarioBase.parse_raw('{"cedula":"Hola"}')
