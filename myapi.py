from fastapi import FastAPI, UploadFile, File, Response
from pydantic import BaseModel
import requests  # to get image from the web
import main
from PIL import Image
import io
from fastapi.staticfiles import StaticFiles
import os
from fastapi.responses import FileResponse, HTMLResponse


class Item(BaseModel):
    text: str


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


# @app.get("/")
# def root():
#     return {"message": "Hello World"}
@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

path = "./static/"


@app.post("/predict/")
def predict(item: Item):
    # Set up the image URL and filename
    image_url = item.text
    filename = image_url.split("/")[-1]
    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream=True)
    img = Image.open(io.BytesIO(r.content))
    return main.detect_objects(img, filename)


# @app.get("/vector_image", responses={200: {"description": "A picture of a vector image.", "content": {
#     "image/jpeg": {"example": "No example available. Just imagine a picture of a vector image."}}}})
# def image_endpoint():
#     file_path = os.path.join(path, "lamb.jpg")
#     if os.path.exists(file_path):
#         return FileResponse(file_path, media_type="image/jpeg", filename="lamb.jpg")
#     return {"error": "File not found!"}


# @app.post("/files/")
# def predict(file: UploadFile = File(...)):
#     file_bytes = file.file.read()
#     image = Image.open(io.BytesIO(file_bytes))
#     # new_image = prepare_image(image)
#     # result = predict(image)
#     bytes_image = io.BytesIO()
#     image.save(bytes_image, format='PNG')
#     return Response(content=bytes_image.getvalue(), headers={}, media_type="image/png")
# Вход - текстовой вид - ссылка на картинку
# Выход 1 json
# {
#     "person": 0.99,
#     "image_url": "https://127.0.0.1:8000/static/filename.jpg"
# }

# Задача со *
# Вход 2 - файл, прикрутим html cтраницу, откуда можно загрузить картинку
# Выход 2: страница, где можем посмотреть результат обработки
# @app.post("/files/")
# async def create_files(
#     files: list[bytes] = File(description="Multiple files as bytes"),
# ):
#     return {"file_sizes": [len(file) for file in files]}
#
#
# @app.post("/uploadfiles/")
# async def create_upload_files(
#     files: list[UploadFile] = File(description="Multiple files as UploadFile"),
# ):
#     return {"filenames": [file.filename for file in files]}