from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from faker import Faker
from faker.providers import DynamicProvider
from src.config import settings

uri_endopoint = f"{settings.API_V1_STR}/funcion-sustantiva"


fake = Faker()


funciones_sustantiva_provider = DynamicProvider(
    provider_name="funciones_sustantivas",
    elements=[
        "Docencia",
        "Investigación",
        "Extensión",
        "Administración y Gestión",
        "Salud",
        "Seguridad",
        "Judicial",
        "Gobierno y Política",
        "Cultura",
        "Deporte",
    ],
)

fake.add_provider(funciones_sustantiva_provider)


def test_create_actividad(client: TestClient, db: Session) -> None:
    nombre = fake.funciones_sustantivas()
    cantidad_horas = fake.pyint(min_value=1, max_value=4)
    descripcion = fake.paragraph(nb_sentences=5)
    actividad = 3
    dependencia = 1
    data = {
        "nombre": nombre,
        "cantidad_horas": cantidad_horas,
        "descripcion": descripcion,
        "actividad": actividad,
        "dependencia": dependencia,
    }
    r = client.post(uri_endopoint, json=data)
    assert 200 <= r.status_code < 300


def test_get_all_actividad(client: TestClient, db: Session) -> None:
    r = client.get(uri_endopoint)
    assert 200 <= r.status_code < 300


def test_get_actividad(client: TestClient, db: Session) -> None:
    id = 16
    r = client.get(f"{uri_endopoint}/{id}")
    assert 200 <= r.status_code < 300


def test_update_actividad(client: TestClient, db: Session) -> None:
    id = 16
    nombre = fake.funciones_sustantivas()
    cantidad_horas = fake.pyint(min_value=1, max_value=4)
    descripcion = fake.paragraph(nb_sentences=5)
    actividad = 3
    dependencia = 1
    data = {
        "nombre": nombre,
        "cantidad_horas": cantidad_horas,
        "descripcion": descripcion,
        "actividad": actividad,
        "dependencia": dependencia,
    }

    r = client.put(f"{uri_endopoint}/{id}", json=data)
    assert 200 <= r.status_code < 300


def test_delete_actividad(client: TestClient, db: Session) -> None:
    id = 17
    r = client.delete(f"{uri_endopoint}/{id}")
    assert 200 <= r.status_code < 300 or 204
