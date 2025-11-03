"""funny test for various improper inputs"""


from moodsmith.core import funny


def test_funny_seed_is_active():
    """throws error if strings arent the same"""
    a=funny("er", None, 1, 54)
    b=funny("er", None, 1, 54)
    assert a==b


def test_language_not_correct_language_still_prints_english():
    """handles error if language inpiut is not valid"""
    test = funny("hi", None, 1, 54)
    print(test)


def test_name_in_output_string():
    """assures that name is in returned string"""
    test = funny("fr", "joy", 1, 54)
    assert "joy" in (test)
