"""Text truncation."""

ELLIPSIS = "..."


def truncate(text: str, max_len: int) -> str:
    """Return ``text`` shortened to at most ``max_len`` characters, ending in ``...``.

    Text that already fits is returned unchanged. If ``max_len`` is smaller than
    the ellipsis, the result is the first ``max_len`` characters of ``...``.

    Raises:
        TypeError: if ``text`` is not a ``str``.
        ValueError: if ``max_len`` is negative.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if max_len < 0:
        raise ValueError("max_len must not be negative")
    if len(text) <= max_len:
        return text
    if max_len < len(ELLIPSIS):
        return ELLIPSIS[:max_len]
    return text[: max_len - len(ELLIPSIS)] + ELLIPSIS
