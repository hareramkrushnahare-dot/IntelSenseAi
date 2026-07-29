"""Database configuration settings for the IntelSense AI service.

This module centralizes all database-related configuration values for the
FastAPI service and exposes them through a typed settings object. It is
intended to be used by the SQLAlchemy engine, session management layer,
and any database-dependent service components.
"""

from __future__ import annotations

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """Typed settings for the shared MySQL database integration.

    These values are loaded from environment variables and optional local
    configuration files. The settings object is designed to support both
    local development and production deployment scenarios.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    host: str = Field(default="localhost", alias="DB_HOST")
    port: int = Field(default=3306, alias="DB_PORT")
    username: str = Field(default="root", alias="DB_USERNAME")
    password: str = Field(default="", alias="DB_PASSWORD")
    database: str = Field(default="intelsense_ai", alias="DB_NAME")
    charset: str = Field(default="utf8mb4", alias="DB_CHARSET")
    pool_size: int = Field(default=10, alias="DB_POOL_SIZE")
    max_overflow: int = Field(default=20, alias="DB_MAX_OVERFLOW")
    pool_pre_ping: bool = Field(default=True, alias="DB_POOL_PRE_PING")
    echo: bool = Field(default=False, alias="DB_ECHO")
    ssl_disabled: bool = Field(default=True, alias="DB_SSL_DISABLED")
    connect_timeout: int = Field(default=30, alias="DB_CONNECT_TIMEOUT")
    isolation_level: str = Field(default="READ COMMITTED", alias="DB_ISOLATION_LEVEL")
    timezone: str = Field(default="UTC", alias="DB_TIMEZONE")

    @field_validator("host", "username", "password", "database")
    @classmethod
    def validate_required_strings(cls, value: str) -> str:
        """Ensure string-based database fields are not blank."""
        if value is None:
            return ""
        return value.strip()

    @field_validator("port")
    @classmethod
    def validate_port(cls, value: int) -> int:
        """Ensure the configured database port is valid."""
        if value <= 0 or value > 65535:
            raise ValueError("Database port must be between 1 and 65535")
        return value

    @field_validator("pool_size", "max_overflow", "connect_timeout")
    @classmethod
    def validate_positive_int(cls, value: int) -> int:
        """Ensure numeric database settings are positive."""
        if value <= 0:
            raise ValueError("Database numeric settings must be greater than zero")
        return value

    @property
    def dsn(self) -> str:
        """Build a SQLAlchemy-compatible DSN string for MySQL."""
        password = self.password.replace("@", "%40") if self.password else ""
        return (
            f"mysql+aiomysql://{self.username}:{password}@{self.host}:{self.port}/"
            f"{self.database}?charset={self.charset}"
        )

    @property
    def sync_dsn(self) -> str:
        """Build a synchronous DSN string for migration tooling."""
        password = self.password.replace("@", "%40") if self.password else ""
        return (
            f"mysql+pymysql://{self.username}:{password}@{self.host}:{self.port}/"
            f"{self.database}?charset={self.charset}"
        )

    @property
    def pool_settings(self) -> dict[str, int | bool]:
        """Return SQLAlchemy pool configuration values."""
        return {
            "pool_size": self.pool_size,
            "max_overflow": self.max_overflow,
            "pool_pre_ping": self.pool_pre_ping,
        }

    @property
    def is_configured(self) -> bool:
        """Return whether the database settings appear to be usable."""
        return bool(self.host and self.database and self.username)


settings = DatabaseSettings()
