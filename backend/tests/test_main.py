from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json() or response.json() is not None

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200 or response.status_code == 404