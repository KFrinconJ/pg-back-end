from starlette.responses import JSONResponse

from fastapi import APIRouter

from src.programa_academico.router import router as programa_academico_router
from src.funcion_sustantiva.router import router as funcion_sustantiva_router
from src.usuario.router import router as usuario_router
from src.actividad.router import router as actividad_router
from src.dependencia.router import router as dependencia_router
from src.periodo_academico.router import router as periodo_academico_router
from src.grupo.router import router as grupo_router
from src.curso.router import router as curso_router
from src.asignacion.router import router as asignacion_router

from src.auth.dependencies import PermissionsValidator
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

# Ruta usuarios
api_router.include_router(
    usuario_router,
    prefix="/usuario",
    tags=["Usuarios"],
)

# Ruta actividades
api_router.include_router(
    actividad_router,
    prefix="/actividad",
    tags=["Actividades"],
)

# Ruta periodo academico
api_router.include_router(
    periodo_academico_router,
    prefix="/periodo-academico",
    tags=["Periodos Academicos"],
)

# Ruta grupos
api_router.include_router(
    grupo_router,
    prefix="/grupo",
    tags=["Grupos"],
)

api_router.include_router(
    curso_router,
    prefix="/curso",
    tags=["Cursos"],
)
# Ruta dependencias
api_router.include_router(
    dependencia_router,
    prefix="/dependencia",
    tags=["Dependencias"],
)
# Ruta Asignaciones
api_router.include_router(
    asignacion_router,
    prefix="/asignacion",
    tags=["Asignaciones"],
)
