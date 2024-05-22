import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Get the absolute path to the directory where this file is located
dir_path = os.path.dirname(os.path.realpath(__file__))

# Set up template directory
templates = Jinja2Templates(directory=os.path.join(dir_path, "templates"))

# Mount static directory
app.mount(
    "/static", StaticFiles(directory=os.path.join(dir_path, "static")), name="static"
)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
async def handle_form(request: Request, email: str = Form(...)):
    with open("emails.txt", "a") as f:
        f.write(email + "\n")

    return templates.TemplateResponse(f"thankyou.html", {"request": request})


@app.get("/api/emails", response_class=FileResponse)
def get_email_responses():
    return FileResponse(os.path.join(dir_path, "emails.txt"))


@app.api_route("/{route}/", methods=["POST", "GET"], response_class=HTMLResponse)
def show(request: Request, route: str):
    page = {
        "home": "index",
        "product_overview": "product_overview",
        "case_studies": "case_studies",
        "contact": "contact",
        "thankyou": "thankyou",
    }.get(route, "404")

    return templates.TemplateResponse(f"{page}.html", {"request": request})
