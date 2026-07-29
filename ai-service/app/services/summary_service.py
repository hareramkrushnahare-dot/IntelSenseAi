"""Summary service for generating concise output summaries."""

from __future__ import annotations

from typing import Any


class SummaryService:
    """Create summary payloads for simple API responses."""

    async def build_summary(self, prediction: dict[str, Any]) -> dict[str, Any]:
        result = prediction.get("result", {})
        return {
            "summary": result.get("summary", ""),
            "keywords": result.get("keywords", []),
            "recommendations": result.get("recommendations", []),
        }
