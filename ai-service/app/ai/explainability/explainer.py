"""Explainability utilities for AI predictions."""

from __future__ import annotations

from typing import Any


def explain_prediction(text: str, result: dict[str, Any]) -> dict[str, Any]:
    sentiment = result.get("sentiment", {}).get("label", "neutral")
    keywords = result.get("keywords", [])
    return {
        "summary": f"Prediction was driven by sentiment '{sentiment}' and the presence of keywords {keywords[:3]}",
        "features": [
            {"name": "sentiment", "value": sentiment},
            {"name": "keywords", "value": keywords[:5]},
        ],
    }
