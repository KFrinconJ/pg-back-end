from typing import Optional, List

from .models import ProgramaAcademico
from .schemas import (
    ProgramaAcademicoCreate,
    ProgramaAcademicoUpdate,
)


def get_by_id(*, db_session, programa_academico_id: int) -> Optional[ProgramaAcademico]:
    """Obtiene el programa academico por id."""
    return (
        db_session.query(ProgramaAcademico)
        .filter(ProgramaAcademico.id == programa_academico_id)
        .first()
    )


def get_by_codigo_snies(*, db_session, snies: int) -> Optional[ProgramaAcademico]:
    """Obtiene el programa academico por codigo_snies"""
    return (
        db_session.query(ProgramaAcademico)
        .filter(ProgramaAcademico.codigo_snies == snies)
        .first()
    )


def get_by_name(*, db_session, nombre: str) -> Optional[ProgramaAcademico]:
    """Obtiene el programa academico por nombre"""
    return (
        db_session.query(ProgramaAcademico)
        .filter(ProgramaAcademico.nombre == nombre)
        .first()
    )


def get_all(
    *, db_session, skip: int = 0, limit: int = 100
) -> List[Optional[ProgramaAcademico]]:
    """Obtine todos los programas academicos"""
    return db_session.query(ProgramaAcademico).offset(skip).limit(limit).all()


def create(
    *, db_session, programa_academico_in: ProgramaAcademicoCreate
) -> ProgramaAcademico:
    """Crea un nuevo programa academico"""
    programa_academico = ProgramaAcademico(**programa_academico_in.dict())
    db_session.add(programa_academico)
    db_session.commit()
    db_session.refresh(programa_academico)
    return programa_academico


def update_by_codigo_snies(
    *,
    db_session,
    programa_academico: ProgramaAcademico,
    programa_academico_in: ProgramaAcademicoUpdate
) -> ProgramaAcademico:
    programa_academico_data = programa_academico.__dict__
    update_data = programa_academico_in.dict(exclude_unset=True)

    for field in programa_academico_data:
        if field in update_data:
            setattr(programa_academico, field, update_data[field])

    db_session.commit()
    db_session.refresh(programa_academico)

    return programa_academico


def delete_by_codigo_snies(*, db_session, codigo_snies: int):
    programa_academico = (
        db_session.query(ProgramaAcademico)
        .filter(ProgramaAcademico.codigo_snies == codigo_snies)
        .first()
    )
    programa_academico.terms = []
    db_session.delete(programa_academico)
    db_session.commit()
