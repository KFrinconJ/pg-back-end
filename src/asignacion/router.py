from fastapi import APIRouter, HTTPException, status
from src.database.core import DbSession
from .schemas import (
    AsignacionCreate,
    AsignacionRead,
    AsignacionUpdate,
)
from .service import (
    create,
    get_all,
    get_by_id,
    update,
    delete,
)


router = APIRouter()

error_object_plural = "asignaciones"
error_object_singular = "la asignacion"


@router.get("")
def read_asignaciones(db_session: DbSession, skip: int = 0, limit: int = 100):
    asignaciones = get_all(db_session=db_session, skip=skip, limit=limit)
    if not asignaciones:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No hay {error_object_plural} registradas"}],
        )
    return asignaciones


@router.get("/{id}", response_model=AsignacionRead)
def get_asignacion_by_id(db_session: DbSession, id: int):
    asignacion = get_by_id(db_session=db_session, id=id)
    if not asignacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )
    return AsignacionRead(**asignacion.__dict__)


@router.post("", response_model=AsignacionRead)
def create_asignacion(asignacion_in: AsignacionCreate, db_session: DbSession):
    asignacion = create(db_session=db_session, asignacion=asignacion_in)
    return AsignacionRead(**asignacion.__dict__)


@router.put("/{id}", response_model=AsignacionUpdate)
def update_asignacion(db_session: DbSession, id: int, asignacion_in: AsignacionUpdate):
    asignacion_update = update(
        db_session=db_session, id=id, asignacion_in=asignacion_in
    )
    return AsignacionRead(**asignacion_update.__dict__)


@router.delete("/{id}")
def delete_asignacion(db_session: DbSession, id: int):
    asignacion_id = get_by_id(db_session=db_session, id=id)
    if not asignacion_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )
    delete(db_session=db_session, id=id)
    return HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail=[{"msg": f"Se elimino {error_object_singular} con el {id}"}],
    )
