try:
    from langdetect import detect, DetectorFactory
except Exception:
    def detect(text: str) -> str:
        return "unknown"

    class DetectorFactory:
        seed = 0

DetectorFactory.seed = 0


def detect_language(text: str) -> str:
    try:
        return detect(text)
    except Exception:
        return "unknown"
