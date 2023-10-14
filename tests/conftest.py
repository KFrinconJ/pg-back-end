from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src import config
from src.database.core import SessionLocal
from src.main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    # Inicializar la base de datos
    db = SessionLocal()
    yield db  # Proporciona la sesión de base de datos
    # Limpiar la base de datos al final de las pruebas
    db.close()


@pytest.fixture(scope="function", autouse=True)
def db_session(db: Session) -> Generator:
    # Comenzar una transacción para cada prueba
    with db.begin():
        yield db


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
