try:
    from transformers import pipeline
except Exception:
    pipeline = None

from threading import Lock


class SummarizationModel:
    _lock = Lock()

    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        self.model_name = model_name
        self._pipe = None

    def _ensure(self):
        if self._pipe is None:
            with SummarizationModel._lock:
                if self._pipe is None:
                    if pipeline is None:
                        raise RuntimeError("transformers pipeline not available")
                    self._pipe = pipeline("summarization", model=self.model_name)

    def summarize(self, text: str) -> str:
        self._ensure()
        out = self._pipe(text, max_length=150, min_length=30)
        if isinstance(out, list) and out:
            return out[0].get("summary_text", "")
        return ""
