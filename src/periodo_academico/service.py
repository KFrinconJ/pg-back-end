from typing import Optional, List
from sqlalchemy.orm import Session
from .models import PeriodoAcademico
from .schemas import PeriodoAcademicoCreate, PeriodoAcademicoUpdate


def get_by_id(*, db_session: Session, id: int) -> Optional[PeriodoAcademico]:
    return db_session.query(PeriodoAcademico).filter(PeriodoAcademico.id == id).first()


def get_all(
    *, db_session, skip: int = 0, limit: int = 100
) -> List[Optional[PeriodoAcademico]]:
    """Obtine todas las actividades"""
    return db_session.query(PeriodoAcademico).offset(skip).limit(limit).all()


def create(
    *, db_session: Session, periodo_academico: PeriodoAcademicoCreate
) -> PeriodoAcademico:
    periodo_academico_db = PeriodoAcademico(**periodo_academico.dict())
    db_session.add(periodo_academico_db)
    db_session.commit()
    db_session.refresh(periodo_academico_db)
    return periodo_academico_db


def update(
    *,
    db_session: Session,
    id: int,
    periodo_academico_in: PeriodoAcademicoUpdate,
) -> PeriodoAcademico:
    periodo_academico = get_by_id(db_session=db_session, id=id)

    update_data = {**periodo_academico_in.dict(exclude_unset=True)}

    periodo_academico_data = periodo_academico.__dict__

    for field in periodo_academico_data:
        if field in update_data:
            setattr(periodo_academico, field, update_data[field])

    db_session.commit()  # Realizar la transacción para asegurarse de que la instancia esté en la sesión
    db_session.refresh(periodo_academico)

    return periodo_academico


def delete(
    *, db_session: Session, periodo_academico_id: int
) -> Optional[PeriodoAcademico]:
    periodo_academico_db = (
        db_session.query(PeriodoAcademico)
        .filter(PeriodoAcademico.id == periodo_academico_id)
        .first()
    )
    if periodo_academico_db:
        db_session.delete(periodo_academico_db)
        db_session.commit()
        return periodo_academico_db
    return None
