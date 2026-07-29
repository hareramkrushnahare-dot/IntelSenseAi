from functools import lru_cache


@lru_cache()
def dummy_sentiment(text: str):
    lower = text.lower()
    label = "positive" if "good" in lower or "love" in lower else "negative" if "bad" in lower or "hate" in lower else "neutral"
    return {"label": label, "score": 0.9}


@lru_cache()
def dummy_summary(text: str):
    if len(text) <= 150:
        return text
    return text[:147] + "..."


class DummyModels:
    @staticmethod
    def register():
        return True
