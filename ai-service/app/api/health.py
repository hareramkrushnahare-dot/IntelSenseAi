from fastapi import APIRouter
from app.database.health import is_db_ready
from app.cache.redis_client import redis_client

router = APIRouter()


@router.get("/health")
async def health():
    db_ready = await is_db_ready()
    redis_ready = await redis_client.ping()
    return {"status": "ok", "db": db_ready, "redis": redis_ready}
