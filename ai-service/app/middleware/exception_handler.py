from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.exceptions import ServiceError


class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except ServiceError as se:
            return JSONResponse(status_code=se.code, content={"status": "error", "message": se.message})
        except Exception as e:
            return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})
