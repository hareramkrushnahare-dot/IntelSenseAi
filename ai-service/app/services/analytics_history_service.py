from __future__ import annotations

from typing import Any

from app.repositories.analytics_repository import AnalyticsRepository


class AnalyticsHistoryService:
    def __init__(self, session: Any) -> None:
        self.session = session
        self.repo = AnalyticsRepository(session)

    async def get_history(self, limit: int = 20) -> list[dict[str, Any]]:
        events = await self.repo.list_recent(limit=limit)
        return [
            {
                "id": event.id,
                "source": event.source,
                "sentiment_label": event.sentiment_label,
                "sentiment_score": event.sentiment_score,
                "topics": event.topics or [],
                "keywords": event.keywords or [],
                "aspects": event.aspects or [],
                "summary": event.summary,
                "created_at": event.created_at.isoformat() if event.created_at else None,
            }
            for event in events
        ]
