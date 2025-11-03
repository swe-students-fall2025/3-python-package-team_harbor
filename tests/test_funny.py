"""funny test for various improper inputs"""

import pytest

from moodsmith.core import funny


def test_funny_intensity_in_range():
    """throws error if intensity inpiut is not valid"""
with pytest.raises(ValueError):
    funny("er", None, -1, 54)


def test_language_not_correct_language_still_prints_english():
    """handles error if language inpiut is not valid"""
    test = funny("hi", None, 1, 54)
    print(test)


def test_name_in_output_string():
    """assures that name is in returned string"""
    test = funny("fr", "joy", 1, 54)
    assert "joy" in (test)
