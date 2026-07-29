from pydantic import BaseModel


class AppSettings(BaseModel):
    max_request_size: int = 10_000
