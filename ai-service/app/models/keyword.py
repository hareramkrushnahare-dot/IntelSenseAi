from sqlalchemy import Column, Integer, JSON, ForeignKey
from app.database.base import Base


class Keyword(Base):
    __tablename__ = "keywords"
    id = Column(Integer, primary_key=True)
    prediction_id = Column(Integer, ForeignKey("predictions.id"), nullable=False)
    keywords = Column(JSON, nullable=False)
