from pydantic import BaseModel


class RedisSettings(BaseModel):
    url: str = "redis://localhost:6379/0"
