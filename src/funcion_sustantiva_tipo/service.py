from typing import Optional, List
from .models import TipoFuncionSustantiva


def get_by_id(*, db_session, id: int) -> Optional[TipoFuncionSustantiva]:
    """Obtiene el tipo de funcion sustantiva por id."""
    return (
        db_session.query(TipoFuncionSustantiva)
        .filter(TipoFuncionSustantiva.id == id)
        .first()
    )


def get_by_name(*, db_session, nombre: str) -> Optional[TipoFuncionSustantiva]:
    """Obtiene el tipo de funcion sustantiva por el nombre."""
    return (
        db_session.query(TipoFuncionSustantiva)
        .filter(TipoFuncionSustantiva.nombre == nombre)
        .first()
    )


def get_all(
    *, db_session, skip: int = 0, limit: int = 100
) -> List[Optional[TipoFuncionSustantiva]]:
    """Obtine todos tipos de funcion sustantiva"""
    return db_session.query(TipoFuncionSustantiva).offset(skip).limit(limit).all()
