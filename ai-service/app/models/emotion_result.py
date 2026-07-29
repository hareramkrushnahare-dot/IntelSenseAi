from sqlalchemy import Column, Integer, JSON, ForeignKey
from app.database.base import Base


class EmotionResult(Base):
    __tablename__ = "emotion_results"
    id = Column(Integer, primary_key=True)
    prediction_id = Column(Integer, ForeignKey("predictions.id"), nullable=False)
    emotions = Column(JSON, nullable=False)
