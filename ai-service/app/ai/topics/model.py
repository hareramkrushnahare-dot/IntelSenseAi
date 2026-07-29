from app.ai.models.bertopic_loader import topic_model_predict


def extract_topics(text: str):
    return topic_model_predict([text])
