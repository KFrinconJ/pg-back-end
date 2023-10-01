from starlette.config import Config

config = Config(".env")

# Variables que se traen desde las variables de entorno que estan en el archivo .env

# Variables de la base de datos
DATABASE_USERNAME = config("DATABASE_USERNAME")
DATABASE_PASSWORD = config("DATABASE_PASSWORD")
DATABASE_HOSTNAME = config("DATABASE_HOSTNAME")
DATABASE_PORT = config("DATABASE_PORT")
DATABASE_NAME = config("DATABASE_NAME")

# Variables para la base de datos de desarrollo y pruebas
DATABASE_DEV_NAME = config("DEVELOPING_DB_NAME")
DATABASE_DEV_USERNAME = config("DEVELOPING_DB_USERNAME")
DATABASE_DEV_PASSWORD = config("DEVELOPING_DB_PASSWORD")


# URI para la conexion con labase de datos
SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE_NAME}"
# URI para la base de datos de desarrollo y pruebas
SQLALCHEMY_DEVELOPER_DATABASE_URI = f"postgresql+psycopg2://{DATABASE_DEV_USERNAME}:{DATABASE_DEV_PASSWORD}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE_DEV_NAME}"


# JWT
JWT_SECRET = config("JWT_SECRET", default=None)
JWT_ALG = config("JWT_ALG", default="HS256")
JWT_EXP = config("JWT_EXP", cast=int, default=86400)
