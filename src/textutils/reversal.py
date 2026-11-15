"""Word order reversal."""


def reverse_words(text: str) -> str:
    """Return the words of ``text`` in reverse order, separated by single spaces."""
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    return " ".join(reversed(text.split()))
