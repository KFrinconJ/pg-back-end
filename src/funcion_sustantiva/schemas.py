from pydantic import BaseModel


class FuncionSustantivaBase(BaseModel):
    nombre: str
    cantidad_horas: int
    descripcion: str
    actividad: int
    dependencia: int


class FuncionSustantivaCreate(FuncionSustantivaBase):
    dependencia: int


class FuncionSustantivaRead(FuncionSustantivaBase):
    id: int
    dependencia: int | str
    actividad: int | str


class FuncionSustantivaUpdate(FuncionSustantivaBase):
    dependencia: int
