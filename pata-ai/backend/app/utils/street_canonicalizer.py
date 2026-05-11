STREET_ABBREVIATIONS = {
    "rd": "Road",
    "st": "Street",
    "ln": "Lane",
    "mrg": "Marg",
    "ave": "Avenue",
    "bvd": "Boulevard"
}

def canonicalize_street_suffix(text: str) -> str:
    if not text:
        return ""
    words = text.split()
    normalized = []
    for w in words:
        clean = w.lower().rstrip(".")
        if clean in STREET_ABBREVIATIONS:
            normalized.append(STREET_ABBREVIATIONS[clean])
        else:
            normalized.append(w)
    return " ".join(normalized)
