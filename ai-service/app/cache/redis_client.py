from app.core.config import settings

try:
    from redis import asyncio as aioredis
except Exception:
    import aioredis


class RedisClient:
    def __init__(self):
        self._url = settings.REDIS_URL
        self._conn = None

    async def connect(self):
        if self._conn is None:
            self._conn = aioredis.from_url(self._url, decode_responses=True)

    async def close(self):
        if self._conn is not None:
            await self._conn.close()
            self._conn = None

    async def ping(self):
        try:
            if self._conn is None:
                await self.connect()
            return await self._conn.ping()
        except Exception:
            return False


redis_client = RedisClient()
