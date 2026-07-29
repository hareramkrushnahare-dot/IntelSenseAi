def predict_emotions(text: str):
    lower = text.lower()
    return {
        "joy": 0.7 if "love" in lower or "great" in lower else 0.1,
        "anger": 0.1 if "hate" in lower else 0.0,
        "sadness": 0.1 if "sad" in lower else 0.0,
    }
