from typing import Optional
from app.core.config import settings
from app.ai.models.dummy import DummyModels
from app.ai.models.roberta_loader import SentimentModel
from app.ai.models.bart_loader import SummarizationModel


class AIManager:
    _sentiment: Optional[SentimentModel] = None
    _summarizer: Optional[SummarizationModel] = None
    _initialized = False

    @classmethod
    async def initialize(cls, use_dummy: bool = True):
        if cls._initialized:
            return
        if use_dummy:
            DummyModels.register()
            cls._initialized = True
            return
        cls._sentiment = SentimentModel()
        cls._summarizer = SummarizationModel()
        cls._initialized = True
