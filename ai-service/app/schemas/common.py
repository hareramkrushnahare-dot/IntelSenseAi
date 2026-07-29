from pydantic import BaseModel
from typing import Optional


class APIResponse(BaseModel):
    status: str
    message: Optional[str] = None
