from moodsmith.core import funny

import pytest

def test_funny_intensity_in_range():

    with pytest.raises(ValueError):
        funny("er",None,-1,54)

def test_language_not_correct_language_still_prints_english():

    test=funny("hi",None,1,54)
    print(test)

def test_name_in_output_string():
    test=funny("fr","joy",1,54)
    assert "joy" in (test)
    
