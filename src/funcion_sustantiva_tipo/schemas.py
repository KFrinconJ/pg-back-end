from pydantic import BaseModel
from typing import Optional


class TipoFuncionSustantivaBase(BaseModel):
    nombre: str


class TipoFuncionSustantivaCreate(TipoFuncionSustantivaBase):
    pass


class TipoFuncionSustantivaRead(TipoFuncionSustantivaBase):
    id: int


class TipoFuncionSustantivaUpdate(TipoFuncionSustantivaBase):
    pass
