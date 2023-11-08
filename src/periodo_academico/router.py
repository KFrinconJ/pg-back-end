from fastapi import APIRouter, HTTPException, status
from src.database.core import DbSession
from .schemas import (
    PeriodoAcademicoCreate,
    PeriodoAcademicoRead,
    PeriodoAcademicoUpdate,
)
from .service import (
    get_all,
    get_by_id,
    create,
    update,
    delete,
)

router = APIRouter()

error_object_plural = "periodos académicos"
error_object_singular = "un periodo académico"


@router.get("")
def read_periodos_academicos(db_session: DbSession, skip: int = 0, limit: int = 100):
    periodos_academicos = get_all(db_session=db_session, skip=skip, limit=limit)
    if not periodos_academicos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No hay {error_object_plural} registradas"}],
        )
    return periodos_academicos


@router.get("/{id}", response_model=PeriodoAcademicoRead)
def get_periodo_academico_by_id(db_session: DbSession, id: int):
    periodo_academico = get_by_id(db_session=db_session, id=id)
    if not periodo_academico:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )
    return PeriodoAcademicoRead(**periodo_academico.__dict__)


@router.post("", response_model=PeriodoAcademicoRead)
def create_periodo_academico(
    periodo_academico_in: PeriodoAcademicoCreate, db_session: DbSession
):
    periodo_academico = create(
        db_session=db_session, periodo_academico=periodo_academico_in
    )
    return PeriodoAcademicoRead(**periodo_academico.__dict__)


@router.put("/{id}", response_model=PeriodoAcademicoRead)
def update_periodo_academico(
    db_session: DbSession, id: int, periodo_academico_in: PeriodoAcademicoUpdate
):
    periodo_academico_id = get_by_id(db_session=db_session, id=id)
    if not periodo_academico_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )

    periodo_academico = update(
        db_session=db_session,
        id=periodo_academico_id.id,
        periodo_academico_in=periodo_academico_in,
    )
    return PeriodoAcademicoRead(**periodo_academico.__dict__)


@router.delete("/{id}")
def delete_periodo_academico(db_session: DbSession, id: int):
    periodo_academico = delete(db_session=db_session, periodo_academico_id=id)
    if not periodo_academico:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )
    return HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail=[{"msg": f"Se elimino {error_object_singular} con el id {id}"}],
    )
