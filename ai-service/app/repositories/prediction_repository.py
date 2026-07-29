from __future__ import annotations

from typing import Any

from sqlalchemy import select

from app.models.prediction import Prediction
from app.repositories.base_repository import BaseRepository


class PredictionRepository(BaseRepository):
    async def save(self, input_text: str, result: dict[str, Any], source: str | None = None) -> Prediction:
        obj = Prediction(input_text=input_text, result=result, source=source)
        self.session.add(obj)
        await self.session.flush()
        await self.session.refresh(obj)
        return obj

    async def get(self, prediction_id: int) -> Prediction | None:
        statement = select(Prediction).where(Prediction.id == prediction_id)
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def list_recent(self, limit: int = 10) -> list[Prediction]:
        statement = select(Prediction).order_by(Prediction.created_at.desc()).limit(limit)
        result = await self.session.execute(statement)
        return list(result.scalars().all())
