from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from faker import Faker
from faker.providers import DynamicProvider
from src.config import settings

uri_endopoint = f"{settings.API_V1_STR}/curso"


fake = Faker()


cursos_nombre_provider = DynamicProvider(
    provider_name="cursos_nombre",
    elements=[
        "Introducción a la Programación",
        "Matemáticas Avanzadas",
        "Historia del Arte",
        "Economía Microeconómica",
        "Literatura Mundial",
        "Biología Celular",
        "Diseño Gráfico",
        "Ingeniería de Software",
        "Química Orgánica",
        "Psicología del Comportamiento Humano",
    ],
)


cursos_codigo_provider = DynamicProvider(
    provider_name="cursos_codigo",
    elements=[
        "4629",
        "2313",
        "7821O",
        "5948",
        "3152",
        "1076K",
        "8390",
        "6614",
        "1234L",
        "4098",
    ],
)

fake.add_provider(cursos_codigo_provider)
fake.add_provider(cursos_nombre_provider)


def test_create_curso(client: TestClient, db: Session) -> None:
    nombre = fake.cursos_nombre()
    codigo = fake.cursos_codigo()
    cantidad_horas = fake.pyint(min_value=1, max_value=4)
    data = {"nombre": nombre, "codigo": codigo, "cantidad_horas": cantidad_horas}
    r = client.post(uri_endopoint, json=data)
    assert 200 <= r.status_code < 300


def test_get_all_curso(client: TestClient, db: Session) -> None:
    r = client.get(uri_endopoint)
    assert 200 <= r.status_code < 300


def test_get_curso(client: TestClient, db: Session) -> None:
    id = 2
    r = client.get(f"{uri_endopoint}/{id}")
    assert 200 <= r.status_code < 300


def test_update_curso(client: TestClient, db: Session) -> None:
    id = 2
    nombre = fake.cursos_nombre()
    codigo = fake.cursos_codigo()
    cantidad_horas = fake.pyint(min_value=1, max_value=4)
    data = {"nombre": nombre, "codigo": codigo, "cantidad_horas": cantidad_horas}
    r = client.put(f"{uri_endopoint}/{id}", json=data)
    assert 200 <= r.status_code < 300


def test_delete_curso(client: TestClient, db: Session) -> None:
    id = 1
    r = client.delete(f"{uri_endopoint}/{id}")
    assert 200 <= r.status_code < 300 or 204
