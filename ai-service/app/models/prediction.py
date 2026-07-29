from __future__ import annotations

from sqlalchemy import JSON, Column, DateTime, Integer, String, func

from app.database.base import Base


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    input_text = Column(String(4000), nullable=False)
    source = Column(String(255), nullable=True)
    result = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
