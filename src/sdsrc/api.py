# src/sdsrc/api.py
from fastapi import FastAPI
from sdsrc.normalize import normalize_whitespace
from sdsrc.textutils import count_words, reverse_words

app = FastAPI(title="Text Utilities API")


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
