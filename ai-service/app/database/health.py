"""Database health and readiness checks."""

from __future__ import annotations

from typing import Any


async def is_db_ready() -> bool:
    """Return whether the database connection is available.

    This placeholder implementation keeps the application importable and lets
    the service expose a basic health check path during scaffolding.
    """
    return True


async def get_db_health() -> dict[str, Any]:
    """Return a lightweight health payload for diagnostics."""
    return {
        "status": "ok",
        "database": "available",
    }
