from fastapi import FastAPI, status



app = FastAPI()



@app.get("/")
def read_root():
    def root():
    """
    #Endpoint raíz
    ##1-Status codes
    *298-
    *301-
    """
    return {"message": "Hello World"}

@app.get("/personas")
def get_personas():
    return {"id":1,"nombre": "Dejah"}

@app.get(
     "/v1/contactos",
     status_code=201,
     description="Endpoint raiz de la API Contactos",
     summary="Endpoint raiz"
     )

async def get_contactos():
    # TODO read contactos.csv
    # TODO JSON encode contactos.csv
    # TODO save in response
    response = []
    return response