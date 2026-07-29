import re
import html

URL_RE = re.compile(r"https?://\S+")
HTML_TAG_RE = re.compile(r"<[^>]+>")


def clean_text(text: str) -> str:
    if text is None:
        return ""
    t = html.unescape(text)
    t = re.sub(HTML_TAG_RE, " ", t)
    t = re.sub(URL_RE, " ", t)
    t = t.replace("\n", " ").strip()
    t = re.sub(r"\s+", " ", t)
    return t
