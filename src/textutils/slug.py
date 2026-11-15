"""URL slug generation."""

import re
import unicodedata

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Return a lowercase, ASCII, hyphen-separated slug of ``text``."""
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    normalized = unicodedata.normalize("NFKD", text.lower())
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    return _NON_ALNUM.sub("-", ascii_text).strip("-")
