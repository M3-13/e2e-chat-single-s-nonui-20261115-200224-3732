"""Palindrome check."""


def is_palindrome(text: str) -> bool:
    """Return whether ``text`` reads the same backwards, ignoring case and punctuation.

    Only alphanumeric characters count. Text without any is a palindrome.
    Raises TypeError for a non-str ``text``.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    chars = [c.casefold() for c in text if c.isalnum()]
    return chars == chars[::-1]
