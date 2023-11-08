from fastapi import APIRouter, HTTPException, status
from src.database.core import DbSession
from .schemas import (
    CursoCreate,
    CursoRead,
    CursoUpdate,
)
from .service import (
    create,
    get_all,
    get_by_id,
    update,
    delete,
)


router = APIRouter()

error_object_plural = "cursos"
error_object_singular = "un curso"


@router.get("")
def read_cursos(db_session: DbSession, skip: int = 0, limit: int = 100):
    cursos = get_all(db_session=db_session, skip=skip, limit=limit)
    if not cursos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No hay {error_object_plural} registrados"}],
        )
    return cursos


@router.get("/{id}", response_model=CursoRead)
def get_curso_by_id(db_session: DbSession, id: int):
    curso = get_by_id(db_session=db_session, id=id)
    if not curso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )
    return CursoRead(**curso.__dict__)


@router.post("", response_model=CursoRead)
def create_usuario(curso_in: CursoCreate, db_session: DbSession):
    curso = create(db_session=db_session, curso_in=curso_in)
    return CursoRead(**curso.__dict__)


@router.put("/{id}", response_model=CursoUpdate)
def update_curso(db_session: DbSession, id: int, curso_in: CursoUpdate):
    curso_update = update(db_session=db_session, id=id, curso_in=curso_in)
    return CursoRead(**curso_update.__dict__)


@router.delete("/{id}")
def delete_curso(db_session: DbSession, id: int):
    curso_id = get_by_id(db_session=db_session, id=id)
    if not curso_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )
    delete(db_session=db_session, id=id)
    return HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail=[{"msg": f"Se elimino {error_object_singular} con el {id}"}],
    )
