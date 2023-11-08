from pydantic import BaseModel
from datetime import date


class PeriodoAcademicoBase(BaseModel):
    nombre: str
    fecha_inicio: date
    fecha_fin: date
    activo: bool = True


# Esquema Pydantic para la creación de un periodo académico
class PeriodoAcademicoCreate(PeriodoAcademicoBase):
    pass


# Esquema Pydantic para la lectura de un periodo académico
class PeriodoAcademicoRead(PeriodoAcademicoBase):
    id: int


# Esquema Pydantic para la actualización de un periodo académico
class PeriodoAcademicoUpdate(PeriodoAcademicoBase):
    pass
