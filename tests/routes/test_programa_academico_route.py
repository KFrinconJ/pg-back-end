from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from faker import Faker
from faker.providers import DynamicProvider
from src.config import settings

uri_endopoint = f"{settings.API_V1_STR}/programa-academico"


fake = Faker()


nombre_programa_academico_provider = DynamicProvider(
    provider_name="nombre_programa_academico",
    elements=[
        "Ingeniería Civil",
        "Ingeniería Industrial",
        "Ingeniería de Sistemas",
        "Administración de Empresas",
        "Economía",
        "Derecho",
        "Psicología",
        "Medicina",
        "Odontología",
        "Enfermería",
        "Comunicación Social",
        "Ciencias Políticas",
        "Contaduría Pública",
        "Arquitectura",
        "Diseño Gráfico",
    ],
)


fake.add_provider(nombre_programa_academico_provider)


def test_create_programa_academico(client: TestClient, db: Session) -> None:
    codigo_snies = fake.pyint(min_value=1, max_value=10000)
    nombre = fake.nombre_programa_academico()
    director = "kevinrincon8@gmail.com"

    data = {
        "codigo_snies": codigo_snies,
        "nombre": nombre,
        "director": director,
    }

    r = client.post(uri_endopoint, json=data)
    assert 200 <= r.status_code < 300


def test_get_all_programas_academicos(client: TestClient, db: Session) -> None:
    r = client.get(uri_endopoint)
    assert 200 <= r.status_code < 300


def test_get_programa_academico(client: TestClient, db: Session) -> None:
    codigo_snies = 5984
    r = client.get(f"{uri_endopoint}/snies/{codigo_snies}")
    assert 200 <= r.status_code < 300


def test_update_programa_academico(client: TestClient, db: Session) -> None:
    codigo_snies = 5984
    nombre = fake.nombre_programa_academico()
    director = "kevinrincon8@gmail.com"

    data = {
        "codigo_snies": codigo_snies,
        "nombre": nombre,
        "director": director,
    }

    r = client.put(f"{uri_endopoint}/snies/{codigo_snies}", json=data)
    assert 200 <= r.status_code < 300


def test_delete_programa_academico(client: TestClient, db: Session) -> None:
    codigo_snies = 2
    r = client.delete(f"{uri_endopoint}/snies/{codigo_snies}")
    assert 200 <= r.status_code < 300 or 204
