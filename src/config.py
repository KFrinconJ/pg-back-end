from starlette.config import Config
from pydantic import AnyHttpUrl, BaseModel, validator
from typing import List, Union


config = Config(".env")

# Variables que se traen desde las variables de entorno que estan en el archivo .env

# Variables de la base de datos
DATABASE_USERNAME = config("DATABASE_USERNAME")
DATABASE_PASSWORD = config("DATABASE_PASSWORD")
DATABASE_HOSTNAME = config("DATABASE_HOSTNAME")
DATABASE_PORT = config("DATABASE_PORT")
DATABASE_NAME = config("DATABASE_NAME")


# URI para la conexion con labase de datos
SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE_NAME}"


# AUTH0
DOMAIN = config("DOMAIN")
API_AUDIENCE = config("API_AUDIENCE")
ISSUER = config("ISSUER")
ALGORITHMS = config("ALGORITHMS")
CLIENT_ORIGIN_URL = config("CLIENT_ORIGIN_URL")
PORT = config("PORT")


# DEPLOY 
RELOAD = config("RELOAD")


# Settings
class Settings(BaseModel):
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost",
        "http://localhost:4200",
        "http://localhost:3000",
        "http://localhost:8080",
        "http://local.dockertoolbox.tiangolo.com",
    ]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = (
        "Sistema para el registro y control de las funciones sustantivas"
    )


settings = Settings()
