def get_confidence_tier(confidence_score: float) -> str:
    if confidence_score >= 85.0:
        return "HIGH_CONFIDENCE"
    if confidence_score >= 65.0:
        return "MEDIUM_CONFIDENCE"
    return "LOW_CONFIDENCE_REVIEW_REQUIRED"
