from starlette.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List

from fastapi import APIRouter

from src.programa_academico.router import router as programa_academico_router


class ErrorMessage(BaseModel):
    msg: str


class ErrorResponse(BaseModel):
    detail: Optional[List[ErrorMessage]]


# Para rutas sin autenticar
authenticated_api_router = APIRouter()


api_router = APIRouter(
    default_response_class=JSONResponse,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)


# Ruta de programa academico
api_router.include_router(
    programa_academico_router,
    prefix="/programa-academico",
    tags=["Programas Academicos"],
)
