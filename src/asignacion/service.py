from typing import Optional, List
from sqlalchemy.orm import Session
from .models import Asignacion
from .schemas import AsignacionCreate, AsignacionUpdate


def get_by_id(db_session: Session, id: int) -> Optional[Asignacion]:
    return db_session.query(Asignacion).filter(Asignacion.id == id).first()


def get_all(db_session: Session, skip: int = 0, limit: int = 100) -> List[Asignacion]:
    return db_session.query(Asignacion).offset(skip).limit(limit).all()


def create(db_session: Session, asignacion: AsignacionCreate) -> Asignacion:
    asignacion_db = Asignacion(**asignacion.dict())
    db_session.add(asignacion_db)
    db_session.commit()
    db_session.refresh(asignacion_db)
    return asignacion_db


def update(
    db_session: Session, id: int, asignacion_in: AsignacionUpdate
) -> Optional[Asignacion]:
    asignacion = get_by_id(db_session, id)
    if asignacion:
        for field, value in asignacion_in.dict(exclude_unset=True).items():
            setattr(asignacion, field, value)
        db_session.commit()
        db_session.refresh(asignacion)
    return asignacion


def delete(db_session: Session, id: int) -> Optional[Asignacion]:
    asignacion = get_by_id(db_session, id)
    if asignacion:
        db_session.delete(asignacion)
        db_session.commit()
    return None
