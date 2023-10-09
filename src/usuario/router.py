from fastapi import APIRouter, HTTPException, status
from src.database.core import DbSession
from .schemas import (
    UsuarioCreate,
    UsuarioRead,
    UsuarioUpdate,
)
from .service import (
    create,
    get_all,
    get_by_id,
    get_by_cedula,
    get_by_email,
    update,
    delete_by_cedula,
    delete_by_correo,
)


router = APIRouter()

error_object_plural = "usuarios"
error_object_singular = "un usuario"


@router.get("")
def read_usuarios(db_session: DbSession, skip: int = 0, limit: int = 100):
    usuarios = get_all(db_session=db_session, skip=skip, limit=limit)
    if not usuarios:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No hay {error_object_plural} registrados"}],
        )
    return usuarios


@router.get("/{usuario_id}", response_model=UsuarioRead)
def get_usuario_by_id(db_session: DbSession, usuario_id: int):
    usuario = get_by_id(db_session=db_session, usuario_id=usuario_id)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {"msg": f"No existe {error_object_singular} con el id {usuario_id}"}
            ],
        )
    return UsuarioRead(**usuario.__dict__)


@router.get("/cedula/{cedula}", response_model=UsuarioRead)
def get_usuario_by_cedula(db_session: DbSession, cedula: int):
    usuario = get_by_cedula(db_session=db_session, cedula=cedula)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {"msg": f"No existe {error_object_singular} con la cédula {cedula}"}
            ],
        )
    return UsuarioRead(**usuario.__dict__)


@router.get("/correo/{correo}", response_model=UsuarioRead)
def get_usuario_by_correo(db_session: DbSession, correo: str):
    usuario = get_by_email(db_session=db_session, correo=correo)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {"msg": f"No existe {error_object_singular} con el correo {correo}"}
            ],
        )
    return UsuarioRead(**usuario.__dict__)


@router.post("", response_model=UsuarioRead)
def create_usuario(usuario_in: UsuarioCreate, db_session: DbSession):
    usuario_cedula = get_by_cedula(db_session=db_session, cedula=usuario_in.cedula)
    usuario_email = get_by_email(db_session=db_session, correo=usuario_in.correo)

    if usuario_cedula:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=[
                {
                    "msg": f"Ya existe {error_object_singular} con la cédula {usuario_in.cedula}"
                }
            ],
        )
    if usuario_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=[
                {
                    "msg": f"Ya existe {error_object_singular} con el correo {usuario_in.correo}"
                }
            ],
        )
    programa_academico = create(db_session=db_session, usuario_in=usuario_in)
    return UsuarioRead(**programa_academico.__dict__)


@router.put("/cedula/{cedula}")
def update_usaurio_by_cedula(
    db_session: DbSession, cedula: int, usuario_in: UsuarioUpdate
):
    usuario_cedula = get_by_cedula(db_session=db_session, cedula=usuario_in.cedula)

    if not usuario_cedula:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {"msg": f"No existe {error_object_singular} con la cédula {cedula}"}
            ],
        )

    usuario_update = update(
        db_session=db_session,
        usuario=usuario_cedula,
        usuario_in=usuario_in,
    )

    return UsuarioRead(**usuario_update.__dict__)


@router.put("/correo/{correo}")
def update_usaurio_by_correo(
    db_session: DbSession, correo: int, usuario_in: UsuarioUpdate
):
    usuario_correo = get_usuario_by_correo(
        db_session=db_session, correo=usuario_in.correo
    )

    if not usuario_correo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el {correo}"}],
        )

    usuario_update = update(
        db_session=db_session,
        usuario=usuario_correo,
        usuario_in=usuario_in,
    )

    return UsuarioRead(**usuario_update.__dict__)


@router.delete("/correo/{correo}")
def delete_usuario_by_correo(db_session: DbSession, correo: str):
    usuario_correo = get_by_email(db_session=db_session, correo=correo)
    if not usuario_correo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {"msg": f"No existe {error_object_singular} con el correo {correo}"}
            ],
        )
    delete_by_correo(db_session=db_session, correo=correo)
    return HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail=[{"msg": f"Se elimino el usuario con el {correo}"}],
    )


@router.delete("/cedula/{cedula}")
def delete_usuario_by_correo(db_session: DbSession, cedula: int):
    usuario_correo = get_by_cedula(db_session=db_session, cedula=cedula)
    if not usuario_correo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {"msg": f"No existe {error_object_singular} con la cedula {cedula}"}
            ],
        )
    delete_by_correo(db_session=db_session, cedula=cedula)
    return HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail=[{"msg": f"Se elimino el usuario con la {cedula}"}],
    )
