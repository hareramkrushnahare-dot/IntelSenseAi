"""Session management and transaction helpers."""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Any, AsyncIterator


class DatabaseSession:
    """Lightweight async session wrapper for scaffolded services."""

    def __init__(self) -> None:
        self._closed = False
        self._pending: list[Any] = []

    def add(self, obj: Any) -> None:
        self._pending.append(obj)

    async def execute(self, statement: Any) -> Any:
        return _FakeResult([])

    async def flush(self) -> None:
        return None

    async def refresh(self, obj: Any) -> None:
        return None

    async def commit(self) -> None:
        return None

    async def rollback(self) -> None:
        return None

    async def close(self) -> None:
        self._closed = True


class _FakeResult:
    def __init__(self, rows: list[Any]) -> None:
        self._rows = rows

    def scalars(self) -> "_FakeScalarResult":
        return _FakeScalarResult(self._rows)


class _FakeScalarResult:
    def __init__(self, rows: list[Any]) -> None:
        self._rows = rows

    def all(self) -> list[Any]:
        return self._rows

    async def __aenter__(self) -> "DatabaseSession":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()


@asynccontextmanager
async def get_db() -> AsyncIterator[DatabaseSession]:
    """Yield a database session-like object for dependency injection."""
    session = DatabaseSession()
    try:
        yield session
    finally:
        await session.close()
