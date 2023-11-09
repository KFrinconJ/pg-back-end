from pydantic import BaseModel


class CursoAcademicoGrupoBase(BaseModel):
    curso_academico_id: int
    grupo_id: int


class CursoAcademicoGrupoCreate(CursoAcademicoGrupoBase):
    pass


class CursoAcademicoGrupoRead(CursoAcademicoGrupoBase):
    id: int


class CursoAcademicoGrupoUpdate(CursoAcademicoGrupoBase):
    pass
