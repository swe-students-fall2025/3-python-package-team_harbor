'''Core driver program of moodsmith'''

import random
from typing import Optional

from .locales import POSITIVE_TEMPLATES


def _bangs(intensity: int) -> str:
    '''
    Converts intensity 0-5 to punctuation, if 0 then "."

    Args:
        intensity: how many "!"s will be added or "."
    '''

    intensity = max(0, min(intensity, 5))
    return "!" * intensity if intensity else "."


def positive(
    language: str = "en",
    name: Optional[str] = None,
    enthusiasm: int = 2,
    seed: Optional[int] = None,
) -> str:
    '''
    Return a short positive message.

    Args:
        language: english, falls back to english if none other written
        name: Optional person to address.
        enthusiasm: 0-5 number of exclamation points (0 -> '.').
        seed: If provided, makes the random
            choice deterministic (useful for tests).
    '''

    # use seed as the same number as running as in test to remove randomness
    # and you will always get the same output for e.g seed 123
    rnd = random.Random(seed)
    templates = POSITIVE_TEMPLATES.get(language, POSITIVE_TEMPLATES["en"])
    punct = _bangs(enthusiasm)
    base = rnd.choice(templates).format(punct=punct)
    prefix = f"{name}, " if name else ""
    return prefix + base
