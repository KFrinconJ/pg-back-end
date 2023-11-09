from typing import Optional, List
from sqlalchemy.orm import Session
from .models import CursoAcademicoGrupo
from .schemas import CursoAcademicoGrupoCreate, CursoAcademicoGrupoUpdate


def get_by_id(db_session: Session, id: int) -> Optional[CursoAcademicoGrupo]:
    return (
        db_session.query(CursoAcademicoGrupo)
        .filter(CursoAcademicoGrupo.id == id)
        .first()
    )


def get_all(
    db_session: Session, skip: int = 0, limit: int = 100
) -> List[CursoAcademicoGrupo]:
    return db_session.query(CursoAcademicoGrupo).offset(skip).limit(limit).all()


def create(
    db_session: Session, cursogrupo: CursoAcademicoGrupoCreate
) -> CursoAcademicoGrupo:
    cursogrupo_db = CursoAcademicoGrupo(**cursogrupo.dict())
    db_session.add(cursogrupo_db)
    db_session.commit()
    db_session.refresh(cursogrupo_db)
    return cursogrupo_db


def update(
    db_session: Session, id: int, cursogrupo_in: CursoAcademicoGrupoUpdate
) -> CursoAcademicoGrupo:
    cursogrupo = get_by_id(db_session, id)
    if cursogrupo:
        for field, value in cursogrupo_in.dict().items():
            setattr(cursogrupo, field, value)
        db_session.commit()
        db_session.refresh(cursogrupo)
    return cursogrupo


def delete_cursogrupo(db_session: Session, id: int) -> Optional[CursoAcademicoGrupo]:
    cursogrupo = get_by_id(db_session, id)
    if cursogrupo:
        db_session.delete(cursogrupo)
        db_session.commit()
    return cursogrupo
