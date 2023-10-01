from fastapi import APIRouter, HTTPException, status

from src.database.core import DbSession
from .schemas import ProgramaAcademicoCreate, ProgramaAcademicoRead
from .service import create, get_all


# Faltan crear validaciones

router = APIRouter()


@router.get("")
def read_programas_academicos(db_session: DbSession, skip: int = 0, limit: int = 100):
    programas_academicos = get_all(db_session=db_session, skip=skip, limit=limit)
    return programas_academicos


@router.post("", response_model=ProgramaAcademicoRead)
def create_programa_academico(
    programa_academico_in: ProgramaAcademicoCreate, db_session: DbSession
):
    return create(db_session=db_session, programa_academico_in=programa_academico_in)
