def extract_keywords_with_keybert(text: str, top_n: int = 5):
    words = text.split()
    return list(dict.fromkeys(words))[:top_n]
