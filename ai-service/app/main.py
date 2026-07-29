from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.logging import init_logging
from app.api import health, prediction, summary, analytics, recommendation, admin, history
from app.middleware.request_logging import RequestLoggingMiddleware
from app.middleware.exception_handler import ExceptionMiddleware
from app.middleware.jwt_auth import JWTAuthMiddleware
from app.cache.redis_client import redis_client
from app.services.ai_manager import AIManager


def create_app() -> FastAPI:
    init_logging()
    app = FastAPI(
        title=settings.APP_NAME,
        openapi_url=f"{settings.API_PREFIX}/openapi.json",
        docs_url=f"{settings.API_PREFIX}/docs",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"] if settings.ENVIRONMENT == "development" else [],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(RequestLoggingMiddleware)
    app.add_middleware(ExceptionMiddleware)
    app.add_middleware(JWTAuthMiddleware)

    app.include_router(health.router, prefix=settings.API_PREFIX, tags=["health"])
    app.include_router(prediction.router, prefix=settings.API_PREFIX, tags=["prediction"])
    app.include_router(summary.router, prefix=settings.API_PREFIX, tags=["summary"])
    app.include_router(analytics.router, prefix=settings.API_PREFIX, tags=["analytics"])
    app.include_router(recommendation.router, prefix=settings.API_PREFIX, tags=["recommendation"])
    app.include_router(admin.router, prefix=settings.API_PREFIX, tags=["admin"])
    app.include_router(history.router, prefix=settings.API_PREFIX, tags=["history"])

    @app.on_event("startup")
    async def startup():
        await redis_client.connect()
        await AIManager.initialize(use_dummy=settings.USE_DUMMY_MODELS)

    @app.on_event("shutdown")
    async def shutdown():
        await redis_client.close()

    return app


app = create_app()
