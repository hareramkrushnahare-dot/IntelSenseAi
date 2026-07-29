from sqlalchemy import Column, Integer, JSON, ForeignKey
from app.database.base import Base


class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(Integer, primary_key=True)
    prediction_id = Column(Integer, ForeignKey("predictions.id"), nullable=False)
    recommendations = Column(JSON, nullable=False)
