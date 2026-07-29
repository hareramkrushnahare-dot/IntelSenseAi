from typing import List, Dict, Any


def recommend_actions(sentiment: Dict[str, Any], emotions: Dict[str, float], keywords: List[str], topics: List[str]) -> List[str]:
    recs = []
    label = sentiment.get("label", "").lower()
    if label == "negative":
        recs.append("Investigate complaints related to: " + ", ".join(keywords[:3]))
        recs.append("Prioritize cases with high emotion scores")
    else:
        recs.append("Continue monitoring: " + ", ".join(keywords[:5]))
    return recs
