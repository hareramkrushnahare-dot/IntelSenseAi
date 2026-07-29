"""Analytics service for aggregate AI insights."""

from __future__ import annotations

from typing import Any


class AnalyticsService:
    """Create aggregate analytics payloads from prediction results."""

    async def build_analytics(self, predictions: list[dict[str, Any]]) -> dict[str, Any]:
        if not predictions:
            return {"total_predictions": 0, "sentiment_breakdown": {}, "topics": []}

        sentiment_breakdown: dict[str, int] = {}
        topics: list[str] = []
        for prediction in predictions:
            result = prediction.get("result", {})
            sentiment = result.get("sentiment", {})
            label = sentiment.get("label", "neutral")
            sentiment_breakdown[label] = sentiment_breakdown.get(label, 0) + 1
            topics.extend(result.get("topics", []))

        return {
            "total_predictions": len(predictions),
            "sentiment_breakdown": sentiment_breakdown,
            "topics": sorted(set(topics)),
        }
