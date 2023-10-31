from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from faker import Faker
from faker.providers import DynamicProvider
from src.config import settings

uri_endopoint = f"{settings.API_V1_STR}/dependencia"


fake = Faker()


nombre_dependencia_provider = DynamicProvider(
    provider_name="nombre_dependencia",
    elements=[
        "Programa",
        "Investigaciones",
        "Proyección Social",
        "Internacionalización",
        "Bienestar Universitatio",
        "Educación Continua",
    ],
)


fake.add_provider(nombre_dependencia_provider)


def test_create_dependencia(client: TestClient, db: Session) -> None:
    encargado = 1098811091
    nombre = fake.nombre_dependencia()

    data = {
        "encargado": encargado,
        "nombre": nombre,
    }

    r = client.post(uri_endopoint, json=data)
    assert 200 <= r.status_code < 300


def test_get_all_dependencias(client: TestClient, db: Session) -> None:
    r = client.get(uri_endopoint)
    print(r)
    assert 200 <= r.status_code < 300


def test_get_dependencia(client: TestClient, db: Session) -> None:
    id = 1
    r = client.get(f"{uri_endopoint}/{id}")
    assert 200 <= r.status_code < 300


def test_update_dependencia(client: TestClient, db: Session) -> None:
    id = 1
    encargado = 1098811091
    nombre = fake.nombre_dependencia()

    data = {
        "encargado": encargado,
        "nombre": nombre,
    }

    r = client.put(f"{uri_endopoint}/{id}", json=data)
    assert 200 <= r.status_code < 300


def test_delete_dependencia(client: TestClient, db: Session) -> None:
    id = 9
    r = client.delete(f"{uri_endopoint}/{id}")
    assert 200 <= r.status_code < 300 or 204
