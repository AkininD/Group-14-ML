from fastapi import FastAPI
from pydantic import BaseModel
import requests  # to get image from the web
import main
from PIL import Image
import io
from fastapi.staticfiles import StaticFiles
class Item(BaseModel):
    text: str


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    # Set up the image URL and filename
    image_url = item.text
    filename = image_url.split("/")[-1]
    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream=True)
    img = Image.open(io.BytesIO(r.content))
    return main.detect_objects(img, filename).split('/')


