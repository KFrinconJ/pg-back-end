from fastapi import APIRouter, HTTPException, status
from src.database.core import DbSession
from .schemas import (
    DependenciaCreate,
    DependenciaRead,
    DependenciaUpdate,
)
from .service import create, get_all, get_by_id, get_by_name, delete, update

from src.usuario.service import get_by_cedula


router = APIRouter()

error_object_plural = "Dependencias"
error_object_singular = "una Dependencia"


@router.get("")
def read_dependencias(db_session: DbSession, skip: int = 0, limit: int = 100):
    dependencia = get_all(db_session=db_session, skip=skip, limit=limit)
    if not dependencia:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No hay {error_object_plural}"}],
        )
    return dependencia


@router.get("/{id}", response_model=DependenciaRead)
def get_dependencia(db_session: DbSession, id: int):
    programa_academico = get_by_id(db_session=db_session, id=id)
    if not programa_academico:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )
    return DependenciaRead(**programa_academico.__dict__)


@router.post("", response_model=DependenciaRead)
def create_dependencia(dependencia_in: DependenciaCreate, db_session: DbSession):
    dependencia_name = get_by_name(db_session=db_session, nombre=dependencia_in.nombre)

    encargado = get_by_cedula(db_session=db_session, cedula=dependencia_in.encargado)

    if not encargado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {
                    "msg": f"No se encuentra un usuario[encargado] con la cedula {dependencia_in.encargado}"
                }
            ],
        )

    if dependencia_name:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=[
                {
                    "msg": f"Ya existe {error_object_singular} con el nombre {dependencia_in.nombre}"
                }
            ],
        )

    dependencia = create(db_session=db_session, dependencia_in=dependencia_in)
    return DependenciaRead(**dependencia.__dict__)


@router.put("/{id}")
def update_dependencia(
    db_session: DbSession, id: int, dependencia_in: DependenciaUpdate
):
    dependencia = get_by_id(db_session=db_session, id=id)
    dependencia_name = get_by_name(db_session=db_session, nombre=dependencia_in.nombre)

    encargado = get_by_cedula(db_session=db_session, cedula=dependencia_in.encargado)

    if not encargado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {
                    "msg": f"No se encuentra un usuario[encargado] con la cedula {dependencia_in.encargado}"
                }
            ],
        )

    if dependencia_name:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=[
                {
                    "msg": f"Ya existe {error_object_singular} con el nombre {dependencia_in.nombre}"
                }
            ],
        )
    dependencia_update = update(
        db_session=db_session,
        dependencia=dependencia,
        dependencia_in=dependencia_in,
    )

    return DependenciaRead(**dependencia_update.__dict__)


@router.delete("/{id}")
def delete_dependencia(db_session: DbSession, id: int):
    dependencia = get_by_id(db_session=db_session, id=id)
    if not dependencia:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )
    delete(db_session=db_session, id=id)
    return HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail=[{"msg": f"Se elimino {error_object_singular} con id {id}"}],
    )
