from fastapi import APIRouter, HTTPException, status
from src.database.core import DbSession
from .schemas import (
    ProgramaAcademicoCreate,
    ProgramaAcademicoRead,
    ProgramaAcademicoUpdate,
)
from .service import (
    create,
    get_all,
    get_by_id,
    get_by_codigo_snies,
    get_by_name,
    update_by_codigo_snies,
    delete_by_codigo_snies,
)


# Faltan crear validaciones

router = APIRouter()


@router.get("")
def read_programas_academicos(db_session: DbSession, skip: int = 0, limit: int = 100):
    programas_academicos = get_all(db_session=db_session, skip=skip, limit=limit)
    if not programas_academicos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "No hay programas academicos"}],
        )
    return programas_academicos


@router.get("/{programa_academico_id}", response_model=ProgramaAcademicoRead)
def get_programa_academico_by_id(db_session: DbSession, programa_academico_id: int):
    programa_academico = get_by_id(
        db_session=db_session, programa_academico_id=programa_academico_id
    )
    if not programa_academico:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "No existe un programa academico con este id"}],
        )
    return ProgramaAcademicoRead(**programa_academico.__dict__)


@router.get("/snies/{snies}", response_model=ProgramaAcademicoRead)
def get_programa_academico_by_codigo_snies(db_session: DbSession, snies: int):
    programa_academico = get_by_codigo_snies(db_session=db_session, snies=snies)
    if not programa_academico:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {"msg": f"No existe un programa academico el codigo snies {snies}"}
            ],
        )
    return ProgramaAcademicoRead(**programa_academico.__dict__)


@router.get("/nombre/{nombre}", response_model=ProgramaAcademicoRead)
def get_programa_academico_by_name(db_session: DbSession, nombre: str):
    programa_academico = get_by_name(db_session=db_session, nombre=nombre)
    if not programa_academico:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe un programa academico con el nombre {nombre}"}],
        )
    return ProgramaAcademicoRead(**programa_academico.__dict__)


@router.post("", response_model=ProgramaAcademicoRead)
def create_programa_academico(
    programa_academico_in: ProgramaAcademicoCreate, db_session: DbSession
):
    programa_academico_name = get_by_name(
        db_session=db_session, nombre=programa_academico_in.nombre
    )
    programa_academico_snies = get_by_codigo_snies(
        db_session=db_session, snies=programa_academico_in.codigo_snies
    )

    if programa_academico_name:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=[
                {
                    "msg": f"Ya existe un programa academico con el nombre {programa_academico_in.nombre}"
                }
            ],
        )
    if programa_academico_snies:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=[
                {
                    "msg": f"Ya existe un programa academico con el codigo snies {programa_academico_in.codigo_snies}"
                }
            ],
        )
    programa_academico = create(
        db_session=db_session, programa_academico_in=programa_academico_in
    )
    return ProgramaAcademicoRead(**programa_academico.__dict__)


@router.put("/snies/{snies}")
def update_programa_academico_by_codigo_snies(
    db_session: DbSession, snies: int, programa_academico_in: ProgramaAcademicoUpdate
):
    programa_academico_snies = get_by_codigo_snies(db_session=db_session, snies=snies)
    if not programa_academico_snies:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {"msg": f"No existe un programa academico el codigo snies {snies}"}
            ],
        )

    programa_academico_update = update_by_codigo_snies(
        db_session=db_session,
        programa_academico=programa_academico_snies,
        programa_academico_in=programa_academico_in,
    )

    return ProgramaAcademicoRead(**programa_academico_update.__dict__)


@router.delete("/snies/{snies}")
def delete_programa_academico_by_codigo_snies(db_session: DbSession, snies: int):
    programa_academico_snies = get_by_codigo_snies(db_session=db_session, snies=snies)
    if not programa_academico_snies:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {"msg": f"No existe un programa academico el codigo snies {snies}"}
            ],
        )
    delete_by_codigo_snies(db_session=db_session, codigo_snies=snies)
    return HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail=[{"msg": f"Se elimino el programa academico con codigo snies {snies}"}],
    )
