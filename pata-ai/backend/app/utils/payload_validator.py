def is_valid_delivery_request(address: str) -> bool:
    return len((address or '').strip()) >= 5
