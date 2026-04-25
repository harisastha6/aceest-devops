from app.app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_add_client():
    client = app.test_client()
    response = client.post("/clients", json={"name": "Hari"})
    assert response.status_code in [200, 201]