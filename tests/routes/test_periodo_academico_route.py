from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from faker import Faker
from faker.providers import DynamicProvider
from src.config import settings
from datetime import date

uri_endopoint = f"{settings.API_V1_STR}/periodo-academico"

fake = Faker()

# Proveedor de nombres de períodos académicos ficticios
periodos_academicos_provider = DynamicProvider(
    provider_name="periodos_academicos",
    elements=[
        "Semestre de Primavera 2023",
        "Trimestre de Otoño 2023",
        "Cuatrimestre de Verano 2023",
        "Bimestre de Invierno 2023",
        "Semestre de Primavera 2024",
        "Trimestre de Otoño 2024",
        "Cuatrimestre de Verano 2024",
        "Bimestre de Invierno 2024",
    ],
)

fake.add_provider(periodos_academicos_provider)


def test_get_all_periodo_academico(client: TestClient, db: Session) -> None:
    r = client.get(uri_endopoint)
    assert 200 <= r.status_code < 300


def test_get_periodo_academico(client: TestClient, db: Session) -> None:
    id = 2
    r = client.get(f"{uri_endopoint}/{id}")
    assert 200 <= r.status_code < 300


def test_delete_periodo_academico(client: TestClient, db: Session) -> None:
    id = 1
    r = client.delete(f"{uri_endopoint}/{id}")
    assert 200 <= r.status_code < 300 or 204


def test_create_periodo_academico(client: TestClient, db: Session) -> None:
    nombre = fake.periodos_academicos()
    inicio = fake.date_between(start_date="-1y", end_date="today")
    fin = fake.date_between_dates(date_start=inicio, date_end="+365d")
    data = {
        "nombre": nombre,
        "fecha_inicio": inicio.isoformat(),
        "fecha_fin": fin.isoformat(),
    }
    r = client.post(uri_endopoint, json=data)
    assert 200 <= r.status_code < 300


def test_update_periodo_academico(client: TestClient, db: Session) -> None:
    id = 2
    nombre = fake.periodos_academicos()
    inicio = fake.date_between_dates(
        date_start=date(2021, 12, 27), date_end=date(2022, 4, 15)
    )
    fin = fake.date_between_dates(
        date_start=date(2021, 12, 27), date_end=date(2022, 4, 15)
    )
    data = {
        "nombre": nombre,
        "fecha_inicio": inicio.isoformat(),
        "fecha_fin": fin.isoformat(),
    }
    r = client.put(f"{uri_endopoint}/{id}", json=data)
    assert 200 <= r.status_code < 300
