#motivational.py
from __future__ import annotations

import json
import random
from typing import List, Literal, Optional
from importlib import resources
from pathlib import Path

Intensity = Literal["soft", "medium", "hard"]
Language = Literal["en"]

_DATA_CACHE = {}

def _load_data(language: Language) -> dict:
    """
    Load motivational data. Search order:
    1) Package data: lyfestyle/data/motivational_<lang>.json  (preferred for PyPI)
    2) Project root:        data/motivational_<lang>.json
    3) CWD-relative:        ./data/motivational_<lang>.json
    """
    if language in _DATA_CACHE:
        return _DATA_CACHE[language]

    filename = f"motivational_{language}.json"

    try:
        pkg_file = resources.files(__package__).joinpath("data").joinpath(filename)
        if pkg_file.is_file():
            with pkg_file.open("r", encoding="utf-8") as f:
                payload = json.load(f)
            _validate_payload(payload, filename)
            _DATA_CACHE[language] = payload
            return payload
    except Exception:
        pass

    this_file = Path(__file__).resolve()
    package_dir = this_file.parent                
    project_root = package_dir.parent 

    candidate_project = project_root / "data" / filename
    if candidate_project.is_file():
        with candidate_project.open("r", encoding="utf-8") as f:
            payload = json.load(f)
        _validate_payload(payload, filename)
        _DATA_CACHE[language] = payload
        return payload

    candidate_cwd = Path.cwd() / "data" / filename
    if candidate_cwd.is_file():
        with candidate_cwd.open("r", encoding="utf-8") as f:
            payload = json.load(f)
        _validate_payload(payload, filename)
        _DATA_CACHE[language] = payload
        return payload

    raise FileNotFoundError(
        "Motivational data file not found. Tried:\n"
        f" - package: lyfestyle/data/{filename}\n"
        f" - project : {candidate_project}\n"
        f" - cwd     : {candidate_cwd}\n"
        "Tip: keep data in lyfestyle/data/ for packaging to PyPI."
    )

def _validate_payload(payload: dict, filename: str) -> None:
    for level in ("soft", "medium", "hard"):
        if level not in payload or not isinstance(payload[level], list):
            raise ValueError(f"Invalid data for '{level}' in {filename}")

def motivate(
    *,
    language: Language = "en",
    intensity: Intensity = "medium",
    n: int = 1,
    unique: bool = True,
    seed: Optional[int] = None,
) -> List[str]:
    """
    Return n motivational sentences chosen by language & intensity.
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    data = _load_data(language)
    pool = list(data[intensity])

    rng = random.Random(seed)

    if not pool:
        return []

    if unique:
        rng.shuffle(pool)
        return pool[: min(n, len(pool))]
    else:
        return [rng.choice(pool) for _ in range(n)]

def format_motivation(
    messages: List[str],
    *,
    prefix: str = "💡 ",
    suffix: str = "",
    join_with: str = "\n",
    uppercase: bool = False,
) -> str:
    """Format sentences for display."""
    out = []
    for m in messages:
        text = m.upper() if uppercase else m
        out.append(f"{prefix}{text}{suffix}")
    return join_with.join(out)
