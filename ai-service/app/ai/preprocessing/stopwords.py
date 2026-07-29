STOPWORDS = {"the", "is", "at", "which", "on", "and", "a"}


def remove_stopwords(tokens):
    return [t for t in tokens if t.lower() not in STOPWORDS]
