from typing import Optional, List

from .models import ProgramaAcademico
from .schemas import (
    ProgramaAcademicoCreate,
    ProgramaAcademicoUpdate,
)

from src.usuario.service import get_by_cedula
from src.usuario.models import Usuario


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

    director = get_by_cedula(
        db_session=db_session, cedula=programa_academico_in.director
    )

    nombre = programa_academico_in.nombre.upper()

    programa_academico = ProgramaAcademico(
        **programa_academico_in.dict(exclude={"director", "nombre"}),
        director=director.cedula,
        nombre=nombre
    )
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
    director = get_by_cedula(
        db_session=db_session, cedula=programa_academico_in.director
    )
    programa_academico_data = programa_academico.__dict__
    update_data = {
        "codigo_snies": programa_academico_in.codigo_snies,
        "nombre": programa_academico_in.nombre.upper(),
        "director": director.cedula,
    }

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
