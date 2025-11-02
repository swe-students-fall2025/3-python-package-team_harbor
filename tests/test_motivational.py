from moodsmith import motivational 

def test_seed_is_deterministic():
    a = motivational(intensity="medium", seed=123)
    b = motivational(intensity="medium", seed=123)
    assert a == b

def test_intensity_fallbacks():
    x = motivational(intensity="medium", seed=1)
    y = motivational(intensity="unknown", seed=1)
    assert x == y

def test_name_prefix():
    s = motivational(name="Eason", seed=5)
    assert s.startswith("Eason, ")
