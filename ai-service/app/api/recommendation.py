from fastapi import APIRouter

router = APIRouter()


@router.get("/recommendations")
async def recommendations():
    return {
        "status": "ok",
        "recommendations": [
            "Prioritize service quality improvements",
            "Monitor recurring sentiment themes",
        ],
    }
