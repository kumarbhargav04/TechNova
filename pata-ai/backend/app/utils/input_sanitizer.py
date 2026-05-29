import re

def sanitize_address_input(raw_address: str) -> str:
    if not raw_address:
        return ""
    # Strip HTML tags and control characters
    no_html = re.sub(r'<[^>]+>', ' ', raw_address)
    # Collapse multiple whitespaces
    return re.sub(r'\s+', ' ', no_html).strip()
