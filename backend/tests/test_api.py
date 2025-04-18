from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "Lambda Serverless" in response.json()["title"]

def test_list_functions_empty():
    response = client.get("/functions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list) 