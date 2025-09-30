import pytest
from sdsrc.normalize import normalize_whitespace


@pytest.mark.parametrize(
    "text, expected",
    [
        (" hi  there\t friend  ", "hi there friend"),
        ("one\n\n\n\ntwo", "one\n\ntwo"),
        ("alpha\nbeta\n gamma", "alpha\nbeta\ngamma"),
        ("\u00a0hello\u00a0world\u00a0", "hello world"),
    ],
)
def test_normalizes_whitespace_cases(text, expected):
    assert normalize_whitespace(text) == expected
