from pydantic import BaseModel


class CursoBase(BaseModel):
    nombre: str
    codigo:str
    cantidad_horas:int


class CursoCreate(CursoBase):
    pass


class CursoRead(CursoBase):
    id: int


class CursoUpdate(CursoBase):
    pass
