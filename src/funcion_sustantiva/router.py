from fastapi import APIRouter, HTTPException, status
from typing import Optional
from src.database.core import DbSession
from .shcemas import (
    FuncionSustantivaCreate,
    FuncionSustantivaRead,
    FuncionSustantivaUpdate,
)


error_object_plural = "Funciones Sustantivas"
error_object_singular = "Una Funcion Sustantiva"


from .service import (
    create,
    get_all,
    get_by_name,
    update,
    delete,
    get_by_id,
    get_by_id_numeric,
)
from src.dependencia.service import get_by_id as get_by_id_dependencia
from src.actividad.service import get_by_id as get_by_id_actividad


router = APIRouter()


@router.get("")
def get_funciones_sustantivas(db_session: DbSession, skip: int = 0, limit: int = 100):
    funciones_sustantivas = get_all(db_session=db_session, skip=skip, limit=limit)
    if not funciones_sustantivas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No hay {error_object_plural}"}],
        )
    return funciones_sustantivas


# Ruta para obtener los datos con la informacion completa
@router.get("/{id}", response_model=FuncionSustantivaRead)
def get_funcion_sustantiva_by_id(db_session: DbSession, id: int):
    funcion_sustantiva = get_by_id(db_session=db_session, id=id)
    if not funcion_sustantiva:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )
    return FuncionSustantivaRead(**funcion_sustantiva)


@router.get("/nombre/{nombre}", response_model=FuncionSustantivaRead)
def get_funcion_sustantiva_by_name(db_session: DbSession, nombre: str):
    funcion_sustantiva = get_by_name(db_session=db_session, nombre=nombre)
    if not funcion_sustantiva:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {"msg": f"No existe {error_object_singular} con el nombre {nombre}"}
            ],
        )
    return FuncionSustantivaRead(**funcion_sustantiva.__dict__)


@router.post("", response_model=Optional[FuncionSustantivaRead])
def create_funcion_sustantiva(
    funcion_sustantiva_in: FuncionSustantivaCreate, db_session: DbSession
):
    # funcion_sustantiva_nombre = get_by_name(
    #     db_session=db_session, nombre=funcion_sustantiva_in.nombre
    # )

    funcion_sustantiva_dependencia = get_by_id_dependencia(
        db_session=db_session, id=funcion_sustantiva_in.dependencia
    )

    funcion_sustantiva_actividad = get_by_id_actividad(
        db_session=db_session, id=funcion_sustantiva_in.actividad
    )

    if not funcion_sustantiva_actividad:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {
                    "msg": f"No existe una actividad con el id {funcion_sustantiva_in.actividad}"
                }
            ],
        )

    if not funcion_sustantiva_dependencia:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {
                    "msg": f"No existe una dependencia con el id {funcion_sustantiva_in.dependencia}"
                }
            ],
        )

    # if funcion_sustantiva_nombre:
    #     raise HTTPException(
    #         status_code=status.HTTP_409_CONFLICT,
    #         detail=[
    #             {
    #                 "msg": f"Ya existe {error_object_singular} con el nombre {funcion_sustantiva_in.nombre}"
    #             }
    #         ],
    #     )

    funcion_sustantiva = create(
        db_session=db_session, funcion_sustantiva_in=funcion_sustantiva_in
    )

    return FuncionSustantivaRead(**funcion_sustantiva.__dict__)


@router.put("/{id}")
def update_funcion_sustantiva(
    db_session: DbSession, id: int, funcion_sustantiva_in: FuncionSustantivaUpdate
):
    funcion_sustantiva = get_by_id_numeric(db_session=db_session, id=id)
    if not funcion_sustantiva:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} el id {id}"}],
        )

    funcion_sustantiva_actividad = get_by_id_actividad(
        db_session=db_session, id=funcion_sustantiva_in.actividad
    )

    if not funcion_sustantiva_actividad:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {
                    "msg": f"No existe una actividad con el id {funcion_sustantiva_in.actividad}"
                }
            ],
        )

    # funcion_sustantiva_nombre = get_by_name(
    #     db_session=db_session, nombre=funcion_sustantiva_in.nombre
    # )

    funcion_sustantiva_dependencia = get_by_id_dependencia(
        db_session=db_session, id=funcion_sustantiva_in.dependencia
    )

    if not funcion_sustantiva_dependencia:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {
                    "msg": f"No existe una dependencia con el id {funcion_sustantiva_in.dependencia}"
                }
            ],
        )

    # if funcion_sustantiva_nombre:
    #     raise HTTPException(
    #         status_code=status.HTTP_409_CONFLICT,
    #         detail=[
    #             {
    #                 "msg": f"Ya existe {error_object_singular} con el nombre {funcion_sustantiva_in.nombre}"
    #             }
    #         ],
    #     )

    funcion_sustantiva_update = update(
        db_session=db_session,
        funcion_sustantiva=funcion_sustantiva,
        funcion_sustantiva_in=funcion_sustantiva_in,
    )

    return FuncionSustantivaRead(**funcion_sustantiva_update.__dict__)


@router.delete("/{id}")
def delete_funcion_sustantiva(db_session: DbSession, id: int):
    funcion_sustantiva = get_by_id(db_session=db_session, id=id)
    if not funcion_sustantiva:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": f"No existe {error_object_singular} con el id {id}"}],
        )
    delete(db_session=db_session, id=id)
    return HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail=[{"msg": f"Se elimino {error_object_singular} con el id {id}"}],
    )
