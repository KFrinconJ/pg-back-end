from fastapi import APIRouter, HTTPException, status
from requests.exceptions import RequestException, HTTPError, URLRequired
import requests
from src import config

from src.database.core import DbSession
from .schemas import (
    UsuarioRead,
    UsuarioUpdate,
)
from .service import (
    get_all,
    get_by_cedula,
    get_by_email,
    update,
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


@router.get("/{email}", response_model=UsuarioRead)
def get_usuario_by_correo(db_session: DbSession, email: str):
    usuario = get_by_email(db_session=db_session, email=email)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el email {email}"}],
        )
    return UsuarioRead(**usuario.__dict__)


@router.put("/{email}")
def update_usaurio_by_correo(
    db_session: DbSession, email: str, usuario_in: UsuarioUpdate
):
    usuario_correo = get_usuario_by_correo(db_session=db_session, email=email)

    if not usuario_correo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el email {email}"}],
        )

    usuario_update = update(
        db_session=db_session,
        email=usuario_correo.email,
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


@router.delete("/{cedula}")
def delete_usuario_by_correo(db_session: DbSession, cedula: int):
    usuario_correo = get_by_cedula(db_session=db_session, cedula=cedula)
    if not usuario_correo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {"msg": f"No existe {error_object_singular} con la cedula {cedula}"}
            ],
        )


@router.get("/auth0/users")
def get_users():
    # Get an Access Token from Auth0
    base_url = f"https://{config.DOMAIN}"
    payload = {
        "grant_type": "client_credentials",
        "client_id": config.CLIENT_ID,
        "client_secret": config.CLIENT_SECRET,
        "audience": config.MANAGEMENT_AUDIENCE,
    }
    response = requests.post(f"{base_url}/oauth/token", data=payload)
    oauth = response.json()

    access_token = oauth.get("access_token")

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    # Get all Applications using the token
    try:
        res = requests.get(f"{base_url}/api/v2/users", headers=headers)
        return res.json()
    except HTTPError as e:
        return {"error": f"HTTPError: {str(e.code)} {str(e.reason)}"}
    except URLRequired as e:
        return {"error": f"URLRequired: {str(e.reason)}"}
    except RequestException as e:
        return {"error": f"RequestException: {e}"}
    except Exception as e:
        return {"error": f"Generic Exception: {e}"}


@router.get("/auth0/users/{id}")
def get_access_token(id: str):
    # Get an Access Token from Auth0
    base_url = f"https://{config.DOMAIN}"
    payload = {
        "grant_type": "client_credentials",
        "client_id": config.CLIENT_ID,
        "client_secret": config.CLIENT_SECRET,
        "audience": config.MANAGEMENT_AUDIENCE,
    }
    response = requests.post(f"{base_url}/oauth/token", data=payload)
    oauth = response.json()

    access_token = oauth.get("access_token")

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    # Get all Applications using the token
    try:
        res = requests.get(f"{base_url}/api/v2/users/{id}", headers=headers)
        return res.json()
    except HTTPError as e:
        return {"error": f"HTTPError: {str(e.code)} {str(e.reason)}"}
    except URLRequired as e:
        return {"error": f"URLRequired: {str(e.reason)}"}
    except RequestException as e:
        return {"error": f"RequestException: {e}"}
    except Exception as e:
        return {"error": f"Generic Exception: {e}"}
