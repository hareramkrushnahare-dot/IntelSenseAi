from fastapi import APIRouter
from app.services.analytics_service import AnalyticsService

router = APIRouter()
service = AnalyticsService()


@router.get("/analytics")
async def analytics():
    sample_predictions = [
        {
            "result": {
                "sentiment": {"label": "positive", "score": 0.9},
                "topics": ["support", "quality"],
            }
        }
    ]
    return {"status": "ok", "data": await service.build_analytics(sample_predictions)}
