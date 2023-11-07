from typing import Optional, List
from fastapi import HTTPException, status


from .models import Usuario
from .schemas import UsuarioCreate, UsuarioUpdate, UsuarioRead


def get_by_cedula(*, db_session, cedula: int) -> Optional[Usuario]:
    """Obtiene el usuario usando la cedula"""
    return db_session.query(Usuario).filter(Usuario.cedula == cedula).first()


def get_by_email(*, db_session, email: str) -> Optional[Usuario]:
    """Obtiene el usuario usando el email"""
    return db_session.query(Usuario).filter(Usuario.email == email).first()


def get_all(*, db_session, skip: int = 0, limit: int = 100) -> List[Optional[Usuario]]:
    """Obtine todos los usuarios"""
    return db_session.query(Usuario).offset(skip).limit(limit).all()


def update(*, db_session, email: str, usuario_in: UsuarioUpdate) -> Usuario:
    usuario = get_by_email(db_session=db_session, email=email)

    update_data = {
        **usuario_in.dict(exclude={"nombre", "apellido", "programa"}),
        "nombre": usuario_in.nombre.upper(),
        "apellido": usuario_in.apellido.upper(),
        "programa": usuario_in.programa.upper(),
    }

    usuario_data = usuario.__dict__

    for field in usuario_data:
        if field in update_data:
            setattr(usuario, field, update_data[field])

    db_session.commit()  # Realizar la transacción para asegurarse de que la instancia esté en la sesión
    db_session.refresh(usuario)

    return usuario


