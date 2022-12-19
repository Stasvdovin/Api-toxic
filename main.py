from fastapi import FastAPI
from transformers import pipeline 
from pydantic import BaseModel
# Создаем класс для возможности передачи текста 
class Item(BaseModel):
    text: str
app = FastAPI()
# Создаем модель 
classifier = pipeline(model="SkolkovoInstitute/russian_toxicity_classifier")
@app.get('/')
def root():
    return {'message': 'Hello World'}
# Функция для определения токсичных комментариев и передачи теска 
@app.post("/predict/")
def predict(item: Item):
    """Анализ токсичных комменатиев"""
    return classifier(item.text )[0]
