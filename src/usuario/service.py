from typing import Optional, List
from fastapi import HTTPException, status


from .models import Usuario
from .schemas import (
    UsuarioCreate,
    UsuarioUpdate,
)


def get_by_cedula(*, db_session, cedula: int) -> Optional[Usuario]:
    """Obtiene el usuario usando la cedula"""
    return db_session.query(Usuario).filter(Usuario.cedula == cedula).first()


def get_by_email(*, db_session, correo: str) -> Optional[Usuario]:
    """Obtiene el usuario usando el correo"""
    return db_session.query(Usuario).filter(Usuario.correo == correo).first()


def get_all(*, db_session, skip: int = 0, limit: int = 100) -> List[Optional[Usuario]]:
    """Obtine todos los usuarios"""
    return db_session.query(Usuario).offset(skip).limit(limit).all()


def create(*, db_session, usuario_in: UsuarioCreate) -> Usuario:
    """Crea un nuevo usuario"""
    nombre_usuario = usuario_in.nombre.upper()
    apellido_usuario = usuario_in.apellido.upper()
    correo_usuario = usuario_in.correo.lower()
    perfil_usuario = usuario_in.perfil.upper()
    rol_usuario = usuario_in.rol.upper()
    usuario = Usuario(
        **usuario_in.dict(exclude={"nombre", "apellido", "correo", "perfil", "rol"}),
        nombre=nombre_usuario,
        apellido=apellido_usuario,
        correo=correo_usuario,
        perfil=perfil_usuario,
        rol=rol_usuario,
    )
    db_session.add(usuario)
    db_session.commit()
    db_session.refresh(usuario)
    return usuario


def update(*, db_session, usuario: Usuario, usuario_in: UsuarioUpdate) -> Usuario:
    usuario_data = usuario.__dict__

    update_data = {
        "nombre": usuario_in.nombre.upper(),
        "apellido": usuario_in.apellido.upper(),
        "correo": usuario_in.correo.lower(),
        "perfil": usuario_in.perfil.upper(),
        "rol": usuario_in.rol.upper(),
    }

    for field in usuario_data:
        if field in update_data:
            setattr(usuario, field, update_data[field])

    db_session.commit()
    db_session.refresh(usuario)

    return usuario


def delete_by_cedula(*, db_session, cedula: int):
    usuario = get_by_cedula(db_session=db_session, cedula=cedula)
    usuario.terms = []
    db_session.delete(usuario)
    db_session.commit()


def delete_by_correo(*, db_session, correo: str):
    usuario = get_by_email(db_session=db_session, correo=correo)
    usuario.terms = []
    db_session.delete(usuario)
    db_session.commit()
