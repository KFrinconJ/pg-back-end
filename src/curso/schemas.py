from pydantic import BaseModel


class CursoBase(BaseModel):
    nombre: str


class CursoCreate(CursoBase):
    pass


class CursoRead(CursoBase):
    id: int


class CursoUpdate(CursoBase):
    pass
