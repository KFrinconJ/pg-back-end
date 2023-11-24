from typing import Optional, List


from src.dependencia import service as dependencia_service
from src.actividad import service as actividad_service
from sqlalchemy.orm import Session



from .models import FuncionSustantiva

from .schemas import FuncionSustantivaCreate, FuncionSustantivaUpdate


def get_by_id(db_session: Session, id: int) -> Optional[FuncionSustantiva]:
    return db_session.query(FuncionSustantiva).filter(FuncionSustantiva.id == id).first()


def get_all(db_session: Session, skip: int = 0, limit: int = 100) -> List[FuncionSustantiva]:
    return db_session.query(FuncionSustantiva).offset(skip).limit(limit).all()


def create(
    *, db_session, funcion_sustantiva_in: FuncionSustantivaCreate
) -> FuncionSustantiva:
    """Crea una nueva funcion sustantiva"""

    dependencia = dependencia_service.get_by_id(
        db_session=db_session,
        id=funcion_sustantiva_in.dependencia,
    )

    actividad = actividad_service.get_by_id(
        db_session=db_session, id=funcion_sustantiva_in.actividad
    )

    nombre = funcion_sustantiva_in.nombre.upper()
    funcion_sustantiva = FuncionSustantiva(
        **funcion_sustantiva_in.dict(exclude={"dependencia", "actividad", "nombre"}),
        nombre=nombre,
        dependencia=dependencia.id,
        actividad=actividad.id
    )

    db_session.add(funcion_sustantiva)
    db_session.commit()
    db_session.refresh(funcion_sustantiva)
    return funcion_sustantiva


def update(
    *,
    db_session,
    funcion_sustantiva: FuncionSustantiva,
    funcion_sustantiva_in: FuncionSustantivaUpdate
) -> FuncionSustantiva:
    """Actualiza una funcion sustantiva ya creada"""
    print(funcion_sustantiva)
    funcion_sustantiva_data = funcion_sustantiva.__dict__

    dependencia = dependencia_service.get_by_id(
        db_session=db_session,
        id=funcion_sustantiva_in.dependencia,
    )

    actividad = actividad_service.get_by_id(
        db_session=db_session, id=funcion_sustantiva_in.actividad
    )

    nombre = funcion_sustantiva_in.nombre.upper()

    update_data = {
        "cantidad_horas": funcion_sustantiva_in.cantidad_horas,
        "descripcion": funcion_sustantiva_in.descripcion,
        "dependencia": dependencia.id,
        "actividad": actividad.id,
        "nombre": nombre,
    }

    for field in funcion_sustantiva_data:
        if field in update_data:
            setattr(funcion_sustantiva, field, update_data[field])

    db_session.commit()
    db_session.refresh(funcion_sustantiva)

    return funcion_sustantiva


def delete(*, db_session, id: int):
    funcion_sustantiva = (
        db_session.query(FuncionSustantiva).filter(FuncionSustantiva.id == id).first()
    )
    funcion_sustantiva.terms = []
    db_session.delete(funcion_sustantiva)
    db_session.commit()
