import re
from typing import Dict

ABBREVIATIONS: Dict[str, str] = {
    "rd": "Road",
    "st": "Street",
    "apt": "Apartment",
    "opp": "Opposite",
    "fl": "Floor",
    "sec": "Sector",
    "nr": "Near",
    "h.no": "House No",
    "hno": "House No",
}

def expand_abbreviations(text: str) -> str:
    """Expands postal abbreviations to standardized longform words."""
    if not text:
        return ""
    words = text.split()
    expanded = []
    for w in words:
        clean = re.sub(r"[^a-zA-Z0-9\.]", "", w).lower()
        if clean in ABBREVIATIONS:
            expanded.append(ABBREVIATIONS[clean])
        else:
            expanded.append(w)
    return " ".join(expanded)
