from pydantic import BaseModel


class ActividadBase(BaseModel):
    nombre: str
    cantidad_horas: int


class ActividadCreate(ActividadBase):
    pass


class ActividadRead(ActividadBase):
    id: int


class ActividadUpdate(ActividadBase):
    pass