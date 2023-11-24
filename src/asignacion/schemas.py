from pydantic import BaseModel
from typing import List, Dict, Optional

class Curso(BaseModel):
    cantidad_horas: int
    nombre: str
    id: int
    codigo: str

class FuncionSustantiva(BaseModel):
    id: int
    nombre: str
    cantidad_horas: int
    dependencia: int
    descripcion: str
    actividad: int

class AsignacionBase(BaseModel):
    docente: str
    periodo_academico: int
    horas_disponibles: Optional[int] = None
    cursos: List[Curso]
    funciones_sustantivas: List[FuncionSustantiva]

class AsignacionCreate(AsignacionBase):
    pass

class AsignacionRead(AsignacionBase):
    id: int

class AsignacionUpdate(AsignacionBase):
    pass
