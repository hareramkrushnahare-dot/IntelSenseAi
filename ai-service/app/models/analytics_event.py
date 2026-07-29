from __future__ import annotations

from sqlalchemy import JSON, Column, DateTime, Integer, String, func

from app.database.base import Base


class AnalyticsEvent(Base):
    __tablename__ = "analytics_events"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String(255), nullable=True)
    sentiment_label = Column(String(64), nullable=True)
    sentiment_score = Column(String(64), nullable=True)
    topics = Column(JSON, nullable=True)
    keywords = Column(JSON, nullable=True)
    aspects = Column(JSON, nullable=True)
    summary = Column(String(4000), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
