import difflib
def phonetic_similarity(w1: str, w2: str) -> float:
    return round(difflib.SequenceMatcher(None, w1.lower(), w2.lower()).ratio(), 3)
