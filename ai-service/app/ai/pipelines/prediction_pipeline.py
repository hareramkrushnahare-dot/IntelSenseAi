"""High-level prediction pipeline orchestrating the AI modules."""

from __future__ import annotations

from app.ai.aspect.extractor import extract_aspects
from app.ai.emotion.predict import predict_emotions
from app.ai.explainability.explainer import explain_prediction
from app.ai.keywords.extract import extract_keywords
from app.ai.preprocessing.cleaner import clean_text
from app.ai.recommendation.recommend import recommend_actions
from app.ai.sentiment.predict import predict_sentiment
from app.ai.summarization.summarize import summarize_text
from app.ai.topics.model import extract_topics


class PredictionPipeline:
    """Coordinate the AI analysis workflow for a feedback text."""

    async def run(self, text: str) -> dict[str, object]:
        cleaned = clean_text(text)
        sentiment = predict_sentiment(cleaned)
        emotions = predict_emotions(cleaned)
        aspects = extract_aspects(cleaned)
        keywords = extract_keywords(cleaned)
        topics = extract_topics(cleaned)
        summary = summarize_text(cleaned)
        explanation = explain_prediction(cleaned, {"sentiment": sentiment, "keywords": keywords})
        recommendations = recommend_actions(sentiment, emotions, keywords, topics)

        return {
            "sentiment": sentiment,
            "emotions": emotions,
            "aspects": aspects,
            "keywords": keywords,
            "topics": topics,
            "summary": summary,
            "explainability": explanation,
            "recommendations": recommendations,
        }
