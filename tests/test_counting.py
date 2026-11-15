import pytest

from textutils.counting import word_count


def test_basic_and_repeated_spaces() -> None:
    assert word_count("one two  three") == 3


def test_empty_and_whitespace_only() -> None:
    assert word_count("") == 0
    assert word_count("   ") == 0


def test_tabs_and_newlines() -> None:
    assert word_count("one\ttwo\nthree\r\nfour") == 4


def test_leading_trailing_whitespace() -> None:
    assert word_count("  hello world  ") == 2


@pytest.mark.parametrize("value", [None, 5, 1.5, b"a b", ["a"]])
def test_non_str_raises_type_error(value: object) -> None:
    with pytest.raises(TypeError):
        word_count(value)
