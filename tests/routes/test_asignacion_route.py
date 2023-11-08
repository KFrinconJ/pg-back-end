from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from faker import Faker
from src.config import settings

uri_endopoint = f"{settings.API_V1_STR}/asignacion"

fake = Faker()


def test_create_asignacion(client: TestClient, db: Session) -> None:
    horas_disponibles = 7  #
    periodo_id = 2  # Reemplaza con un período académico válido en tu base de datos
    profesor_id = (
        "kevinrincon8@gmail.com"  # Reemplaza con un profesor válido en tu base de datos
    )

    data = {
        "horas_disponibles": horas_disponibles,
        "periodo_academico": periodo_id,
        "docente": profesor_id,
    }

    r = client.post(uri_endopoint, json=data)
    assert 200 <= r.status_code < 300


def test_get_all_asignacion(client: TestClient, db: Session) -> None:
    r = client.get(uri_endopoint)
    assert 200 <= r.status_code < 300


def test_get_asignacion(client: TestClient, db: Session) -> None:
    asignacion_id = 3  # Reemplaza con un ID válido de asignación en tu base de datos
    r = client.get(f"{uri_endopoint}/{asignacion_id}")
    assert 200 <= r.status_code < 300


def test_update_asignacion(client: TestClient, db: Session) -> None:
    asignacion_id = 2  # Reemplaza con un ID válido de asignación en tu base de datos
    horas_disponibles = 2  # Reemplaza con un curso válido en tu base de datos
    periodo_id = 2  # Reemplaza con un período académico válido en tu base de datos
    profesor_id = (
        "kevinrincon8@gmail.com"  # Reemplaza con un profesor válido en tu base de datos
    )

    data = {
        "horas_disponibles": horas_disponibles,
        "periodo_academico": periodo_id,
        "docente": profesor_id,
    }

    r = client.put(f"{uri_endopoint}/{asignacion_id}", json=data)
    assert 200 <= r.status_code < 300


def test_delete_asignacion(client: TestClient, db: Session) -> None:
    asignacion_id = 1  # Reemplaza con un ID válido de asignación en tu base de datos
    r = client.delete(f"{uri_endopoint}/{asignacion_id}")
    assert 200 <= r.status_code < 300 or 204
