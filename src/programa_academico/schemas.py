from pydantic import BaseModel


class ProgramaAcademicoBase(BaseModel):
    codigo_snies: int
    nombre: str
    director: str


class ProgramaAcademicoCreate(ProgramaAcademicoBase):
    pass


class ProgramaAcademicoRead(ProgramaAcademicoBase):
    id: int


class ProgramaAcademicoUpdate(ProgramaAcademicoBase):
    pass
