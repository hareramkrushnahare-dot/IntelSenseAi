from typing import List, Dict, Any


def simple_rule_engine(sentiment: Dict[str, Any], keywords: List[str]) -> List[str]:
    recs = []
    label = sentiment.get("label", "").lower()
    if label == "negative":
        recs.append("Investigate negative feedback for top keywords: " + ", ".join(keywords[:3]))
    else:
        recs.append("Monitor mentions for: " + ", ".join(keywords[:5]))
    return recs
