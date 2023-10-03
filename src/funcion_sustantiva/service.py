from typing import Optional, List


from src.funcion_sustantiva_tipo import service as tipo_funcion_sustantiva_service
from .models import FuncionSustantiva

from .shcemas import FuncionSustantivaCreate, FuncionSustantivaUpdate


def get_by_id(*, db_session, id: int) -> Optional[FuncionSustantiva]:
    """Obtiene la funcion sustantiva por id."""
    return (
        db_session.query(FuncionSustantiva).filter(FuncionSustantiva.id == id).first()
    )


def get_by_name(*, db_session, nombre: str) -> Optional[FuncionSustantiva]:
    """Obtiene la funcion sustantiva por nombre"""
    return (
        db_session.query(FuncionSustantiva)
        .filter(FuncionSustantiva.nombre == nombre)
        .first()
    )


def get_all(
    *, db_session, skip: int = 0, limit: int = 100
) -> List[Optional[FuncionSustantiva]]:
    """Obtine todas las funciones sustantivas"""
    return db_session.query(FuncionSustantiva).offset(skip).limit(limit).all()


def create(
    *, db_session, funcion_sustantiva_in: FuncionSustantivaCreate
) -> FuncionSustantiva:
    """Crea una nueva funcion sustantiva"""

    tipo = tipo_funcion_sustantiva_service.get_by_id(
        db_session=db_session,
        id=funcion_sustantiva_in.tipo,
    )

    funcion_sustantiva = FuncionSustantiva(
        **funcion_sustantiva_in.dict(exclude={"tipo"}), tipo=tipo.id
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
    funcion_sustantiva_data = funcion_sustantiva.__dict__
    update_data = funcion_sustantiva_in.dict(skip_defaults=True, exclude={"tipo"})

    for field in funcion_sustantiva_data:
        if field in update_data:
            setattr(funcion_sustantiva, field, update_data[field])

    tipo = tipo_funcion_sustantiva_service.get_by_id(
        db_session=db_session,
        id=funcion_sustantiva_in.tipo,
    )
    funcion_sustantiva.tipo = tipo.id

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
