def test_db_connection(client):
    response = client.get("/test-db-connection")
    assert response.status_code == 200
    assert response.json()["message"] == "Conexión a la base de datos exitosa"