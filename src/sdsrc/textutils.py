import re


def count_words(text: str) -> int:
    """
    Count the number of words in a string.
    Words are defined as sequences of non-space characters separated by whitespace or punctuation.
    """

    # \w+ matches "word characters" (letters, digits, underscrore)
    words = re.findall(r"[A-Za-z0-9']+", text)
    return len(words)


def reverse_words(text: str) -> str:
    """
    Reverse the order of words in the string.
    Words are defined the same way as in count_words:
    separated by whitespace or punctuation.
    """

    words = re.findall(r"[A-Za-z0-9']+", text)
    return " ".join(reversed(words))


def word_frequencies(text: str) -> dict[str, int]:
    """
    Counts the frequency of words in the string.
    Words are defined the same way as in count_words.
    """

    words = re.findall(r"[A-Za-z0-9']+", text.lower())
    counts: dict[str, int] = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def summarize_text(text: str) -> dict:
    """
    Summarizes the word count. Provides frequencies of words."""

    words = re.findall(r"[A-Za-z0-9']+", text.lower())
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return {"word_count": len(words), "frequencies": counts}


def top_n_words(text: str, number: int) -> list[tuple[str, int]]:
    """
    Return the top N most frequent words in the text as (word, count) pairs.
    """
    words = re.findall(r"[A-Za-z0-9']+", text.lower())
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_items[:number]
