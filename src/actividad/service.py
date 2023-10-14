from typing import Optional, List
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status

from .models import Actividad
from .schemas import (
    ActividadCreate,
    ActividadUpdate,
)


def get_by_id(*, db_session, id: int) -> Optional[Actividad]:
    """Obtiene la actividad por id."""
    return db_session.query(Actividad).filter(Actividad.id == id).first()


def get_all(
    *, db_session, skip: int = 0, limit: int = 100
) -> List[Optional[Actividad]]:
    """Obtine todas las actividades"""
    return db_session.query(Actividad).offset(skip).limit(limit).all()


def create(*, db_session, actividad_in: ActividadCreate) -> Actividad:
    """Crea un nuevo actividad"""
    nombre_actividad = actividad_in.nombre.upper()

    actividad = Actividad(
        **actividad_in.dict(exclude={"nombre"}),
        nombre=nombre_actividad,
    )
    db_session.add(actividad)
    db_session.commit()
    db_session.refresh(actividad)
    return actividad


def update(
    *, db_session, actividad_id: Actividad, actividad_in: ActividadUpdate
) -> Actividad:
    actividad = get_by_id(db_session=db_session, id=actividad_id)
    if not actividad:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe la actividad con el id {id}"}],
        )

    actividad_data = actividad.__dict__
    update_data = {
        **actividad_in.dict(exclude={"nombre"}),
        "nombre": actividad_in.nombre.upper(),
    }
    for field in actividad_data:
        if field in update_data:
            setattr(actividad, field, update_data[field])

    db_session.commit()  # Guarda los cambios en la base de datos
    db_session.refresh(actividad)  # Refresca la instancia de la actividad

    return actividad


def delete(*, db_session, id: int):
    actividad = get_by_id(db_session=db_session, id=id)
    actividad.terms = []
    db_session.delete(actividad)
    db_session.commit()
