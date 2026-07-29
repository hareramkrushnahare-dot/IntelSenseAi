from __future__ import annotations

from typing import Any

from sqlalchemy import select

from app.models.analytics_event import AnalyticsEvent
from app.repositories.base_repository import BaseRepository


class AnalyticsRepository(BaseRepository):
    async def save(self, payload: dict[str, Any]) -> AnalyticsEvent:
        event = AnalyticsEvent(**payload)
        self.session.add(event)
        await self.session.flush()
        await self.session.refresh(event)
        return event

    async def list_recent(self, limit: int = 20) -> list[AnalyticsEvent]:
        statement = select(AnalyticsEvent).order_by(AnalyticsEvent.created_at.desc()).limit(limit)
        result = await self.session.execute(statement)
        return list(result.scalars().all())
