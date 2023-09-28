from fastapi import FastAPI, File, UploadFile



app = FastAPI()



@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/personas")
def get_personas():
    return {"id":1,"nombre": "Dejah"}

@app.get("/v1/contactos")
async def get_contactos(file: bytes = File("contactos.csv")):
    # TODO read contactos.csv
    # TODO JSON encode contactos.csv
    # TODO save in response
    response = []
    return response