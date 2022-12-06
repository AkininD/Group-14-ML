from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
import main


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    img = await file.read()
    return main.detect_objects(img, file.filename)
