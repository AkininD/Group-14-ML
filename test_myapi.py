from fastapi.testclient import TestClient
from myapi import app
import json

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


# проверка распознавания на тестовых изображениях
def test_predict_cat():
    filename = "./tests/fixtures/cat.jpg"
    response = client.post("/predict", files={"file": ("cat.jpg", open(filename, "rb"), "image/jpeg")})
    predict_response = json.loads(response.content)
    assert response.status_code == 200
    assert any('cat' in d for d in predict_response)
    assert any('image_url' in d for d in predict_response)


def test_predict_elephant():
    filename = "./tests/fixtures/elephant.jpg"
    response = client.post("/predict", files={"file": ("elephant.jpg", open(filename, "rb"), "image/jpeg")})
    predict_response = json.loads(response.content)
    assert response.status_code == 200
    assert any('elephant' in d for d in predict_response)
    assert any('image_url' in d for d in predict_response)
    tear_down()

    
def test_predict_sandwich():
    filename = "./tests/fixtures/sandwich.jpg"
    response = client.post("/predict", files={"file": ("sandwich.jpg", open(filename, "rb"), "image/jpeg")})
    predict_response = json.loads(response.content)
    assert response.status_code == 200
    assert any('sandwich' in d for d in predict_response)
    assert any('image_url' in d for d in predict_response)
    tear_down()

    
# удаление тестовых файлов
def tear_down():
    import os
    files = [f for f in os.listdir('./static') if os.path.isfile(os.path.join('./static', f))]
    for file in files:
        if file == '.keep':
            continue
        os.remove(f'./static/{file}')
