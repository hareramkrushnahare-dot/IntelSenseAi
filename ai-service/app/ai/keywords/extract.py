from app.ai.models.keybert_loader import extract_keywords_with_keybert


def extract_keywords(text: str, top_n: int = 8):
    return extract_keywords_with_keybert(text, top_n=top_n)
