from pydantic import BaseModel
from typing import Optional


class ProgramaAcademicoBase(BaseModel):
    codigo_snies: int
    nombre: str
    descripcion: str


class ProgramaAcademicoCreate(ProgramaAcademicoBase):
    pass


class ProgramaAcademicoRead(ProgramaAcademicoBase):
    id: int


class ProgramaAcademicoUpdate(ProgramaAcademicoBase):
    pass
