from fastapi import APIRouter, HTTPException, status
from src.database.core import DbSession
from .schemas import (
    ActividadCreate,
    ActividadRead,
    ActividadUpdate,
)
from .service import (
    create,
    get_all,
    get_by_id,
    update,
    delete,
)


router = APIRouter()

error_object_plural = "actividades"
error_object_singular = "una actividad"


@router.get("")
def read_actividades(db_session: DbSession, skip: int = 0, limit: int = 100):
    actividades = get_all(db_session=db_session, skip=skip, limit=limit)
    if not actividades:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No hay {error_object_plural} registradas"}],
        )
    return actividades


@router.get("/{id}", response_model=ActividadRead)
def get_actividad_by_id(db_session: DbSession, id: int):
    actividad = get_by_id(db_session=db_session, id=id)
    if not actividad:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )
    return ActividadRead(**actividad.__dict__)


@router.post("", response_model=ActividadRead)
def create_usuario(actividad_in: ActividadCreate, db_session: DbSession):
    actividad = create(db_session=db_session, actividad_in=actividad_in)
    return ActividadRead(**actividad.__dict__)


@router.put("/{id}", response_model=ActividadUpdate)
def update_actividad(db_session: DbSession, id: int, actividad_in: ActividadUpdate):
    actividad_update = update(
        db_session=db_session, actividad_id=id, actividad_in=actividad_in
    )
    return ActividadRead(**actividad_update.__dict__)


@router.delete("/{id}")
def delete_actividad(db_session: DbSession, id: int):
    actividad_id = get_actividad_by_id(db_session=db_session, id=id)
    if not actividad_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )
    delete(db_session=db_session, id=id)
    return HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail=[{"msg": f"Se elimino el usuario con el {id}"}],
    )
