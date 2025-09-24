# normalize.py
import re

def normalize_whitespace(text: str) -> str:
    text = text.replace("\u00A0", " ")
    text = text.strip()
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        line = re.sub(r"[ \t]+", " ", line.strip())
        cleaned.append(line)
    compact = []
    prev_blank = False
    for line in cleaned:
        is_blank = (line == "")
        if is_blank and prev_blank:
            continue
        compact.append(line)
        prev_blank = is_blank
    return "\n".join(compact)


