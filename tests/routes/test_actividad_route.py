from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from faker import Faker
from faker.providers import DynamicProvider
from src.config import settings

uri_endopoint = f"{settings.API_V1_STR}/actividad"


fake = Faker()


actividades_docente_provider = DynamicProvider(
    provider_name="actividades_docente",
    elements=[
        "Impartir clases",
        "Investigación",
        "Orientación académica",
        "Participación en comités y órganos de gobierno",
        "Desarrollo curricular",
        "Colaboración con la comunidad",
        "Participación en eventos académicos",
        "Mentoría a estudiantes",
        "Supervisión de trabajos de grado",
        "Formación continua",
        "Colaboración interinstitucional",
        "Evaluación de procesos educativos",
        "Innovación pedagógica",
        "Evaluación y retroalimentación",
        "Actividades extracurriculares",
    ],
)

fake.add_provider(actividades_docente_provider)


def test_create_actividad(client: TestClient, db: Session) -> None:
    nombre = fake.actividades_docente()
    cantidad_horas = fake.pyint(min_value=1, max_value=4)
    data = {"nombre": nombre, "cantidad_horas": cantidad_horas}
    r = client.post(uri_endopoint, json=data)
    assert 200 <= r.status_code < 300


def test_get_all_actividad(client: TestClient, db: Session) -> None:
    r = client.get(uri_endopoint)
    assert 200 <= r.status_code < 300


def test_get_actividad(client: TestClient, db: Session) -> None:
    id = 1
    r = client.get(f"{uri_endopoint}/{id}")
    assert 200 <= r.status_code < 300


def test_update_actividad(client: TestClient, db: Session) -> None:
    id = 1
    nombre = fake.actividades_docente()
    cantidad_horas = fake.pyint(min_value=1, max_value=4)
    data = {"nombre": nombre, "cantidad_horas": cantidad_horas}
    r = client.put(f"{uri_endopoint}/{id}", json=data)
    assert 200 <= r.status_code < 300


def test_delete_actividad(client: TestClient, db: Session) -> None:
    id = 2
    r = client.delete(f"{uri_endopoint}/{id}")
    assert 200 <= r.status_code < 300 or 204
