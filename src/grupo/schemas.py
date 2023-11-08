from pydantic import BaseModel


class GrupoBase(BaseModel):
    nombre: str


class GrupoCreate(GrupoBase):
    pass


class GrupoRead(GrupoBase):
    id: int


class GrupoUpdate(GrupoBase):
    pass
