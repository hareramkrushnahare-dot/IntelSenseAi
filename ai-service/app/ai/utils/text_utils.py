import re


def is_english(text: str) -> bool:
    return bool(re.search(r"[a-zA-Z]", text))
