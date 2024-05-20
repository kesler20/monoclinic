from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Set up template directory
templates = Jinja2Templates(directory="templates")

# Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.api_route("/{route}/", methods=["POST", "GET"], response_class=HTMLResponse)
def show(request: Request, route: str):
    page = {
        "home": "index",
        "product_overview": "product_overview",
        "case_studies": "case_studies",
        "contact": "contact",
    }.get(route, "404")
    return templates.TemplateResponse(f"{page}.html", {"request": request})
