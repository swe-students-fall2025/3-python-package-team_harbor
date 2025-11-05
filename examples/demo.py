"""Examples of how Moodsmith is used"""

import moodsmith

# Defaults to 2 exclamation marks and English language
print(f"""
===========================FUNNY MESSAGE===========================
Funny message:
    {moodsmith.funny()}
Funny message in French with a period:
    {moodsmith.funny(language="fr", enthusiasm=0)}
Funny message in Spanish with my name in it and 4 exclamation marks:
    {moodsmith.funny(language="es", enthusiasm=4, name="Eric")}
Funny message with seed (will always generate same phrase):
    {moodsmith.funny(seed=22)}
==================================================================
""")

# Defaults to medium intensity and English language
print(f"""
=======================MOTIVATIONAL MESSAGE=======================
Motivational message:
    {moodsmith.motivational()}
Very motivational message in French:
    {moodsmith.motivational(language="fr", intensity="hard")}
Slightly motivational message in Spanish with my name in it:
    {moodsmith.motivational(language="es", intensity="soft", name="Eric")}
Motivational message with seed (will always generate same phrase):
    {moodsmith.motivational(seed=22)}
==================================================================
""")

# Defaults to 2 exclamation marks, medium intensity, and English language
print(f"""
=========================NEGATIVE MESSAGE=========================
Negative message:
    {moodsmith.negative()}
Very negative message in French with my name in it:
    {moodsmith.negative(language="fr", name="Eric", intensity="hard")}
Slightly negative message in Spanish with 5 exclamation marks:
    {moodsmith.negative(language="es", intensity="soft", enthusiasm=5)}
Negative message with seed (will always generate same phrase):
    {moodsmith.negative(seed=22)}
==================================================================
""")

# Defaults to 2 exclamation marks and English language
print(f"""
=========================POSITIVE MESSAGE=========================
Positive message:
    {moodsmith.positive()}
Positive message in French with my name in it and a period:
    {moodsmith.positive(language="fr", name="Eric", enthusiasm=0)}
Positive message in Spanish with 5 exclamation marks:
    {moodsmith.positive(language="es", enthusiasm=5)}
Positive message with seed (will always generate same phrase):
    {moodsmith.positive(seed=22)}
==================================================================
""")
