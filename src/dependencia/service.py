from typing import Optional, List
from .models import Dependencia
from .schemas import DependenciaCreate, DependenciaUpdate
from src.usuario.service import get_by_cedula
from src.usuario.models import Usuario


def get_by_id(*, db_session, id: int) -> Optional[Dependencia]:
    """Obtiene la dependencia por id."""
    return db_session.query(Dependencia).filter(Dependencia.id == id).first()


def get_by_name(*, db_session, nombre: str) -> Optional[Dependencia]:
    """Obtiene la dependencia usando el nombre."""
    return db_session.query(Dependencia).filter(Dependencia.nombre == nombre).first()


def get_all(
    *, db_session, skip: int = 0, limit: int = 100
) -> List[Optional[Dependencia]]:
    """Obtine todas las dependencias"""
    return db_session.query(Dependencia).offset(skip).limit(limit).all()


def create(*, db_session, dependencia_in: DependenciaCreate) -> Dependencia:
    """Crea una nueva dependencia"""

    encargado = get_by_cedula(db_session=db_session, cedula=dependencia_in.encargado)

    dependencia = Dependencia(
        nombre=dependencia_in.nombre.upper(), encargado=encargado.cedula
    )
    db_session.add(dependencia)
    db_session.commit()
    db_session.refresh(dependencia)
    return dependencia


def update(
    *, db_session, dependencia: Dependencia, dependencia_in: DependenciaUpdate
) -> Dependencia:
    encargado = get_by_cedula(db_session=db_session, cedula=dependencia_in.encargado)
    dependencia_data = dependencia.__dict__
    update_data = {
        "nombre": dependencia_in.nombre.upper(),
        "encargado": encargado.cedula,
    }

    for field in dependencia_data:
        if field in update_data:
            setattr(dependencia, field, update_data[field])

    db_session.commit()
    db_session.refresh(dependencia)

    return dependencia


def delete(*, db_session, id: int):
    dependencia = db_session.query(Dependencia).filter(Dependencia.id == id).first()
    dependencia.terms = []
    db_session.delete(dependencia)
    db_session.commit()
