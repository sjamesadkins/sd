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
