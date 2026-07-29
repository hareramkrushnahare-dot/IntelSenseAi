try:
    from transformers import pipeline
except Exception:
    pipeline = None

from threading import Lock


class SentimentModel:
    _lock = Lock()

    def __init__(self, model_name: str = "distilbert-base-uncased-finetuned-sst-2-english"):
        self.model_name = model_name
        self._pipe = None

    def _ensure(self):
        if self._pipe is None:
            with SentimentModel._lock:
                if self._pipe is None:
                    if pipeline is None:
                        raise RuntimeError("transformers pipeline not available")
                    self._pipe = pipeline("sentiment-analysis", model=self.model_name, return_all_scores=False)

    def predict(self, text: str):
        self._ensure()
        out = self._pipe(text)
        if isinstance(out, list) and out:
            return out[0]
        return {"label": "neutral", "score": 0.0}
