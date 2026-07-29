import json
from typing import Any
from app.cache.redis_client import redis_client


async def get_cached(key: str):
    if not await redis_client.ping():
        return None
    val = await redis_client._conn.get(key)
    if not val:
        return None
    return json.loads(val)


async def set_cached(key: str, value: Any, ttl: int = 3600):
    if not await redis_client.ping():
        return False
    await redis_client._conn.set(key, json.dumps(value), ex=ttl)
    return True
