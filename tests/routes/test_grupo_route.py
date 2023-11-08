from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from faker import Faker
from faker.providers import DynamicProvider
from src.config import settings

uri_endopoint = f"{settings.API_V1_STR}/grupo"


fake = Faker()


grupo_nombres_provider = DynamicProvider(
    provider_name="grupo_nombres",
    elements=["8L", "10A", "6L", "15A", "7L", "12A", "9L", "11A", "5L", "13A"],
)

fake.add_provider(grupo_nombres_provider)


def test_create_grupo(client: TestClient, db: Session) -> None:
    nombre = fake.grupo_nombres()
    data = {"nombre": nombre}
    r = client.post(uri_endopoint, json=data)
    assert 200 <= r.status_code < 300


def test_get_all_grupo(client: TestClient, db: Session) -> None:
    r = client.get(uri_endopoint)
    assert 200 <= r.status_code < 300


def test_get_grupo(client: TestClient, db: Session) -> None:
    id = 2
    r = client.get(f"{uri_endopoint}/{id}")
    assert 200 <= r.status_code < 300


def test_update_grupo(client: TestClient, db: Session) -> None:
    id = 2
    nombre = fake.grupo_nombres()
    data = {"nombre": nombre}
    r = client.put(f"{uri_endopoint}/{id}", json=data)
    assert 200 <= r.status_code < 300


def test_delete_grupo(client: TestClient, db: Session) -> None:
    id = 3
    r = client.delete(f"{uri_endopoint}/{id}")
    assert 200 <= r.status_code < 300 or 204
