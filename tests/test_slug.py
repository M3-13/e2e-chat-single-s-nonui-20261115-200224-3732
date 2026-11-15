from typing import Any

import pytest

from textutils import slugify


def test_basic() -> None:
    assert slugify("Hello, World!") == "hello-world"


def test_accents_and_separators() -> None:
    assert slugify("  Crème  Brûlée -- Rezept ") == "creme-brulee-rezept"


@pytest.mark.parametrize("text", ["", "!!!", "   ", "---"])
def test_empty_or_symbol_only(text: str) -> None:
    assert slugify(text) == ""


def test_digits_and_collapsing() -> None:
    assert slugify("a___b  2024") == "a-b-2024"


@pytest.mark.parametrize("value", [None, 5, 1.5, b"abc", ["a"]])
def test_non_str_raises(value: Any) -> None:
    with pytest.raises(TypeError):
        slugify(value)
