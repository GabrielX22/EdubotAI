def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "activo"

def test_get_metadata(client):
    response = client.get("/metadata")
    assert response.status_code == 200
    assert response.json()["proyecto"] == "EdubotAI"

def test_chat_invalid_module(client):
    payload = {
        "estudiante_id": "UGB2026",
        "mensaje": "¿Qué es una variable?",
        "modulo": "ModuloInvalido"
    }
    response = client.post("/chat", json=payload)
    assert response.status_code == 400