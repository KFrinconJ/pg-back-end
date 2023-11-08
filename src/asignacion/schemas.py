from pydantic import BaseModel
from typing import List


class AsignacionBase(BaseModel):
    docente: str
    periodo_academico: int
    horas_disponibles: int | None


class AsignacionCreate(AsignacionBase):
    pass


class AsignacionRead(AsignacionBase):
    id: int


class AsignacionUpdate(AsignacionBase):
    pass
