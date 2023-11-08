from fastapi import APIRouter, HTTPException, status
from src.database.core import DbSession
from .schemas import (
    GrupoCreate,
    GrupoRead,
    GrupoUpdate,
)
from .service import (
    get_all,
    get_by_id,
    create,
    update,
    delete,
)

router = APIRouter()

error_object_plural = "grupos"
error_object_singular = "un grupo"


@router.get("")
def read_grupos(db_session: DbSession, skip: int = 0, limit: int = 100):
    grupos = get_all(db_session=db_session, skip=skip, limit=limit)
    if not grupos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No hay {error_object_plural} registrados"}],
        )
    return grupos


@router.get("/{id}", response_model=GrupoRead)
def get_grupo_by_id(db_session: DbSession, id: int):
    grupo = get_by_id(db_session=db_session, id=id)
    if not grupo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )
    return GrupoRead(**grupo.__dict__)


@router.post("", response_model=GrupoRead)
def create_grupo(grupo_in: GrupoCreate, db_session: DbSession):
    grupo = create(db_session=db_session, grupo=grupo_in)
    return GrupoRead(**grupo.__dict__)


@router.put("/{id}", response_model=GrupoRead)
def update_grupo(db_session: DbSession, id: int, grupo_in: GrupoUpdate):
    grupo_id = get_by_id(db_session=db_session, id=id)
    if not grupo_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )

    grupo = update(
        db_session=db_session,
        id=grupo_id.id,
        grupo_in=grupo_in,
    )
    return GrupoRead(**grupo.__dict__)


@router.delete("/{id}")
def delete_grupo(db_session: DbSession, id: int):
    grupo = get_by_id(db_session=db_session, id=id)
    if not grupo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )
    delete(db_session=db_session, id=id)
    return HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail=[{"msg": f"Se elimino {error_object_singular} con el id {id}"}],
    )
