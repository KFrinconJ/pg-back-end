from fastapi import Depends
from src import config
from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from starlette.requests import Request


# !PRODUCCION = Inicia la base de datos
# engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

# !DESARROLLO = Inicia la base de datos para desarrollo
engine = create_engine(config.SQLALCHEMY_DEVELOPER_DATABASE_URI)
# Para las sesiones de cada peticion
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db(request: Request):
    return request.state.db


DbSession = Annotated[Session, Depends(get_db)]
