from fastapi import FastAPI

from .database.core import engine
from starlette.requests import Request

from sqlalchemy.orm import sessionmaker, scoped_session
from .api import api_router

# ASGI para el framework
app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    try:
        # Crea una sesión de base de datos
        session = scoped_session(sessionmaker(bind=engine))
        request.state.db = session()
        # Llama al siguiente manipulador en la cadena
        response = await call_next(request)
    except Exception as e:
        raise e from None
    finally:
        # Cierra la sesión de la base de datos
        request.state.db.close()

    return response


@app.get("/")
def hello_world():
    return "Hola Mundo"


@app.get("/test-db-connection")
def test_db_connection():
    try:
        # Realiza una consulta de prueba en la base de datos
        result = engine.execute("SELECT 1")
        return {"message": "Conexión a la base de datos exitosa"}
    except Exception as e:
        return {"message": "Error al conectar a la base de datos", "error": str(e)}


# Añadimos todas la rutas
app.include_router(api_router)
