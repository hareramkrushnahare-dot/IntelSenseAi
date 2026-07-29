from pydantic import BaseModel


class ApiSettings(BaseModel):
    prefix: str = "/api/v1"
