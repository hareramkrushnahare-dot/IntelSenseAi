from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base


class Summary(Base):
    __tablename__ = "summaries"
    id = Column(Integer, primary_key=True)
    prediction_id = Column(Integer, ForeignKey("predictions.id"), nullable=False)
    summary_text = Column(String(4000))
