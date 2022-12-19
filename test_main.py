# Подключаем TestClient для тестирования Api
from fastapi.testclient import TestClient
# Импортируем объект app из файла main.py
from main import app
# Создаем клиента дляя тестирования 
client = TestClient(app)
# Тест определяет доступность приложения к корню сервера
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
# Тест определяет доступность приложение и проверяет нейтральные комментарии
def test_read_predict_neutral():
    response = client.post("/predict/",
        json = {"text": "Я думаю, вот эта ссылка будет кстати"}
    )
    json_data = response.json()

    assert response.status_code == 200
    assert json_data["label"] == "neutral"
# Тест определяет доступность приложение и проверяет токсичные комментарии
def test_read_predict_toxic():
    response = client.post("/predict/",
        json = {"text": "А ты кто такой?Иди отседова"}
    )
    json_data = response.json()

    assert response.status_code == 200
    assert json_data["label"] == "neutral"   
