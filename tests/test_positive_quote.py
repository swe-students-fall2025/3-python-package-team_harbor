import re
from moodsmith import positive_quote

def _count_trailing_bangs(s: str) -> int:
    m = re.search(r"!+$", s)
    return len(m.group(0)) if m else 0

def test_seed_is_deterministic():
    a = positive_quote(language="en", seed=42)
    b = positive_quote(language="en", seed=42)
    assert a == b

def test_incorrect_language():
    msg = positive_quote(language="xx", enthusiasm=3, seed=7)
    assert _count_trailing_bangs(msg) == 3
    english_snippets=["Steve Jobs", "You are", "you are", "Love the"]
    assert any(snippet in msg for snippet in english_snippets)

def test_empty_language():
    msg = positive_quote(enthusiasm=4, seed=7)
    assert _count_trailing_bangs(msg) == 4
    english_snippets=["Steve Jobs", "You are", "you are", "Love the"]
    assert any(snippet in msg for snippet in english_snippets) 

def test_same_seed_different_language():
    a = positive_quote(language="es", seed=42)
    b = positive_quote(language="fr", seed=42)
    assert a != b

def test_enthusiasm_zero_ends_with_fullstop():
    msg = positive_quote(language="en", enthusiasm=0, seed=3)
    assert msg.endswith(".")    