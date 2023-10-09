from typing import Annotated

from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/")
def read_root():
    return"ci"

@app.post("/static/images/file/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/static/images/upload/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.fiilename}

app.mount("/static/images", StaticFiles(directory="static"), name="static")
