from normalize import normalize_whitespace

def test_collapses_spaces_tabs_and_trims():
    assert normalize_whitespace(" hi  there\t friend ") == "hi there friend"

def test_collapses_blank_lines_to_single_newline():
    text = "one\n\n\n\ntwo"
    assert normalize_whitespace(text) == "one\n\ntwo"

def test_preserves_single_newlines_between_lines():
    text = "alpha\nbeta\n gamma"
    assert normalize_whitespace(text) == "alpha\nbeta\ngamma"


