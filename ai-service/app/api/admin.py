from fastapi import APIRouter

router = APIRouter()


@router.get("/admin")
async def admin():
    return {"status": "ok"}
