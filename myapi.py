from fastapi import FastAPI, UploadFile, File, Response
from pydantic import BaseModel
import requests  # to get image from the web
from PIL import Image
import io
from fastapi.staticfiles import StaticFiles
import os
# from fastapi.responses import FileResponse, HTMLResponse
import main


class Item(BaseModel):
    text: str


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    img = await file.read()
    return main.detect_objects(img, file.filename)

# Вход - текстовой вид - ссылка на картинку
# Выход 1 json
# {
#     "person": 0.99,
#     "image_url": "https://127.0.0.1:8000/static/filename.jpg"
# }

# Задача со *
# Вход 2 - файл, прикрутим html cтраницу, откуда можно загрузить картинку
# Выход 2: страница, где можем посмотреть результат обработки
