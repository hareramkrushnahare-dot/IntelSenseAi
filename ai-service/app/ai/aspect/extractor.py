"""Aspect extraction utilities for ABSA-style analysis."""

from __future__ import annotations

from typing import Any


def extract_aspects(text: str) -> list[dict[str, Any]]:
    lower = text.lower()
    aspects: list[dict[str, Any]] = []
    if "battery" in lower:
        aspects.append({"aspect": "battery", "sentiment": "positive" if "good" in lower else "neutral"})
    if "price" in lower:
        aspects.append({"aspect": "price", "sentiment": "negative" if "expensive" in lower else "neutral"})
    if "support" in lower:
        aspects.append({"aspect": "support", "sentiment": "negative" if "bad" in lower else "positive"})
    return aspects or [{"aspect": "general", "sentiment": "neutral"}]
