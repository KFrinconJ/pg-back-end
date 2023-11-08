from fastapi import FastAPI, Depends
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import sessionmaker, scoped_session
from .database.core import engine
from .config import settings
from .api import api_router
import uvicorn
from src import config


# ASGI para el framework
app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    try:
        # Crea una sesión de base de datos
        session = scoped_session(sessionmaker(bind=engine))
        request.state.db = session()
        # Llama al siguiente manipulador en la cadena
        response = await call_next(request)
    except Exception as e:
        raise e from None
    finally:
        # Cierra la sesión de la base de datos
        request.state.db.close()

    return response


@app.get("/")
def hello_world():
    return "Hola Mundo"


@app.get("/test-db-connection")
def test_db_connection():
    try:
        # Realiza una consulta de prueba en la base de datos
        result = engine.execute("SELECT 1")
        return {"message": "Conexión a la base de datos exitosa"}
    except Exception as e:
        return {"message": "Error al conectar a la base de datos", "error": str(e)}


# Obtener Roles de los usuarios

from requests.exceptions import RequestException, HTTPError, URLRequired
import requests
from src.auth.dependencies import validate_token


@app.get("/auth0/users/{id}", dependencies=[Depends(validate_token)])
def get_users(id: str):
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
        res = requests.get(f"{base_url}/api/v2/users/{id}/roles", headers=headers)
        return res.json()
    except HTTPError as e:
        return {"error": f"HTTPError: {str(e.code)} {str(e.reason)}"}
    except URLRequired as e:
        return {"error": f"URLRequired: {str(e.reason)}"}
    except RequestException as e:
        return {"error": f"RequestException: {e}"}
    except Exception as e:
        return {"error": f"Generic Exception: {e}"}


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# Añadimos todas la rutas
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=config.DATABASE_PORT,
        reload=config.RELOAD,
        server_header=False,
    )
