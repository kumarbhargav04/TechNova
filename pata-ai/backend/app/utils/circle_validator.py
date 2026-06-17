def is_valid_postal_circle(circle_digit: str) -> bool:
    return circle_digit in [str(i) for i in range(1, 10)]
