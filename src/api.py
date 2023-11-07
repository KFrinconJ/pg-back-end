from starlette.responses import JSONResponse

from fastapi import APIRouter

from src.programa_academico.router import router as programa_academico_router
from src.funcion_sustantiva.router import router as funcion_sustantiva_router
from src.usuario.router import router as usuario_router
from src.actividad.router import router as actividad_router
from src.dependencia.router import router as dependencia_router

from src.auth.dependencies import PermissionsValidator, validate_token
from fastapi import Depends


api_router = APIRouter(
    default_response_class=JSONResponse,
)


# Ruta de programa academico
api_router.include_router(
    programa_academico_router,
    prefix="/programa-academico",
    tags=["Programas Academicos"],
)

# Ruta de Funcion Sustantiva
api_router.include_router(
    funcion_sustantiva_router,
    prefix="/funcion-sustantiva",
    tags=["Funciones Sustantivas"],
)

# Proteger autenticacion
# @app.get("/api/messages/protected", dependencies=[Depends(validate_token)])
# def protected():
#     return {"text": "This is a protected message."}


api_router.include_router(
    usuario_router,
    prefix="/usuario",
    tags=["Usuarios"],
    dependencies=[Depends(PermissionsValidator(["read:usuarios"]))],
)


api_router.include_router(
    actividad_router,
    prefix="/actividad",
    tags=["Actividades"],
)


api_router.include_router(
    dependencia_router,
    prefix="/dependencia",
    tags=["Dependencias"],
)
