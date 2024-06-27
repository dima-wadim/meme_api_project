from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_meme():
    response = client.post("/memes/", json={"title": "Funny Cat", "description": "A very funny cat meme", "image_url": "http://localhost:9000/memes/funny_cat.jpg"})
    assert response.status_code == 200
    assert response.json()["title"] == "Funny Cat"

def test_read_meme():
    response = client.get("/memes/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Funny Cat"

def test_read_memes():
    response = client.get("/memes/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_meme():
    response = client.put("/memes/1", json={"title": "Funnier Cat", "description": "An even funnier cat meme", "image_url": "http://localhost:9000/memes/funnier_cat.jpg"})
    assert response.status_code == 200
    assert response.json()["title"] == "Funnier Cat"

def test_delete_meme():
    response = client.delete("/memes/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Funnier Cat"
