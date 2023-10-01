from typing import Optional, List

from .models import ProgramaAcademico
from .schemas import ProgramaAcademicoCreate, ProgramaAcademicoRead


def get_by_id(*, db_session, programa_academico_id: int) -> Optional[ProgramaAcademico]:
    """Obtiene el programa academico por id."""
    return (
        db_session.query(ProgramaAcademico)
        .filter(ProgramaAcademico.id == programa_academico_id)
        .one_or_none()
    )


def create(
    *, db_session, programa_academico_in: ProgramaAcademicoCreate
) -> ProgramaAcademicoRead:
    """Crea un nuevo programa academico"""
    programa_academico = ProgramaAcademico(**programa_academico_in.dict())
    db_session.add(programa_academico)
    db_session.commit()
    db_session.refresh(programa_academico)
    return ProgramaAcademicoRead(**programa_academico.__dict__)


def get_all(
    *, db_session, skip: int = 0, limit: int = 100
) -> List[Optional[ProgramaAcademico]]:
    return db_session.query(ProgramaAcademico).offset(skip).limit(limit).all()
