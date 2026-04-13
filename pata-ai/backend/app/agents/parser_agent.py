import os
import re
import json
from typing import Dict, Any, Optional

PINCODE_PATTERN = re.compile(r"\b([1-9][0-9]{5})\b")
LANDMARK_KEYWORDS = ["near", "opp", "opposite", "behind", "beside", "next to", "adjacent", "front of"]
COMMON_CITIES = ["hyderabad", "secunderabad", "bangalore", "bengaluru", "delhi", "new delhi", "noida", "mumbai"]
COMMON_STATES = ["telangana", "karnataka", "delhi", "uttar pradesh", "up", "maharashtra", "punjab", "ap", "andhra pradesh"]

async def parse_address(normalized_address: str, db: Any = None, evidence_callback = None) -> dict:
    cb = evidence_callback or (lambda *args, **kwargs: None)
    parsed = {"landmark": None, "locality": None, "city": None, "state": None, "pincode": None}
    pincode_match = re.search(r'\b\d{6}\b', normalized_address)
    if pincode_match:
        parsed["pincode"] = pincode_match.group(0)
        cb("Parser Agent", f"Regex extracted pincode: {parsed['pincode']}", 1.0)
    for city in COMMON_CITIES:
        if city in normalized_address.lower():
            parsed["city"] = city.title()
            break
    for state in COMMON_STATES:
        if state in normalized_address.lower():
            parsed["state"] = state.upper() if len(state) <= 3 else state.title()
            break
    parsed["used_llm"] = False
    return parsed


PINCODE_PATTERN = re.compile(r"\b([1-9][0-9]{5})\b")
LANDMARK_KEYWORDS = ["near", "opp", "opposite", "behind", "beside", "next to", "adjacent", "front of"]

def extract_pincode_regex(text: str) -> Optional[str]:
    """Finds first 6-digit Indian PIN code in raw text."""
    match = PINCODE_PATTERN.search(text)
    return match.group(1) if match else None

def extract_landmark_clue(text: str) -> Optional[str]:
    """Extracts landmark hint following common Indian address spatial prepositions."""
    lower = text.lower()
    for kw in LANDMARK_KEYWORDS:
        idx = lower.find(kw)
        if idx != -1:
            clue = text[idx:].split(",")[0].strip()
            if len(clue) > len(kw) + 2:
                return clue
    return None

def tokenize_address(raw_address: str) -> Dict[str, Any]:
    """Tokenizes raw Indian address into PIN, landmark clue, and cleaned tokens."""
    if not raw_address or not raw_address.strip():
        return {"pincode": None, "landmark_clue": None, "tokens": []}

    pincode = extract_pincode_regex(raw_address)
    landmark = extract_landmark_clue(raw_address)
    clean = re.sub(r"[,\.\-#/]", " ", raw_address)
    tokens = [t.strip() for t in clean.split() if len(t.strip()) > 1]

    return {
        "pincode": pincode,
        "landmark_clue": landmark,
        "tokens": tokens
    }
