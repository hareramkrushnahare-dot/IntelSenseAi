import asyncio
from loguru import logger


async def background_report_task():
    while True:
        logger.info("Generating periodic report (dummy task)")
        await asyncio.sleep(60 * 60)
