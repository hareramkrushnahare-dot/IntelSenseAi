"""Declarative base for SQLAlchemy models."""

from __future__ import annotations

try:
    from sqlalchemy.orm import DeclarativeBase
except ImportError:  # pragma: no cover - compatibility for SQLAlchemy 1.4
    from sqlalchemy.ext.declarative import declarative_base

    class Base(object):
        """Fallback base class for SQLAlchemy 1.4 style models."""

        __table_args__ = {}

    Base = declarative_base(cls=Base)
else:

    class Base(DeclarativeBase):
        """Base class for SQLAlchemy ORM models in the service."""

        pass
