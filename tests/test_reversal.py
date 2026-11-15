from typing import Any

import pytest

from textutils.reversal import reverse_words


def test_reverses_word_order() -> None:
    assert reverse_words("one two three") == "three two one"


def test_collapses_extra_whitespace() -> None:
    assert reverse_words("  a   b ") == "b a"


def test_single_word() -> None:
    assert reverse_words("solo") == "solo"


@pytest.mark.parametrize("text", ["", "   ", "\t\n"])
def test_empty_or_whitespace_gives_empty(text: str) -> None:
    assert reverse_words(text) == ""


@pytest.mark.parametrize("value", [None, 42, b"a b", ["a"]])
def test_non_str_raises_type_error(value: Any) -> None:
    with pytest.raises(TypeError):
        reverse_words(value)
