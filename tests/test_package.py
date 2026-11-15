"""The package exposes its public API."""

import textutils

NAMES = ["slugify", "truncate", "word_count", "is_palindrome", "reverse_words"]


def test_public_names_are_importable_and_callable() -> None:
    for name in NAMES:
        assert callable(getattr(textutils, name))


def test_all_lists_the_public_names() -> None:
    assert sorted(textutils.__all__) == sorted(NAMES)
