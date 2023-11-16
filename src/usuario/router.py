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
    get_by_email,
    update,
)

from src.auth.dependencies import PermissionsValidator
from fastapi import Depends


router = APIRouter()

error_object_plural = "usuarios"
error_object_singular = "un usuario"


@router.get(
    "/{email}",
    dependencies=[Depends(PermissionsValidator(["read:usuario"]))],
    response_model=UsuarioRead,
)
def get_usuario_by_correo_db(db_session: DbSession, email: str):
    usuario = get_by_email(db_session=db_session, email=email)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el email {email}"}],
        )
    return UsuarioRead(**usuario.__dict__)


@router.put(
    "/{email}",
    dependencies=[Depends(PermissionsValidator(["update:usuario"]))],
)
def update_usaurio_by_correo(
    db_session: DbSession, email: str, usuario_in: UsuarioUpdate
):
    usuario_correo = get_usuario_by_correo_db(db_session=db_session, email=email)

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


@router.get(
    "/auth0/users",
    dependencies=[Depends(PermissionsValidator(["read:usuarios"]))],
)
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


@router.get(
    "/auth0/users/{id}",
    dependencies=[Depends(PermissionsValidator(["read:usuario"]))],
)
def get_user(id: str):
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


@router.put(
    "/auth0/users/{id}",
    dependencies=[Depends(PermissionsValidator(["update:usuario"]))],
)
def update_user(id: str, user_update: dict):
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
        res = requests.patch(f"{base_url}/api/v2/users/{id}", headers=headers,json=user_update)
        return res.json()
    except HTTPError as e:
        return {"error": f"HTTPError: {str(e.code)} {str(e.reason)}"}
    except URLRequired as e:
        return {"error": f"URLRequired: {str(e.reason)}"}
    except RequestException as e:
        return {"error": f"RequestException: {e}"}
    except Exception as e:
        return {"error": f"Generic Exception: {e}"}
