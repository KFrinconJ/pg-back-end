from typing import Optional, List


from src.dependencia import service as dependencia_service
from src.dependencia.models import Dependencia
from src.actividad import service as actividad_service
from src.actividad.models import Actividad


from .models import FuncionSustantiva

from .shcemas import FuncionSustantivaCreate, FuncionSustantivaUpdate


def get_by_id_numeric(*, db_session, id: int) -> Optional[FuncionSustantiva]:
    """Obtiene la funcion sustantiva por id."""
    return (
        db_session.query(FuncionSustantiva).filter(FuncionSustantiva.id == id).first()
    )


def get_by_id(*, db_session, id: int) -> Optional[FuncionSustantiva]:
    """Obtiene la funcion sustantiva por id."""
    return (
        db_session.query(
            FuncionSustantiva.id,
            FuncionSustantiva.nombre,
            FuncionSustantiva.descripcion,
            FuncionSustantiva.cantidad_horas,
            Dependencia.nombre.label("dependencia"),
            Actividad.nombre.label("actividad"),
        )
        .filter(FuncionSustantiva.id == id)
        .join(Dependencia, FuncionSustantiva.dependencia == Dependencia.id)
        .join(Actividad, FuncionSustantiva.actividad == Actividad.id)
        .first()
    )


# query(FS, TipoFS.nombre_tipo_fs).join(TipoFS, FS.id_tipo_fs == TipoFS.id_tipo_fs).all()
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
    return (
        db_session.query(
            FuncionSustantiva.id,
            FuncionSustantiva.nombre,
            FuncionSustantiva.descripcion,
            FuncionSustantiva.cantidad_horas,
            Dependencia.nombre.label("dependencia"),
            Actividad.nombre.label("actividad"),
        )
        .join(Dependencia, FuncionSustantiva.dependencia == Dependencia.id)
        .join(Actividad, FuncionSustantiva.actividad == Actividad.id)
        .offset(skip)
        .limit(limit)
        .all()
    )


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
