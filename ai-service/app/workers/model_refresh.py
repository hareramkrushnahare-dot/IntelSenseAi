import asyncio
from loguru import logger


async def refresh_models_periodically():
    while True:
        logger.info("Refreshing models if needed (placeholder)")
        await asyncio.sleep(60 * 60)
