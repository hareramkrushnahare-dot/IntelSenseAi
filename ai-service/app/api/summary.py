from fastapi import APIRouter
from app.services.summary_service import SummaryService

router = APIRouter()
service = SummaryService()


@router.post("/summary")
async def summarize():
    prediction = {
        "result": {
            "summary": "Customer feedback indicates positive sentiment and strong product satisfaction.",
            "keywords": ["support", "quality"],
            "recommendations": ["Continue monitoring customer experience"],
        }
    }
    return {"status": "ok", **await service.build_summary(prediction)}
