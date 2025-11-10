# src/sdsrc/api.py
from pathlib import Path
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sdsrc.normalize import normalize_whitespace
from sdsrc.textutils import count_words, reverse_words

app = FastAPI(title="Text Utilities API")

TEMPLATE_DIR = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to the Text Utilities API"}


@app.get("/normalize")
def normalize(text: str) -> dict[str, str]:
    """Normalize whitespace in a string."""
    return {"normalized": normalize_whitespace(text)}


@app.get("/count")
def count(text: str) -> dict[str, int]:
    """Count words in a string."""
    count = count_words(text)
    return {"word_count": count}


@app.get("/reverse")
def reverse(text: str) -> dict[str, str]:
    """Reverse word order in a string."""
    reversed_text = reverse_words(text)
    return {"reversed": reversed_text}


@app.get("/ui", response_class=HTMLResponse)
def ui_form(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("ui.html", {"request": request, "result": None})


@app.post("/ui/submit", response_class=HTMLResponse)
def ui_submit(
    request: Request, text: str = Form(...), op: str = Form(...)
) -> HTMLResponse:
    result: str | int

    if op == "normalize":
        result = normalize_whitespace(text)
    elif op == "count":
        result = count_words(text)
    elif op == "reverse":
        result = reverse_words(text)
    else:
        result = "Unknown operation."

    return HTMLResponse(str(result))
