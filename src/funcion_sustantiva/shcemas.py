from pydantic import BaseModel


class FuncionSustantivaBase(BaseModel):
    nombre: str
    activo: bool


class FuncionSustantivaCreate(FuncionSustantivaBase):
    tipo: int


class FuncionSustantivaRead(FuncionSustantivaBase):
    id: int
    tipo: int


class FuncionSustantivaUpdate(FuncionSustantivaBase):
    tipo: int
