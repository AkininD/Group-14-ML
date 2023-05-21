from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
import main
import awesome_log

logger = awesome_log.Logger(__name__)
a_log = logger.printer()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    a_log.info("Root")
    return {"message": "Hello World"}


@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    a_log.info("Prediction started")
    img = await file.read()
    return main.detect_objects(img, file.filename)
