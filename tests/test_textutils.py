import pytest
from sdsrc.textutils import count_words, reverse_words, word_frequencies, summarize_text
# from sdsrc.textutils import reverse_words
# from sdsrc.textutils import word_frequencies
# from sdsrc.textutils import summarize_text

@pytest.mark.parametrize(
    "text, expected",
    [
        ("one two three", 3),
        ("   spaced   out   ", 2),
        ("", 0),
        ("Hello, world!", 2),
        ("Wait... what?!", 2),
        ("Python's great", 2),
        ("hi, hi, hi", 3),
        ("end.", 1),
    ],
)

def test_count_words_various_cases(text, expected):
    assert count_words(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("one two three", "three two one"),
        ("   spaced    out     ", "out spaced"),
        ("", ""),
        ("Hello, world!", "world Hello"),
    ],
)

def test_reverse_words_various_cases(text, expected):
    assert reverse_words(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("one two two three", {"one": 1, "two": 2, "three": 1}),
        ("Repeat repeat REPEAT", {"repeat": 3}),
        ("", {}),
        ("Hi!, Hi, hi.", {"hi": 3}),
    ],
)

def test_word_frequencies_various_cases(text, expected):
    assert word_frequencies(text) == expected


def test_summarize_text_basic():
    result = summarize_text("Hello,     hello world!")
    assert result["word_count"] == 3
    assert result["frequencies"] == {"hello": 2, "world": 1}
