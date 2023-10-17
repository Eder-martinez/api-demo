import csv
import json
import os
import requests
import random

from fastapi import FastAPI, HTTPException
from fastapi import File, UploadFile
from pydantic import BaseModel
from PIL import Image, ImageOps, ImageFilter, ImageEnhance
from io import BytesIO
from typing import List, Union
from fastapi.responses import FileResponse

app = FastAPI()
class Contacto(BaseModel):
    id : int
    nombre : str
    primer_apellido : str
    segundo_apellido : str
    email : str
    telefono : int

@app.get("/contactos")
async def get_contactos():
    contactos = []
    with open('contactos.csv', mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contactos.append(row)
    return contactos
    
@app.post("/contactos")
async def agregar(contacto: Contacto):
    try:
        nuevo_contacto = contacto.dict()
        filename = 'contactos.csv'

        existe = os.path.isfile(filename)

        with open(filename, 'a', newline='') as csv_file:
            fieldnames = nuevo_contacto.keys()
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if not existe:
                csv_writer.writeheader()
            
            csv_writer.writerow(nuevo_contacto)
            csv_file.write('/n')
        return  nuevo_contacto
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al agregar registro: {str(e)}")

@app.put("/contactos/{contacto_id}")
async def actualizar(contacto_id: int, nuevo_contacto: Contacto):
    try:
        contactos = []
        with open('contactos.csv', 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                contactos.append(row)
        contacto_actualizado = None
        for contacto in contactos:
            if int(contacto['id']) == contacto_id:
                contacto_actualizado = nuevo_contacto.dict()
                contacto_actualizado['id'] = contacto_id
                break
        if contacto_actualizado is None:
            raise HTTPException(status_code=404, detail="Contacto no encontardo")

        with open('contactos.csv', 'w', newline='') as csv_file:
            fieldnames = contacto_actualizado.keys()
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for contacto in contactos:
                if int(contacto['id']) == contacto_id:
                    csv_writer.writerow(contacto_actualizado)
                else:
                    csv_writer.writerow(contacto)
        return contacto_actualizado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inter del servidor")

@app.delete("/contactos/{contacto_id}")
async def eliminar(contacto_id: int):
    try:
        contactos = []
        with open('contactos.csv', 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                contactos.append(row)
        contacto_eliminado = None
        nuevos_contactos = []
        for contacto in contactos:
            if int(contacto['id']) == contacto_id:
                contacto_eliminado= contacto
            else:
                nuevos_contactos.append(contacto)
        if contacto_eliminado is None:
            raise HTTPException(status_code=404, detail="Contacto no encontrado")
        with open('contactos.csv', 'w', newline='') as csv_file:
            fieldnames = nuevos_contactos[0].keys()
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for contacto in nuevos_contactos:
                csv_writer.writerow(contacto)
        return contacto_eliminado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor")
    
@app.get("/contactos/{contacto_nombre}")
async def contacto_nombre(contacto_nombre: str):
    try:
        contactos = []
        with open('contactos.csv', mode='r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                contactos.append(row)
        contacto_encontrado = None
        for contacto in contactos:
            if str(contacto['nombre']) == contacto_nombre:
                contacto_encontrado = contacto
                break
        if contacto_encontrado is None:
            raise HTTPException(status_code=404, detail="Contacto no encontrado")
        return contacto_encontrado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor")

def aplicar_efectos(image, crop_params, flip_horizontal, colorize):
    if crop_params:
        crop_x, crop_y, crop_width, crop_height = crop_params
        image = image.crop((crop_x, crop_y, crop_x + crop_width, crop_y + crop_height))
    if flip_horizontal:
        image = ImageOps.mirror(image)
    if colorize:
        enhancer = ImageEnhance.Color(image)
        image = enhancer.enhance(2.0)
    return image

@app.post("/imagenes")
async def imagen(file: UploadFile, crop_x: int = 0, crop_y: int = 0, crop_width: int = 0, crop_height: int = 0, flip_horizontal: bool = False, colorize: bool = False):
    try:
        folder_path = "imagenes"
        os.makedirs(folder_path, exist_ok=True)
        image_path = os.path.join(folder_path, file.filename)
        with open(image_path, "wb") as image_file:
            image_file.write(file.file.read())
        im = Image.open(image_path)
        im = aplicar_efectos(im, (crop_x, crop_y, crop_width, crop_height), flip_horizontal, colorize)
        im.save(image_path)
        return FileResponse(image_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor")


@app.get("/contactos-ordenados")
async def get_contactos():
    contactos = []
    with open('contactos.csv', mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contactos.append(row)
    contactos_ordenados = sorted(contactos, key=lambda x: x['primer_apellido'])
    return contactos_ordenados

def orden_burbuja(numeros):
    n = len(numeros)
    for i in range(n):
        for j in range(0, n - i  - 1):
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

@app.post("/random-numero")
async def numero_random(numeros: List[int]):
    try:
        if not numeros:
            raise HTTPException(status_code=400, detail="La lista está vacía")
        orden_burbuja(numeros)
        return numeros
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor")
