import pytest

from textutils.truncation import truncate


def test_truncates_with_ellipsis() -> None:
    assert truncate("Hello World", 8) == "Hello..."


def test_short_text_unchanged() -> None:
    assert truncate("Hi", 8) == "Hi"
    assert truncate("Hello", 5) == "Hello"


def test_empty_text() -> None:
    assert truncate("", 0) == ""


@pytest.mark.parametrize(
    ("max_len", "expected"),
    [(0, ""), (1, "."), (2, ".."), (3, "...")],
)
def test_small_max_len(max_len: int, expected: str) -> None:
    assert truncate("Hello", max_len) == expected


def test_never_longer_than_max_len() -> None:
    for n in range(0, 15):
        assert len(truncate("Hello World, long text", n)) <= n


def test_negative_max_len_raises() -> None:
    with pytest.raises(ValueError):
        truncate("Hello", -1)


@pytest.mark.parametrize("bad", [None, 42, b"x", ["a"]])
def test_non_str_raises(bad: object) -> None:
    with pytest.raises(TypeError):
        truncate(bad, 5)
