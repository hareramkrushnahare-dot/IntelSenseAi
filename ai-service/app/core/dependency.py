from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import DatabaseSession, get_db


async def get_db_session() -> AsyncIterator[AsyncSession]:
    session = DatabaseSession()
    try:
        yield session
    finally:
        await session.close()
