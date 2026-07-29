from pydantic import BaseModel
from typing import Optional, Any, Dict, List


class PredictionRequest(BaseModel):
    text: str
    source: Optional[str] = None


class SentimentResult(BaseModel):
    label: str
    score: float


class PredictionResult(BaseModel):
    sentiment: Dict[str, Any]
    emotions: Dict[str, float]
    keywords: List[str]
    topics: List[str]
    summary: Optional[str]
    recommendations: List[str]


class PredictionResponse(BaseModel):
    id: Optional[int]
    input_text: str
    result: PredictionResult
