import time
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        logger.info(f"Start {request.method} {request.url}")
        response = await call_next(request)
        duration = (time.time() - start) * 1000
        logger.info(f"End {request.method} {request.url} status={response.status_code} duration_ms={duration:.2f}")
        return response
