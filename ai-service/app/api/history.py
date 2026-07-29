from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependency import get_db_session
from app.services.analytics_history_service import AnalyticsHistoryService

router = APIRouter()


@router.get("/analytics-history")
async def analytics_history(limit: int = 20, db: AsyncSession = Depends(get_db_session)):
    service = AnalyticsHistoryService(db)
    return {"status": "ok", "data": await service.get_history(limit=limit)}
