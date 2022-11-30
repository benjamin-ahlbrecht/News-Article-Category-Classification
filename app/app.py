from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder

from jinja2.exceptions import TemplateNotFound


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")
templates = Jinja2Templates(directory="html")

@app.get("/", response_class=HTMLResponse)
async def read_project(request:Request):
    return templates.TemplateResponse(
        name="index.html",
        context={"request": request}
    )