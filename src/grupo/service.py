from typing import Optional, List
from sqlalchemy.orm import Session
from .models import Grupo
from .schemas import GrupoCreate, GrupoUpdate


def get_by_id(db_session: Session, id: int) -> Optional[Grupo]:
    return db_session.query(Grupo).filter(Grupo.id == id).first()


def get_all(db_session: Session, skip: int = 0, limit: int = 100) -> List[Grupo]:
    return db_session.query(Grupo).offset(skip).limit(limit).all()


def create(db_session: Session, grupo: GrupoCreate) -> Grupo:
    grupo_db = Grupo(**grupo.dict())
    db_session.add(grupo_db)
    db_session.commit()
    db_session.refresh(grupo_db)
    return grupo_db


def update(db_session: Session, id: int, grupo_in: GrupoUpdate) -> Grupo:
    grupo = get_by_id(db_session, id)
    if grupo:
        for field, value in grupo_in.dict().items():
            setattr(grupo, field, value)
        db_session.commit()
        db_session.refresh(grupo)
    return grupo


def delete(db_session: Session, id: int) -> Optional[Grupo]:
    grupo = get_by_id(db_session, id)
    if grupo:
        db_session.delete(grupo)
        db_session.commit()
    return None
