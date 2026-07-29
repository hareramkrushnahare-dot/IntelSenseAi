def validate_input(text: str, max_length: int = 10000) -> bool:
    return isinstance(text, str) and 0 < len(text) <= max_length
