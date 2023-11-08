from pydantic import BaseModel
from typing import Optional


class DependenciaBase(BaseModel):
    nombre: str
    encargado: str


class DependenciaCreate(DependenciaBase):
    pass


class DependenciaRead(DependenciaBase):
    id: int
    encargado: str


class DependenciaUpdate(DependenciaBase):
    pass
