from sqlalchemy import Column, Integer, JSON, ForeignKey
from app.database.base import Base


class AspectResult(Base):
    __tablename__ = "aspect_results"
    id = Column(Integer, primary_key=True)
    prediction_id = Column(Integer, ForeignKey("predictions.id"), nullable=False)
    aspects = Column(JSON, nullable=False)
