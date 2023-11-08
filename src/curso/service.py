from typing import Optional, List
from sqlalchemy.orm import Session
from .models import CursoAcademico
from .schemas import CursoCreate, CursoUpdate


def get_by_id(db_session: Session, id: int) -> Optional[CursoAcademico]:
    return db_session.query(CursoAcademico).filter(CursoAcademico.id == id).first()


def get_all(
    db_session: Session, skip: int = 0, limit: int = 100
) -> List[CursoAcademico]:
    return db_session.query(CursoAcademico).offset(skip).limit(limit).all()


def create(db_session: Session, curso_in: CursoCreate) -> CursoAcademico:
    curso_db = CursoAcademico(**curso_in.dict())
    db_session.add(curso_db)
    db_session.commit()
    db_session.refresh(curso_db)
    return curso_db


def update(db_session: Session, id: int, curso_in: CursoUpdate) -> CursoAcademico:
    curso = get_by_id(db_session, id)
    if curso:
        for field, value in curso_in.dict().items():
            setattr(curso, field, value)
        db_session.commit()
        db_session.refresh(curso)
    return curso


def delete(db_session: Session, id: int) -> Optional[CursoAcademico]:
    curso = get_by_id(db_session, id)
    if curso:
        db_session.delete(curso)
        db_session.commit()
    return None
