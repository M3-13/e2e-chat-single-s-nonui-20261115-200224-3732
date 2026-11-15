"""Tests for is_palindrome."""

from typing import Any

import pytest

from textutils import is_palindrome


def test_sentence_with_punctuation() -> None:
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_case_insensitive() -> None:
    assert is_palindrome("Racecar") is True


def test_not_a_palindrome() -> None:
    assert is_palindrome("hello") is False


def test_empty_string() -> None:
    assert is_palindrome("") is True


def test_no_alphanumerics() -> None:
    assert is_palindrome(" ,.! ") is True


def test_single_character_and_digits() -> None:
    assert is_palindrome("a") is True
    assert is_palindrome("12321") is True
    assert is_palindrome("12345") is False


@pytest.mark.parametrize("value", [None, 123, 1.5, b"abc", ["a"]])
def test_non_str_raises_type_error(value: Any) -> None:
    with pytest.raises(TypeError):
        is_palindrome(value)
