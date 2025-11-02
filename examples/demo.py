'''Examples of how moodsmith is used'''

from moodsmith import positive, motivational

print("-- Positive demo --")
print(positive(language="en", name="bob", enthusiasm=3))
print(positive(language="en", seed=123))
# Consistent seed will ensure identical outputs between runs

print("\n== motivational (soft) ==")
print(motivational(language="en", intensity="soft", seed=2))
