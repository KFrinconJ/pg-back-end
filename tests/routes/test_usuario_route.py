from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from faker import Faker
from faker.providers import DynamicProvider
from src.config import settings

uri_endopoint = f"{settings.API_V1_STR}/usuario"


fake = Faker()


perfil_usuario_provider = DynamicProvider(
    provider_name="perfil_usuario",
    elements=[
        "Docente de Aula",
        "Docente Orientador",
        "Docente Tutor",
        "Docente de funciones de apoyo",
    ],
)


rol_usuario_provider = DynamicProvider(
    provider_name="rol_usuario",
    elements=["Administrador", "Docente", "Director Programa Academico"],
)

fake.add_provider(perfil_usuario_provider)
fake.add_provider(rol_usuario_provider)


def test_create_usuario(client: TestClient, db: Session) -> None:
    cedula = fake.pyint(min_value=9999999, max_value=999999999)
    nombre = fake.first_name()
    apellido = fake.last_name()
    correo = nombre + apellido + "@example.com"
    activo = fake.pybool()
    rol = fake.rol_usuario()
    horas_laborales = fake.pyint(min_value=20, max_value=40, step=20)
    password = "Passwordtest"
    perfil = fake.perfil_usuario()

    data = {
        "cedula": cedula,
        "correo": correo,
        "nombre": nombre,
        "apellido": apellido,
        "activo": activo,
        "rol": rol,
        "horas_laborales": horas_laborales,
        "password": password,
        "perfil": perfil,
    }

    r = client.post(uri_endopoint, json=data)
    assert 200 <= r.status_code < 300


def test_get_all_usuarios(client: TestClient, db: Session) -> None:
    r = client.get(uri_endopoint)
    assert 200 <= r.status_code < 300


def test_get_usuario(client: TestClient, db: Session) -> None:
    cedula = 1098811091
    r = client.get(f"{uri_endopoint}/{cedula}")
    assert 200 <= r.status_code < 300


def test_update_usuario(client: TestClient, db: Session) -> None:
    cedula = 1098811091
    nombre = fake.first_name()
    apellido = fake.last_name()
    correo = nombre + apellido + "@example.com"
    activo = fake.pybool()
    rol = fake.rol_usuario()
    horas_laborales = fake.pyint(min_value=20, max_value=40, step=20)
    perfil = fake.perfil_usuario()

    data = {
        "cedula": cedula,
        "correo": correo,
        "nombre": nombre,
        "apellido": apellido,
        "activo": activo,
        "rol": rol,
        "horas_laborales": horas_laborales,
        "perfil": perfil,
    }

    r = client.put(f"{uri_endopoint}/{cedula}", json=data)
    assert 200 <= r.status_code < 300


def test_delete_usuario(client: TestClient, db: Session) -> None:
    cedula = 2
    r = client.delete(f"{uri_endopoint}/{cedula}")
    assert 200 <= r.status_code < 300 or 204
