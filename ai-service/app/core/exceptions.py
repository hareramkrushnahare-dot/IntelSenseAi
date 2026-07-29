"""Core exception definitions for the service."""

from __future__ import annotations


class ServiceError(Exception):
    """Base exception for service-layer failures."""

    def __init__(self, message: str = "Service error", code: int = 500) -> None:
        super().__init__(message)
        self.message = message
        self.code = code


class ConfigurationError(ServiceError):
    """Raised when required configuration is missing or invalid."""

    def __init__(self, message: str = "Configuration error") -> None:
        super().__init__(message, 500)


class DatabaseConnectionError(ServiceError):
    """Raised when a database connection cannot be established."""

    def __init__(self, message: str = "Database connection error") -> None:
        super().__init__(message, 503)


class ExternalServiceError(ServiceError):
    """Raised when an upstream external service call fails."""

    def __init__(self, message: str = "External service error") -> None:
        super().__init__(message, 502)
