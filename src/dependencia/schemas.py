from pydantic import BaseModel
from typing import Optional


class DependenciaBase(BaseModel):
    nombre: str
    encargado: int


class DependenciaCreate(DependenciaBase):
    pass


class DependenciaRead(DependenciaBase):
    id: int
    encargado: int | str


class DependenciaUpdate(DependenciaBase):
    pass
