from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_create_todo():
    response = client.post("/todos", json={"title": "Test Todo"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Todo"
def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
def test_get_invalid_id():
    response = client.get("/todos/99999")
    assert response.status_code == 404