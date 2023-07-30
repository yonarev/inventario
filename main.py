from fastapi import FastAPI , Request #request es para la solicitudes
from fastapi.responses import HTMLResponse, FileResponse  # para procesar las respuestas
from fastapi.staticfiles import StaticFiles # para set carpeta static
from fastapi.templating import Jinja2Templates # para templates

app = FastAPI()

#CONFIGURA RUTA STATIC
app.mount("/static",StaticFiles(directory= "./static"),name='static') #set ruta para archivos estaticos

#CONFIGURA RUTA TEMPLATES
templates=Jinja2Templates(directory="templates")

# RUTA RAIZ
# ver en http://127.0.0.1:8000/url
@app.get("/",response_class=HTMLResponse)
async def root():
    #SE ENVIA WEB DESDE OTRA RUTA
    ruta_archivo="./templates/index.html"
    return FileResponse(ruta_archivo,status_code=200)
    # es un json key valor
    # SE ENVIA UN DICCIONARIO
    # return {"message": "Hello World"}
    # SE ENVIA PAGINA WEB DIRECTA
    # return """ 
    #     <html lang="en">
    #     <head>
    #         <meta charset="UTF-8">
    #         <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #         <title>Inventario</title>
    #     </head>
    #     <body>
    #         <h1>Inventario con fastapi</h1>
            
    #     </body>
    #     </html>
    # """
    
@app.get("/plantilla/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("plantilla.html", {"request": request, "id": id})

# RUTA plantilla
# @app.get("/plantilla/{id}",response_class=HTMLResponse)
# async def plantilla(request: Request, id:str):
#     return templates.TemplateResponse("plantilla.html",{"request": request,"id":id})
