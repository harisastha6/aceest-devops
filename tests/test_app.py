from app.app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"ACEest" in response.data


def test_add_client():
    client = app.test_client()
    response = client.post("/clients", json={"name": "Hari"})
    assert response.status_code in [200, 201, 400]


def test_get_clients():
    client = app.test_client()
    response = client.get("/clients")
    assert response.status_code == 200